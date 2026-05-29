"""
routers/auth.py
Endpoints de registro y autenticación de usuarios.
"""
from fastapi import APIRouter, Depends
from pymongo.collection import Collection

from app.core.database import get_db
from app.core.security import get_current_user
from app.models.usuario import LoginRequest, TokenResponse, UsuarioCreate, UsuarioResponse
from app.services import usuario_service

router = APIRouter(prefix="/api/auth", tags=["Autenticación"])


def get_usuarios_col() -> Collection:
    return get_db()["usuarios"]


@router.post("/registro", response_model=UsuarioResponse, status_code=201,
             summary="Registrar nuevo usuario")
def registrar(datos: UsuarioCreate, col: Collection = Depends(get_usuarios_col)):
    """
    Crea un nuevo usuario con rol: `usuario` | `soporte` | `administrador`.
    """
    return usuario_service.registrar_usuario(col, datos)


@router.post("/token", response_model=TokenResponse,
             summary="Obtener token JWT")
def login(datos: LoginRequest, col: Collection = Depends(get_usuarios_col)):
    """
    Autentica al usuario y retorna un token JWT Bearer.
    """
    return usuario_service.autenticar_usuario(col, datos.email, datos.password)


@router.get("/me", response_model=dict, summary="Datos del usuario autenticado")
def me(current_user: dict = Depends(get_current_user)):
    """Retorna la información del usuario autenticado desde el token."""
    return current_user
