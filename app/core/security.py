"""
core/security.py
JWT, hashing de contraseñas y dependencias de control de acceso por roles.
Roles válidos: usuario | soporte | administrador
"""
import logging
from datetime import datetime, timedelta, timezone
from typing import Optional

from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError, jwt
from passlib.context import CryptContext

from app.core.config import settings

logger = logging.getLogger(__name__)

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/api/auth/token")

ROLES = {"usuario", "soporte", "administrador"}


# ── Contraseñas ──────────────────────────────────────────────────────────────

def hash_password(password: str) -> str:
    return pwd_context.hash(password)


def verify_password(plain: str, hashed: str) -> bool:
    return pwd_context.verify(plain, hashed)


# ── JWT ───────────────────────────────────────────────────────────────────────

def create_access_token(data: dict, expires_delta: Optional[timedelta] = None) -> str:
    to_encode = data.copy()
    expire = datetime.now(timezone.utc) + (
        expires_delta or timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    )
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, settings.SECRET_KEY, algorithm=settings.ALGORITHM)


def decode_token(token: str) -> dict:
    try:
        return jwt.decode(token, settings.SECRET_KEY, algorithms=[settings.ALGORITHM])
    except JWTError as e:
        logger.warning(f"Token inválido: {e}")
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Token inválido o expirado.",
            headers={"WWW-Authenticate": "Bearer"},
        )


# ── Dependencias de usuario actual ───────────────────────────────────────────

def get_current_user(token: str = Depends(oauth2_scheme)) -> dict:
    payload = decode_token(token)
    usuario_id: str = payload.get("sub")
    rol: str = payload.get("rol")
    if not usuario_id or rol not in ROLES:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Credenciales inválidas.")
    return {"usuario_id": usuario_id, "rol": rol, "nombre": payload.get("nombre", "")}


def require_role(*roles: str):
    """Dependencia que restringe el acceso a uno o más roles."""
    def checker(current_user: dict = Depends(get_current_user)) -> dict:
        if current_user["rol"] not in roles:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail=f"Acción no permitida para el rol '{current_user['rol']}'.",
            )
        return current_user
    return checker
