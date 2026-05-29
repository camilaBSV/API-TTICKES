# API de Gestión de Solicitudes de Soporte Técnico

API REST para centralizar, ordenar y dar seguimiento a solicitudes de soporte técnico.  
**Stack:** Python 3.11+ · FastAPI · PyMongo · MongoDB Atlas

---

## Variables de entorno (`.env`)

```env
DATABASE_URL=mongodb+srv://<usuario>:<password>@cluster0.xxxxx.mongodb.net/?appName=Cluster0
COLECCION=colecciontest0
SECRET_KEY=supersecretkey2026
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=60
```

> Nunca commitear el `.env` al repositorio.

---

## Instalación

```bash
# 1. Clonar y entrar al directorio
cd api_soporte

# 2. Crear entorno virtual
python -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate

# 3. Instalar dependencias
pip install -r requirements.txt

# 4. Ejecutar la API
uvicorn main:app --reload
```

La API estará disponible en: `http://localhost:8000`  
Documentación Swagger: `http://localhost:8000/docs`  
Documentación ReDoc: `http://localhost:8000/redoc`

---

## Endpoints principales

| Método | Ruta | Rol requerido | Descripción |
|--------|------|---------------|-------------|
| `POST` | `/api/auth/registro` | — | Registrar usuario |
| `POST` | `/api/auth/token` | — | Obtener JWT |
| `GET` | `/api/auth/me` | Cualquiera | Info del usuario actual |
| `POST` | `/api/solicitudes` | Cualquiera | Crear solicitud |
| `GET` | `/api/solicitudes` | Cualquiera | Listar solicitudes |
| `GET` | `/api/solicitudes/{id}` | Cualquiera | Ver solicitud |
| `PATCH` | `/api/solicitudes/{id}/estado` | soporte / admin | Cambiar estado |
| `PATCH` | `/api/solicitudes/{id}/asignar` | soporte / admin | Asignar responsable |
| `GET` | `/api/informe` | soporte / admin | Informe de métricas |
| `GET` | `/health` | — | Estado de la API |

---

## Roles

| Rol | Permisos |
|-----|----------|
| `usuario` | Crear y consultar sus propias solicitudes |
| `soporte` | Ver todas, cambiar estados, asignar, ver informe |
| `administrador` | Todo lo anterior + gestión completa |

---

## Flujo de estados

```
creada → en_revision → en_proceso → resuelta → cerrada
```

---

## Ejecutar tests

```bash
pytest --cov=app --cov-report=term-missing --cov-fail-under=80
```

Cobertura mínima requerida: **80%** (bloquea si no se cumple).

---

## Estructura del proyecto

```
api_soporte/
├── main.py                     # Punto de entrada FastAPI
├── .env                        # Variables de entorno (no commitear)
├── requirements.txt
├── pyproject.toml              # Configuración pytest + cobertura
├── app/
│   ├── core/
│   │   ├── config.py           # Carga de .env (DATABASE_URL, COLECCION)
│   │   ├── database.py         # Conexión MongoDB Atlas
│   │   └── security.py        # JWT + control de roles
│   ├── models/
│   │   ├── solicitud.py        # Schemas Pydantic de solicitudes
│   │   └── usuario.py          # Schemas de usuario y auth
│   ├── routers/
│   │   ├── auth.py             # /api/auth
│   │   ├── solicitudes.py      # /api/solicitudes
│   │   └── informe.py          # /api/informe
│   └── services/
│       ├── solicitud_service.py
│       ├── usuario_service.py
│       └── informe_service.py
└── tests/
    └── test_solicitudes.py     # Pruebas unitarias e integración
```

---

## Colección MongoDB (`colecciontest0`)

Documento de ejemplo:

```json
{
  "_id": "req_456",
  "titulo": "Error al iniciar sesión",
  "descripcion": "No puedo acceder desde esta mañana.",
  "estado": "en_proceso",
  "prioridad": "alta",
  "usuario_id": "usr_123",
  "asignado_id": "usr_890",
  "eventos": [
    { "estado": "creada", "fecha": "2026-05-01T10:00:00Z", "actor_id": "usr_123" },
    { "estado": "en_proceso", "fecha": "2026-05-01T11:00:00Z", "actor_id": "usr_890" }
  ],
  "fecha_creacion": "2026-05-01T10:00:00Z",
  "fecha_actualizacion": "2026-05-01T11:00:00Z"
}
```
