"""
models/solicitud.py
Esquemas Pydantic para Solicitudes (tickets) de soporte técnico.
"""
from datetime import datetime, timezone
from typing import List, Optional
from pydantic import BaseModel, Field


# ── Enums como literales ──────────────────────────────────────────────────────

EstadoLiteral = str   # creada | en_revision | en_proceso | resuelta | cerrada
PrioridadLiteral = str  # baja | media | alta | critica

ESTADOS_VALIDOS = {"creada", "en_revision", "en_proceso", "resuelta", "cerrada"}
PRIORIDADES_VALIDAS = {"baja", "media", "alta", "critica"}


# ── Evento de historial embebido ──────────────────────────────────────────────

class Evento(BaseModel):
    estado: str
    fecha: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    actor_id: str
    comentario: Optional[str] = None


# ── Schemas de entrada ────────────────────────────────────────────────────────

class SolicitudCreate(BaseModel):
    titulo: str = Field(..., min_length=3, max_length=200)
    descripcion: str = Field(..., min_length=10)
    prioridad: str = Field(default="media")

    model_config = {"json_schema_extra": {
        "example": {
            "titulo": "Error al iniciar sesión",
            "descripcion": "No puedo acceder al sistema desde esta mañana. Aparece error 401.",
            "prioridad": "alta"
        }
    }}


class SolicitudEstadoUpdate(BaseModel):
    estado: str
    comentario: Optional[str] = None

    model_config = {"json_schema_extra": {
        "example": {"estado": "en_proceso", "comentario": "Revisando el incidente."}
    }}


class SolicitudAsignacion(BaseModel):
    asignado_id: str
    comentario: Optional[str] = None

    model_config = {"json_schema_extra": {
        "example": {"asignado_id": "usr_890", "comentario": "Asignado al técnico Carlos."}
    }}


# ── Schema de respuesta ───────────────────────────────────────────────────────

class SolicitudResponse(BaseModel):
    id: str
    titulo: str
    descripcion: str
    estado: str
    prioridad: str
    usuario_id: str
    asignado_id: Optional[str] = None
    eventos: List[Evento] = []
    fecha_creacion: datetime
    fecha_actualizacion: datetime

    model_config = {"populate_by_name": True}
