"""
services/usuario_service.py
Lógica de negocio para registro y autenticación de usuarios.
"""
import logging
from datetime import datetime, timezone

from fastapi import HTTPException, status
from pymongo.collection import Collection

from app.core.security import create_access_token, hash_password, verify_password
from app.models.usuario import TokenResponse, UsuarioCreate

logger = logging.getLogger(__name__)

ROLES_VALIDOS = {"usuario", "soporte", "administrador"}


def _doc_to_response(doc: dict) -> dict:
    doc["id"] = str(doc.pop("_id"))
    doc.pop("password_hash", None)
    return doc


def registrar_usuario(col: Collection, datos: UsuarioCreate) -> dict:
    if datos.rol not in ROLES_VALIDOS:
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            detail=f"Rol inválido. Valores permitidos: {ROLES_VALIDOS}",
        )
    if col.find_one({"email": datos.email}):
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="Ya existe un usuario con ese email.",
        )
    doc = {
        "nombre": datos.nombre,
        "email": datos.email,
        "password_hash": hash_password(datos.password),
        "rol": datos.rol,
        "activo": True,
        "fecha_creacion": datetime.now(timezone.utc),
    }
    result = col.insert_one(doc)
    doc["_id"] = result.inserted_id
    logger.info(f"Usuario registrado: {datos.email} con rol {datos.rol}")
    return _doc_to_response(doc)


def autenticar_usuario(col: Collection, email: str, password: str) -> TokenResponse:
    usuario = col.find_one({"email": email})
    if not usuario or not verify_password(password, usuario.get("password_hash", "")):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Credenciales incorrectas.",
            headers={"WWW-Authenticate": "Bearer"},
        )
    if not usuario.get("activo", True):
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Usuario inactivo.")

    token = create_access_token({
        "sub": str(usuario["_id"]),
        "rol": usuario["rol"],
        "nombre": usuario["nombre"],
    })
    logger.info(f"Login exitoso: {email}")
    return TokenResponse(access_token=token)
