"""
models/usuario.py
Esquemas Pydantic para usuarios y autenticación.
"""
from typing import Optional
from pydantic import BaseModel, EmailStr, Field


class UsuarioCreate(BaseModel):
    nombre: str = Field(..., min_length=2, max_length=100)
    email: EmailStr
    password: str = Field(..., min_length=6)
    rol: str = Field(default="usuario")

    model_config = {"json_schema_extra": {
        "example": {
            "nombre": "Camila Sepúlveda",
            "email": "camila@empresa.cl",
            "password": "segura123",
            "rol": "usuario"
        }
    }}


class UsuarioResponse(BaseModel):
    id: str
    nombre: str
    email: str
    rol: str
    activo: bool


class TokenResponse(BaseModel):
    access_token: str
    token_type: str = "bearer"


class LoginRequest(BaseModel):
    email: str
    password: str
