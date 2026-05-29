"""
services/solicitud_service.py
Lógica de negocio para la gestión de solicitudes de soporte técnico.
Opera sobre la colección definida en COLECCION (.env).
"""
import logging
from datetime import datetime, timezone
from typing import Optional

from bson import ObjectId
from bson.errors import InvalidId
from fastapi import HTTPException, status
from pymongo.collection import Collection

from app.models.solicitud import (
    ESTADOS_VALIDOS,
    PRIORIDADES_VALIDAS,
    SolicitudAsignacion,
    SolicitudCreate,
    SolicitudEstadoUpdate,
)

logger = logging.getLogger(__name__)


def _doc_to_response(doc: dict) -> dict:
    """Convierte documento MongoDB a dict serializable."""
    doc["id"] = str(doc.pop("_id"))
    return doc


def crear_solicitud(col: Collection, datos: SolicitudCreate, usuario_id: str) -> dict:
    if datos.prioridad not in PRIORIDADES_VALIDAS:
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            detail=f"Prioridad inválida. Valores permitidos: {PRIORIDADES_VALIDAS}",
        )
    ahora = datetime.now(timezone.utc)
    doc = {
        "titulo": datos.titulo,
        "descripcion": datos.descripcion,
        "estado": "creada",
        "prioridad": datos.prioridad,
        "usuario_id": usuario_id,
        "asignado_id": None,
        "eventos": [
            {"estado": "creada", "fecha": ahora, "actor_id": usuario_id, "comentario": "Solicitud creada."}
        ],
        "fecha_creacion": ahora,
        "fecha_actualizacion": ahora,
    }
    result = col.insert_one(doc)
    doc["_id"] = result.inserted_id
    logger.info(f"Solicitud creada: {result.inserted_id} por usuario {usuario_id}")
    return _doc_to_response(doc)


def obtener_solicitud(col: Collection, solicitud_id: str) -> dict:
    try:
        oid = ObjectId(solicitud_id)
    except InvalidId:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="ID de solicitud inválido.")
    doc = col.find_one({"_id": oid})
    if not doc:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Solicitud no encontrada.")
    return _doc_to_response(doc)


def listar_solicitudes(
    col: Collection,
    usuario_id: Optional[str] = None,
    estado: Optional[str] = None,
    asignado_id: Optional[str] = None,
    skip: int = 0,
    limit: int = 20,
) -> list[dict]:
    filtro = {}
    if usuario_id:
        filtro["usuario_id"] = usuario_id
    if estado:
        if estado not in ESTADOS_VALIDOS:
            raise HTTPException(
                status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
                detail=f"Estado inválido. Valores permitidos: {ESTADOS_VALIDOS}",
            )
        filtro["estado"] = estado
    if asignado_id:
        filtro["asignado_id"] = asignado_id

    cursor = col.find(filtro).sort("fecha_creacion", -1).skip(skip).limit(limit)
    return [_doc_to_response(doc) for doc in cursor]


def actualizar_estado(
    col: Collection,
    solicitud_id: str,
    datos: SolicitudEstadoUpdate,
    actor_id: str,
) -> dict:
    if datos.estado not in ESTADOS_VALIDOS:
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            detail=f"Estado inválido. Valores permitidos: {ESTADOS_VALIDOS}",
        )
    try:
        oid = ObjectId(solicitud_id)
    except InvalidId:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="ID de solicitud inválido.")

    ahora = datetime.now(timezone.utc)
    evento = {
        "estado": datos.estado,
        "fecha": ahora,
        "actor_id": actor_id,
        "comentario": datos.comentario,
    }
    result = col.find_one_and_update(
        {"_id": oid},
        {
            "$set": {"estado": datos.estado, "fecha_actualizacion": ahora},
            "$push": {"eventos": evento},
        },
        return_document=True,
    )
    if not result:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Solicitud no encontrada.")
    logger.info(f"Solicitud {solicitud_id} → estado '{datos.estado}' por {actor_id}")
    return _doc_to_response(result)


def asignar_solicitud(
    col: Collection,
    solicitud_id: str,
    datos: SolicitudAsignacion,
    actor_id: str,
) -> dict:
    try:
        oid = ObjectId(solicitud_id)
    except InvalidId:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="ID de solicitud inválido.")

    ahora = datetime.now(timezone.utc)
    evento = {
        "estado": "asignada",
        "fecha": ahora,
        "actor_id": actor_id,
        "comentario": datos.comentario or f"Asignada a {datos.asignado_id}",
    }
    result = col.find_one_and_update(
        {"_id": oid},
        {
            "$set": {"asignado_id": datos.asignado_id, "fecha_actualizacion": ahora},
            "$push": {"eventos": evento},
        },
        return_document=True,
    )
    if not result:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Solicitud no encontrada.")
    logger.info(f"Solicitud {solicitud_id} asignada a {datos.asignado_id} por {actor_id}")
    return _doc_to_response(result)
