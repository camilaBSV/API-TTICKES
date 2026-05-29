"""
services/informe_service.py
Generación del informe MVP con métricas desde la colección definida en COLECCION.
"""
import logging
from datetime import datetime, timezone

from pymongo.collection import Collection

logger = logging.getLogger(__name__)


def generar_informe(col: Collection) -> dict:
    """
    Informe MVP con:
    - Volumen total de solicitudes
    - Cantidad por estado
    - Tiempo promedio de resolución (creada → resuelta)
    - Solicitudes sin asignar
    """
    total = col.count_documents({})

    # Conteo por estado
    pipeline_estados = [
        {"$group": {"_id": "$estado", "cantidad": {"$sum": 1}}}
    ]
    por_estado = {doc["_id"]: doc["cantidad"] for doc in col.aggregate(pipeline_estados)}

    # Tiempo promedio de resolución (ms → horas)
    pipeline_resolucion = [
        {"$match": {"estado": {"$in": ["resuelta", "cerrada"]}}},
        {
            "$project": {
                "duracion_ms": {
                    "$subtract": ["$fecha_actualizacion", "$fecha_creacion"]
                }
            }
        },
        {"$group": {"_id": None, "promedio_ms": {"$avg": "$duracion_ms"}}},
    ]
    resolucion_result = list(col.aggregate(pipeline_resolucion))
    promedio_horas = None
    if resolucion_result and resolucion_result[0].get("promedio_ms") is not None:
        promedio_horas = round(resolucion_result[0]["promedio_ms"] / 3_600_000, 2)

    # Sin asignar
    sin_asignar = col.count_documents({"asignado_id": None})

    informe = {
        "generado_en": datetime.now(timezone.utc).isoformat(),
        "total_solicitudes": total,
        "por_estado": por_estado,
        "tiempo_promedio_resolucion_horas": promedio_horas,
        "sin_asignar": sin_asignar,
    }
    logger.info(f"Informe generado: {total} solicitudes totales.")
    return informe
