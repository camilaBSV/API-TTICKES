"""
tests/test_solicitudes.py
Pruebas unitarias e integración para los endpoints de solicitudes.
Usa TestClient de FastAPI con mocks de MongoDB para pruebas unitarias.
"""
import pytest
from unittest.mock import MagicMock, patch
from fastapi.testclient import TestClient
from bson import ObjectId
from datetime import datetime, timezone

from main import app
from app.core.security import create_access_token

# ── Fixtures ──────────────────────────────────────────────────────────────────

def token_usuario():
    return create_access_token({"sub": "usr_test_001", "rol": "usuario", "nombre": "Test User"})

def token_soporte():
    return create_access_token({"sub": "usr_soporte_001", "rol": "soporte", "nombre": "Soporte"})

def token_admin():
    return create_access_token({"sub": "usr_admin_001", "rol": "administrador", "nombre": "Admin"})

def headers_usuario():
    return {"Authorization": f"Bearer {token_usuario()}"}

def headers_soporte():
    return {"Authorization": f"Bearer {token_soporte()}"}

def headers_admin():
    return {"Authorization": f"Bearer {token_admin()}"}


# ── Documento mock ────────────────────────────────────────────────────────────

def mock_solicitud_doc(estado="creada", asignado_id=None):
    oid = ObjectId()
    ahora = datetime.now(timezone.utc)
    return {
        "_id": oid,
        "titulo": "Error en acceso al sistema",
        "descripcion": "No puedo iniciar sesión desde esta mañana.",
        "estado": estado,
        "prioridad": "alta",
        "usuario_id": "usr_test_001",
        "asignado_id": asignado_id,
        "eventos": [{"estado": "creada", "fecha": ahora, "actor_id": "usr_test_001", "comentario": "Creada."}],
        "fecha_creacion": ahora,
        "fecha_actualizacion": ahora,
    }


# ── Tests: Crear solicitud ────────────────────────────────────────────────────

class TestCrearSolicitud:

    def test_crear_solicitud_exitosa(self):
        """Creación de solicitud con campos válidos."""
        mock_col = MagicMock()
        oid = ObjectId()
        mock_col.insert_one.return_value = MagicMock(inserted_id=oid)

        with patch("app.routers.solicitudes.get_collection", return_value=mock_col):
            with TestClient(app) as client:
                resp = client.post(
                    "/api/solicitudes",
                    json={"titulo": "Error en sistema", "descripcion": "No funciona desde ayer.", "prioridad": "alta"},
                    headers=headers_usuario(),
                )
        assert resp.status_code == 201
        data = resp.json()
        assert data["titulo"] == "Error en sistema"
        assert data["estado"] == "creada"

    def test_crear_solicitud_sin_autenticacion(self):
        """Crear solicitud sin token debe retornar 401."""
        with TestClient(app) as client:
            resp = client.post(
                "/api/solicitudes",
                json={"titulo": "Test", "descripcion": "Descripción larga.", "prioridad": "media"},
            )
        assert resp.status_code == 401

    def test_crear_solicitud_prioridad_invalida(self):
        """Prioridad no válida debe retornar 422."""
        mock_col = MagicMock()

        with patch("app.routers.solicitudes.get_collection", return_value=mock_col):
            with TestClient(app) as client:
                resp = client.post(
                    "/api/solicitudes",
                    json={"titulo": "Error", "descripcion": "Descripción del problema.", "prioridad": "urgentisima"},
                    headers=headers_usuario(),
                )
        assert resp.status_code == 422

    def test_crear_solicitud_titulo_muy_corto(self):
        """Título menor a 3 caracteres debe retornar 422."""
        with TestClient(app) as client:
            resp = client.post(
                "/api/solicitudes",
                json={"titulo": "AB", "descripcion": "Descripción válida.", "prioridad": "media"},
                headers=headers_usuario(),
            )
        assert resp.status_code == 422


# ── Tests: Consulta de solicitud ──────────────────────────────────────────────

class TestObtenerSolicitud:

    def test_obtener_solicitud_existente(self):
        """Consultar solicitud existente retorna 200."""
        doc = mock_solicitud_doc()
        oid_str = str(doc["_id"])
        mock_col = MagicMock()
        mock_col.find_one.return_value = doc

        with patch("app.routers.solicitudes.get_collection", return_value=mock_col):
            with TestClient(app) as client:
                resp = client.get(f"/api/solicitudes/{oid_str}", headers=headers_usuario())
        assert resp.status_code == 200
        assert resp.json()["titulo"] == "Error en acceso al sistema"

    def test_obtener_solicitud_no_existente(self):
        """ID no encontrado debe retornar 404."""
        mock_col = MagicMock()
        mock_col.find_one.return_value = None
        oid_str = str(ObjectId())

        with patch("app.routers.solicitudes.get_collection", return_value=mock_col):
            with TestClient(app) as client:
                resp = client.get(f"/api/solicitudes/{oid_str}", headers=headers_soporte())
        assert resp.status_code == 404

    def test_obtener_solicitud_id_invalido(self):
        """ID con formato inválido debe retornar 400."""
        mock_col = MagicMock()
        with patch("app.routers.solicitudes.get_collection", return_value=mock_col):
            with TestClient(app) as client:
                resp = client.get("/api/solicitudes/id-invalido-xyz", headers=headers_soporte())
        assert resp.status_code == 400

    def test_usuario_no_puede_ver_solicitud_ajena(self):
        """Usuario no puede consultar solicitud de otro usuario (403)."""
        doc = mock_solicitud_doc()
        doc["usuario_id"] = "otro_usuario_999"
        oid_str = str(doc["_id"])
        mock_col = MagicMock()
        mock_col.find_one.return_value = doc

        with patch("app.routers.solicitudes.get_collection", return_value=mock_col):
            with TestClient(app) as client:
                resp = client.get(f"/api/solicitudes/{oid_str}", headers=headers_usuario())
        assert resp.status_code == 403


