"""
main.py
Punto de entrada de la API de Gestión de Solicitudes de Soporte Técnico.
Stack: Python + FastAPI + PyMongo + MongoDB Atlas
"""
import logging
import contextlib

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.core.config import settings
from app.core.database import close_connection, get_client
from app.routers import auth, informe, solicitudes

# ── Logging estructurado ──────────────────────────────────────────────────────

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(name)s | %(message)s",
)
logger = logging.getLogger(__name__)


# ── Lifespan: conexión y cierre de MongoDB ────────────────────────────────────

@contextlib.asynccontextmanager
async def lifespan(app: FastAPI):
    logger.info("Iniciando API — conectando a MongoDB Atlas...")
    logger.info(f"Colección activa: {settings.COLECCION}")
    get_client()  # valida la conexión al arrancar
    yield
    logger.info("Cerrando conexión a MongoDB Atlas...")
    close_connection()


# ── Instancia FastAPI ─────────────────────────────────────────────────────────

app = FastAPI(
    title="API de Gestión de Soporte Técnico",
    description=(
        "API REST para centralizar, ordenar y dar seguimiento a solicitudes de soporte técnico. "
        "Desarrollada con **Python + FastAPI + MongoDB Atlas**.\n\n"
        f"Colección activa: `{settings.COLECCION}`"
    ),
    version="1.0.0",
    contact={"name": "Equipo de Desarrollo", "email": "dev@empresa.cl"},
    license_info={"name": "Interno"},
    lifespan=lifespan,
)

# ── CORS ──────────────────────────────────────────────────────────────────────

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ── Routers ───────────────────────────────────────────────────────────────────

app.include_router(auth.router)
app.include_router(solicitudes.router)
app.include_router(informe.router)


# ── Healthcheck ───────────────────────────────────────────────────────────────

@app.get("/health", tags=["Sistema"], summary="Estado de la API")
def health():
    return {
        "status": "ok",
        "coleccion": settings.COLECCION,
        "version": "1.0.0",
    }
