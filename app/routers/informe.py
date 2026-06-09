"""
routers/informe.py
Endpoint de informe MVP con métricas de solicitudes.
"""
from fastapi import APIRouter, Depends
from pymongo.collection import Collection

from app.core import database as database_utils
from app.core.security import require_role
from app.services import informe_service

router = APIRouter(prefix="/api/informe", tags=["Informe"])


def get_collection():
    """Dependencia local para que las pruebas puedan mockearla por ruta del módulo."""
    return database_utils.get_collection()


@router.get(
    "",
    summary="Informe de métricas MVP",
    dependencies=[Depends(require_role("soporte", "administrador"))],
)
def informe(col: Collection = Depends(lambda: get_collection())):
    """
    Retorna métricas del sistema desde la colección `COLECCION`:
    - Total de solicitudes
    - Cantidad por estado
    - Tiempo promedio de resolución (horas)
    - Solicitudes sin asignar

    Acceso: `soporte` | `administrador`.
    """
    return informe_service.generar_informe(col)