# ── Tests: Actualización de estado ───────────────────────────────────────────

class TestActualizarEstado:

    def test_actualizar_estado_valido(self):
        """Soporte puede cambiar estado a en_proceso (200)."""
        doc = mock_solicitud_doc(estado="en_proceso")
        mock_col = MagicMock()
        mock_col.find_one_and_update.return_value = doc
        oid_str = str(doc["_id"])

        with patch("app.routers.solicitudes.get_collection", return_value=mock_col):
            with TestClient(app) as client:
                resp = client.patch(
                    f"/api/solicitudes/{oid_str}/estado",
                    json={"estado": "en_proceso", "comentario": "Revisando."},
                    headers=headers_soporte(),
                )
        assert resp.status_code == 200
        assert resp.json()["estado"] == "en_proceso"

    def test_actualizar_estado_invalido(self):
        """Estado no válido debe retornar 422."""
        mock_col = MagicMock()
        oid_str = str(ObjectId())

        with patch("app.routers.solicitudes.get_collection", return_value=mock_col):
            with TestClient(app) as client:
                resp = client.patch(
                    f"/api/solicitudes/{oid_str}/estado",
                    json={"estado": "volando"},
                    headers=headers_soporte(),
                )
        assert resp.status_code == 422

    def test_usuario_no_puede_cambiar_estado(self):
        """Rol usuario no puede actualizar estado (403)."""
        oid_str = str(ObjectId())
        with TestClient(app) as client:
            resp = client.patch(
                f"/api/solicitudes/{oid_str}/estado",
                json={"estado": "resuelta"},
                headers=headers_usuario(),
            )
        assert resp.status_code == 403


# ── Tests: Asignación ─────────────────────────────────────────────────────────

class TestAsignar:

    def test_asignar_solicitud(self):
        """Soporte puede asignar solicitud (200)."""
        doc = mock_solicitud_doc(asignado_id="usr_soporte_001")
        mock_col = MagicMock()
        mock_col.find_one_and_update.return_value = doc
        oid_str = str(doc["_id"])

        with patch("app.routers.solicitudes.get_collection", return_value=mock_col):
            with TestClient(app) as client:
                resp = client.patch(
                    f"/api/solicitudes/{oid_str}/asignar",
                    json={"asignado_id": "usr_soporte_001"},
                    headers=headers_soporte(),
                )
        assert resp.status_code == 200
        assert resp.json()["asignado_id"] == "usr_soporte_001"

    def test_usuario_no_puede_asignar(self):
        """Rol usuario no puede asignar (403)."""
        oid_str = str(ObjectId())
        with TestClient(app) as client:
            resp = client.patch(
                f"/api/solicitudes/{oid_str}/asignar",
                json={"asignado_id": "alguien"},
                headers=headers_usuario(),
            )
        assert resp.status_code == 403


# ── Tests: Informe ────────────────────────────────────────────────────────────

class TestInforme:

    def test_informe_accesible_por_soporte(self):
        """Soporte puede obtener el informe MVP (200)."""
        mock_col = MagicMock()
        mock_col.count_documents.side_effect = [10, 3]  # total, sin_asignar
        mock_col.aggregate.side_effect = [
            iter([{"_id": "creada", "cantidad": 4}, {"_id": "resuelta", "cantidad": 6}]),
            iter([{"_id": None, "promedio_ms": 7200000}]),
        ]
        with patch("app.routers.informe.get_collection", return_value=mock_col):
            with TestClient(app) as client:
                resp = client.get("/api/informe", headers=headers_soporte())
        assert resp.status_code == 200
        data = resp.json()
        assert data["total_solicitudes"] == 10
        assert data["tiempo_promedio_resolucion_horas"] == 2.0

    def test_informe_no_accesible_por_usuario(self):
        """Rol usuario no puede acceder al informe (403)."""
        with TestClient(app) as client:
            resp = client.get("/api/informe", headers=headers_usuario())
        assert resp.status_code == 403

    def test_informe_sin_autenticacion(self):
        """Sin token el informe retorna 401."""
        with TestClient(app) as client:
            resp = client.get("/api/informe")
        assert resp.status_code == 401


# ── Tests: Health ─────────────────────────────────────────────────────────────

class TestHealth:

    def test_health_ok(self):
        """El endpoint /health debe retornar status ok."""
        with TestClient(app) as client:
            resp = client.get("/health")
        assert resp.status_code == 200
        assert resp.json()["status"] == "ok"
