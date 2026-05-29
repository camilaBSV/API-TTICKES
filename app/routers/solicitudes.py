"""
routers/solicitudes.py
Endpoints de gestión de solicitudes de soporte técnico.
Colección utilizada: definida en COLECCION (.env) → colecciontest0
"""
from typing import Optional

from fastapi import APIRouter, Depends, Query
from pymongo.collection import Collection

from app.core.database import get_collection
from app.core.security import get_current_user, require_role
from app.models.solicitud import (
    SolicitudAsignacion,
    SolicitudCreate,
    SolicitudEstadoUpdate,
)
from app.services import solicitud_service

router = APIRouter(prefix="/api/solicitudes", tags=["Solicitudes"])


# ── Crear solicitud ───────────────────────────────────────────────────────────

@router.post("", status_code=201, summary="Crear solicitud de soporte")
def crear(
    datos: SolicitudCreate,
    current_user: dict = Depends(get_current_user),
    col: Collection = Depends(get_collection),
):
    """
    Crea una nueva solicitud de soporte técnico en la colección `COLECCION`.
    Acceso: todos los roles autenticados.
    """
    return solicitud_service.crear_solicitud(col, datos, current_user["usuario_id"])


# ── Listar solicitudes ────────────────────────────────────────────────────────

@router.get("", summary="Listar solicitudes con filtros opcionales")
def listar(
    usuario_id: Optional[str] = Query(None, description="Filtrar por usuario creador"),
    estado: Optional[str] = Query(None, description="Filtrar por estado"),
    asignado_id: Optional[str] = Query(None, description="Filtrar por responsable asignado"),
    skip: int = Query(0, ge=0),
    limit: int = Query(20, ge=1, le=100),
    current_user: dict = Depends(get_current_user),
    col: Collection = Depends(get_collection),
):
    """
    Lista solicitudes con filtros opcionales.
    - `usuario` solo ve sus propias solicitudes (se fuerza `usuario_id`).
    - `soporte` y `administrador` pueden ver todas.
    """
    if current_user["rol"] == "usuario":
        usuario_id = current_user["usuario_id"]

    return solicitud_service.listar_solicitudes(col, usuario_id, estado, asignado_id, skip, limit)


# ── Obtener solicitud por ID ──────────────────────────────────────────────────

@router.get("/{solicitud_id}", summary="Obtener solicitud por ID")
def obtener(
    solicitud_id: str,
    current_user: dict = Depends(get_current_user),
    col: Collection = Depends(get_collection),
):
    """
    Retorna una solicitud específica.
    - `usuario` solo puede consultar sus propias solicitudes.
    """
    doc = solicitud_service.obtener_solicitud(col, solicitud_id)
    if current_user["rol"] == "usuario" and doc["usuario_id"] != current_user["usuario_id"]:
        from fastapi import HTTPException, status
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="No autorizado.")
    return doc


# ── Actualizar estado ─────────────────────────────────────────────────────────

@router.patch(
    "/{solicitud_id}/estado",
    summary="Actualizar estado de una solicitud",
    dependencies=[Depends(require_role("soporte", "administrador"))],
)
def actualizar_estado(
    solicitud_id: str,
    datos: SolicitudEstadoUpdate,
    current_user: dict = Depends(get_current_user),
    col: Collection = Depends(get_collection),
):
    """
    Cambia el estado de una solicitud.
    Estados válidos: `creada` | `en_revision` | `en_proceso` | `resuelta` | `cerrada`.
    Acceso: `soporte` | `administrador`.
    """
    return solicitud_service.actualizar_estado(col, solicitud_id, datos, current_user["usuario_id"])


# ── Asignar solicitud ─────────────────────────────────────────────────────────

@router.patch(
    "/{solicitud_id}/asignar",
    summary="Asignar solicitud a un responsable",
    dependencies=[Depends(require_role("soporte", "administrador"))],
)
def asignar(
    solicitud_id: str,
    datos: SolicitudAsignacion,
    current_user: dict = Depends(get_current_user),
    col: Collection = Depends(get_collection),
):
    """
    Asigna la solicitud a un miembro del equipo de soporte.
    Acceso: `soporte` | `administrador`.
    """
    return solicitud_service.asignar_solicitud(col, solicitud_id, datos, current_user["usuario_id"])
