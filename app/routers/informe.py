"""
routers/informe.py
Endpoint de informe MVP con métricas de solicitudes.
"""
from fastapi import APIRouter, Depends
from pymongo.collection import Collection

from app.core.database import get_collection
from app.core.security import require_role
from app.services import informe_service

router = APIRouter(prefix="/api/informe", tags=["Informe"])


@router.get(
    "",
    summary="Informe de métricas MVP",
    dependencies=[Depends(require_role("soporte", "administrador"))],
)
def informe(col: Collection = Depends(get_collection)):
    """
    Retorna métricas del sistema desde la colección `COLECCION`:
    - Total de solicitudes
    - Cantidad por estado
    - Tiempo promedio de resolución (horas)
    - Solicitudes sin asignar

    Acceso: `soporte` | `administrador`.
    """
    return informe_service.generar_informe(col)
