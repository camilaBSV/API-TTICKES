# Plan del Proyecto

## Objetivo

Definir un plan de trabajo para implementar la API de gestión de solicitudes de soporte técnico, considerando un MVP de informe y una fase de levantamiento y testing.

## Variables de entorno del proyecto

- `DATABASE_URL`: cadena de conexión a la base de datos MongoDB.
- `COLECCION`: nombre de la colección donde se almacenan las solicitudes de soporte.

> Nota: El archivo `.env` del proyecto existe pero está vacío. Estas variables deben completarse antes de ejecutar la API.

## Fase 1: Levantamiento de requerimientos

1. Revisión del `spec.md` para validar alcance y priorización.
2. Confirmar con stakeholders:
   - Tipos de solicitudes de soporte.
   - Estados del flujo de trabajo (creada, en proceso, resuelta, cerrada).
   - Roles y permisos necesarios (usuario, soporte, administrador).
   - Campos obligatorios de cada solicitud.
3. Identificar datos adicionales:
   - Prioridad/urgencia.
   - Asignación de responsable.
   - Comentarios o historial básico.
4. Establecer criterios de aceptación para el MVP.
5. Documentar las necesidades de reporte básico que debe entregar el informe.

## Fase 2: Diseño técnico

1. Definir modelo de datos para la colección MongoDB:
   - Identificador único.
   - Usuario solicitante.
   - Descripción del problema.
   - Estado actual.
   - Prioridad.
   - Responsable asignado.
   - Fechas de creación, actualización y cierre.
2. Configurar carga de variables de entorno:
   - `DATABASE_URL` para la conexión de MongoDB.
   - `COLECCION` para la colección de solicitudes.
3. Seleccionar el stack del MVP basado en el `spec.md`:
   - Python + FastAPI.
   - PyMongo para acceso a MongoDB.
4. Diseñar los endpoints principales:
   - Crear solicitud.
   - Actualizar estado/asignación.
   - Consultar solicitud por id.
   - Listar solicitudes con filtros básicos.
   - Generar informe básico de métricas.

## Fase 3: Desarrollo del MVP

1. Implementar la conexión con MongoDB usando `DATABASE_URL`.
2. Usar `COLECCION` para almacenar y leer las solicitudes.
3. Desarrollar los endpoints Must Have del MVP:
   - Registro de solicitudes.
   - Gestión de estados.
   - Asignación de solicitudes.
   - Consulta de estado.
   - Almacenamiento centralizado.
4. Añadir seguridad básica con control de roles.
5. Implementar el informe MVP que entregue:
   - Volumen total de solicitudes.
   - Cantidad por estado.
   - Tiempo promedio de resolución.
   - Estado de solicitudes asignadas.
6. Documentar el uso de la API y los requerimientos de la `.env`.

## Fase 4: Testing

1. Preparar datos de prueba en la colección indicada por `COLECCION`.
2. Validar los escenarios principales:
   - Creación de solicitudes.
   - Actualización de estados.
   - Asignación de tickets.
   - Consulta de estado por usuario y soporte.
   - Generación del informe.
3. Realizar pruebas de integración con la base de datos usando `DATABASE_URL`.
4. Ejecutar pruebas de aceptación con stakeholders sobre los criterios definidos.
5. Registrar errores y ajustes necesarios para asegurar que el MVP cumple el objetivo.

## Entregables del MVP

- API funcionando con los endpoints básicos.
- Informe inicial con métricas de solicitudes.
- Documentación de variables de entorno: `DATABASE_URL`, `COLECCION`.
- Plan de pruebas y resultados de validación.

## Cronograma sugerido

- Semana 1: Levantamiento de requerimientos y diseño técnico.
- Semana 2: Desarrollo del MVP.
- Semana 3: Testing y refinamiento.
- Semana 4: Revisión final y entrega.

## Consideraciones finales

- Mantener el MVP enfocado en los `Must Have` del `spec.md`.
- Dejar fuera del MVP los elementos de mayor complejidad identificados en `Won’t Have`.
- Asegurar que la base de datos se conecte correctamente con `DATABASE_URL` y que la colección utilizada sea la de `COLECCION`.
