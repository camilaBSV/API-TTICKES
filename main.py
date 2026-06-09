"""Punto de entrada mínimo de la API."""

from fastapi import FastAPI

app = FastAPI(
    title="API mínima",
    version="0.1.0",
    description="Versión simplificada para ejecutar la API con lo mínimo necesario.",
)


@app.get("/")
def read_root():
    return {"message": "API mínima funcionando"}


@app.get("/health")
def health_check():
    return {"status": "ok"}
