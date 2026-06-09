"""Punto de entrada principal de la API."""

from fastapi import FastAPI

from app.routers import auth, informe, solicitudes

app = FastAPI(
    title="API de gestión de solicitudes de soporte técnico",
    version="0.1.0",
    description="API para gestionar solicitudes, autenticación y reportes de soporte.",
)

app.include_router(auth.router, tags=["auth"])
app.include_router(solicitudes.router, tags=["solicitudes"])
app.include_router(informe.router, tags=["informe"])


@app.get("/")
def read_root():
    return {"message": "API funcionando"}


@app.get("/health")
def health_check():
    return {"status": "ok"}
