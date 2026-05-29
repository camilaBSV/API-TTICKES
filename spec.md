SPEC TECNICA - API "TTICKES"
1	Apartado de negocio (visión Product Owner)
1.1	Problemática
•	Contexto
Actualmente, el área de soporte técnico gestiona las solicitudes de los usuarios a través de múltiples canales y sin un flujo estandarizado. Esta situación genera un desorden en la recepción, priorización y seguimiento de los requerimientos, dificultando la visibilidad del estado de cada solicitud y la coordinación entre los equipos responsables. La ausencia de un sistema centralizado y de procesos claros impacta directamente en la eficiencia operativa del soporte técnico.
•	Dolor del Usuario
Desde la perspectiva del usuario final, el principal dolor es la falta de claridad y seguimiento de sus solicitudes. Los usuarios no saben si su requerimiento fue recibido, en qué estado se encuentra ni cuándo será resuelto. Esto ocasiona incertidumbre, repetición de solicitudes, aumento de reclamos y una percepción negativa del servicio de soporte, afectando la confianza en el área y en la organización.
•	Impacto en el Negocio
El desorden en la gestión de solicitudes de soporte técnico tiene un impacto directo en el negocio:
•	Aumento en los tiempos de respuesta y resolución.
•	Uso ineficiente de los recursos del equipo de soporte.
•	Mayor carga operativa debido a retrabajos y solicitudes duplicadas.
•	Disminución en la satisfacción del usuario interno o externo, lo que puede afectar la productividad general y la imagen de la organización.
En el mediano y largo plazo, esta problemática limita la capacidad del área para escalar, medir desempeño y mejorar continuamente el servicio.
•	Oportunidad
Existe una oportunidad clara para implementar una solución estructurada y centralizada de gestión de solicitudes de soporte técnico, que permita ordenar el flujo de requerimientos, priorizarlos correctamente y asegurar su seguimiento de principio a fin. Desde la perspectiva del Product Owner, esta mejora habilita la entrega de valor al usuario mediante un servicio más transparente, eficiente y confiable, al mismo tiempo que proporciona al negocio métricas claras para la toma de decisiones y la optimización del servicio.
1.2	Solución Propuesta
•	Descripción funcional de la API de Gestión de Soporte Técnico
•	Visión General
Se propone el desarrollo e implementación de una API de gestión de solicitudes de soporte técnico, cuyo objetivo es centralizar, ordenar y dar seguimiento completo a los requerimientos de los usuarios. Esta API actuará como el núcleo del sistema, permitiendo la integración con distintas plataformas (portales web, aplicaciones internas o sistemas de mensajería), asegurando un flujo de trabajo estructurado y trazable desde la creación de la solicitud hasta su resolución.
•	¿Qué hace la API?
La API permite:
•	Registrar y almacenar solicitudes de soporte técnico de manera estandarizada.
•	Asignar, priorizar y categorizar los requerimientos según su tipo, urgencia y estado.
•	Gestionar el ciclo de vida de cada solicitud (creada, en revisión, en proceso, resuelta, cerrada).
•	Facilitar el seguimiento en tiempo real del estado de las solicitudes.
•	Generar métricas y reportes sobre tiempos de respuesta, resolución y carga de trabajo.
•	Mantener un historial claro y auditable de todas las interacciones relacionadas a cada caso.
•	¿Para quién está diseñada?
La API está orientada a dos tipos principales de usuarios:
•	Usuarios finales (internos o externos): quienes generan las solicitudes de soporte y requieren visibilidad, transparencia y confirmación del estado de sus requerimientos.
•	Equipo de soporte técnico y gestión: encargados de recibir, priorizar, atender y cerrar las solicitudes, así como de analizar el desempeño del servicio y tomar decisiones basadas en datos.
Desde la perspectiva del Product Owner, la API actúa como un habilitador clave para mejorar tanto la experiencia del usuario como la eficiencia operativa del equipo.
•	¿Qué problema resuelve?
Esta solución aborda directamente los principales dolores identificados:
•	Elimina el desorden causado por solicitudes dispersas en distintos canales.
•	Evita la pérdida de requerimientos y la duplicación de esfuerzos.
•	Proporciona visibilidad y control sobre el estado de cada solicitud.
•	Reduce los tiempos de respuesta y mejora la coordinación del equipo de soporte.
•	Aumenta la satisfacción del usuario al ofrecer un proceso claro y confiable.
•	Valor para el Negocio
La implementación de esta API representa una mejora significativa en la gestión del soporte técnico, permitiendo escalar el servicio, estandarizar procesos y generar información confiable para la mejora continua. Desde el punto de vista del negocio, la solución contribuye a optimizar recursos, mejorar la calidad del servicio y fortalecer la percepción del área de soporte como un habilitador estratégico.
1.3	Alcance del Proyecto
•	 ¿Qué entra en el alcance?
El proyecto contempla el diseño y desarrollo de una API de gestión de solicitudes de soporte técnico, cuyo alcance funcional incluye:
•	Registro centralizado de solicitudes de soporte técnico.
•	Gestión del ciclo de vida de las solicitudes (creación, asignación, seguimiento, cierre).
•	Clasificación y priorización de requerimientos según criterios predefinidos.
•	Consulta del estado de las solicitudes por parte de usuarios y equipo de soporte.
•	Generación de registros históricos y métricas básicas (tiempos de respuesta, volumen de solicitudes).
•	Integración de la API con aplicaciones internas o interfaces clientes previamente definidas.
El enfoque principal está en ordenar, centralizar y dar trazabilidad a las solicitudes, garantizando un proceso estandarizado.
•	 ¿Qué no entra en el alcance?
Quedan explícitamente fuera del alcance del proyecto:
•	Desarrollo de interfaces gráficas complejas (frontend) más allá de prototipos o integraciones básicas.
•	Automatización avanzada basada en inteligencia artificial o machine learning.
•	Gestión de infraestructura, hardware o redes físicas.
•	Atención directa de los casos por parte del equipo de soporte (la API solo gestiona información).
•	Integraciones con sistemas externos no definidos o no disponibles durante el proyecto.
Estas exclusiones permiten mantener el enfoque del proyecto en la gestión y seguimiento de solicitudes, evitando la ampliación innecesaria del alcance.
•	Supuestos
Para la correcta ejecución del proyecto se consideran los siguientes supuestos:
•	Los usuarios y el equipo de soporte contarán con acceso a los sistemas que consuman la API.
•	Los procesos básicos de soporte técnico existen y pueden ser estandarizados.
•	La organización dispone de los recursos técnicos mínimos para alojar y mantener la API.
•	Los stakeholders clave participarán en la definición de requisitos y validación de la solución.
Estos supuestos son necesarios para asegurar la viabilidad y el éxito del proyecto.
•	Restricciones
El proyecto está condicionado por las siguientes restricciones:
•	Tiempo limitado para el diseño e implementación de la solución.
•	Recursos técnicos y humanos acotados.
•	Cumplimiento de políticas internas de seguridad y privacidad de la información.
•	Dependencia de tecnologías y entornos previamente definidos por la organización.
Estas restricciones influyen en la priorización de funcionalidades y en el alcance final de la solución.
•	Stakeholders
Los principales interesados (stakeholders) del proyecto son:
•	Usuarios finales: responsables de generar solicitudes y consumir el servicio de soporte.
•	Equipo de soporte técnico: usuarios clave de la API para la gestión y seguimiento de los requerimientos.
•	Product Owner: responsable de maximizar el valor del producto y priorizar funcionalidades.
•	Área de TI / Desarrollo: encargada del diseño, desarrollo y mantenimiento de la API.
•	Gestión o liderazgo: interesados en métricas, desempeño y mejora continua del servicio.
La correcta identificación y coordinación entre stakeholders es fundamental para asegurar que la solución entregue valor real al negocio.
1.4	Metodología MoSCoW – Priorización de Requisitos
La metodología MoSCoW se utiliza para priorizar los requisitos del proyecto en función de su valor para el negocio y su impacto en la solución. Esta priorización permite definir claramente el Producto Mínimo Viable (MVP) y gestionar expectativas de los stakeholders.
•	Must Have (Imprescindibles – MVP)
Estos requisitos son críticos para el éxito del proyecto. El MVP se construye exclusivamente con los ítems de esta categoría.
Requisito	Descripción	Justificación
Registro de solicitudes	Permite crear solicitudes de soporte técnico de forma estandarizada	Sin este componente no existe el sistema; es la base del producto
Gestión de estados	Control del ciclo de vida de la solicitud (creada, en proceso, resuelta, cerrada)	Garantiza seguimiento y trazabilidad, resolviendo el principal problema identificado
Asignación de solicitudes	Permite asignar tickets a responsables del soporte	Evita pérdida de solicitudes y mejora la organización del trabajo
Consulta de estado	Usuarios y soporte pueden visualizar el estado de cada solicitud	Reduce incertidumbre y reclamos de los usuarios
Almacenamiento centralizado	Base de datos única para todas las solicitudes	Elimina el desorden y la dispersión de información
Seguridad básica	Control de acceso por roles (usuario / soporte / administrador)	Protege la información y asegura uso correcto de la API
✅ Resultado: Con estos elementos se resuelve el problema principal de desorden y falta de seguimiento, entregando valor inmediato.


•	Should Have (Importantes – No críticos para el MVP)
Requisito	Descripción	Justificación
Priorización por urgencia	Clasificación de solicitudes según impacto o criticidad	Mejora la eficiencia, pero el sistema puede operar sin ello inicialmente
Notificaciones básicas	Avisos de cambios de estado (correo o sistema)	Aumenta la experiencia del usuario, pero no es esencial en la primera versión
Búsqueda y filtros	Filtros por estado, fecha o tipo de solicitud	Facilita la gestión diaria, pero no bloquea el funcionamiento
Comentarios en solicitudes	Registro de intercambio entre soporte y usuario	Mejora la comunicación, pero puede resolverse externamente en el MVP
Se consideran para una segunda iteración una vez validado el MVP.
•	Could Have (Deseables – Bajo impacto inicial)
Requisito	Descripción	Justificación
Dashboard de métricas	Visualización gráfica de indicadores de soporte	Aporta valor analítico, pero no influye directamente en la operación básica
Etiquetas personalizadas	Tags configurables para clasificación adicional	Mejora la flexibilidad, pero no es prioritaria
Integración con otros sistemas	Conexión con herramientas externas (correo, chat, ERP)	Requiere mayor esfuerzo técnico y no es esencial en etapas iniciales
Historial avanzado	Detalle extendido de cambios y acciones	Útil para auditorías futuras, no crítico para el MVP
Se implementan solo si hay tiempo y recursos adicionales.
•	Won’t Have (Fuera de Alcance – Por ahora)
Requisito	Descripción	Justificación
Automatización con IA	Respuesta automática o clasificación inteligente	Incrementa complejidad y riesgo, fuera del objetivo del proyecto
Aplicación móvil nativa	App dedicada para usuarios	La API puede ser consumida sin necesidad de app propia
Gestión de infraestructura	Administración de hardware o redes	No corresponde al objetivo de la API
Atención directa del soporte	Resolución técnica de incidentes	La API gestiona información, no ejecuta soporte técnico
🚫 Estos elementos se excluyen para mantener el enfoque y evitar el crecimiento descontrolado del alcance.
•	Relación MoSCoW y MVP
El Producto Mínimo Viable (MVP) se compone únicamente de los requisitos clasificados como Must Have, ya que:
•	Resuelven el problema central del desorden y seguimiento de solicitudes
•	Permiten validar la solución con usuarios reales
•	Entregan valor inmediato al negocio
•	Sientan la base para futuras iteraciones
2	 Apartado técnico
2.1	Stack Tecnológico — MVP vs Producto Final (Solo Python)

La elección del stack tecnológico se plantea de forma progresiva, diferenciando entre el Producto Mínimo Viable (MVP) y el Producto Final, con el objetivo de equilibrar rapidez de desarrollo, control de costos y madurez técnica a medida que el producto evoluciona.

2.1.1	 Justificación técnica del MVP
Stack Tecnológico del MVP
Lenguaje: Python
Framework: FastAPI

•	Rendimiento
FastAPI está construido sobre el estándar ASGI y aprovecha librerías como Starlette y Uvicorn, lo que le permite manejar alta concurrencia con baja latencia. Para una API de soporte técnico —centrada en operaciones I/O como creación, consulta y actualización de solicitudes— ofrece un rendimiento excelente sin complejidad adicional.

•	Drivers de MongoDB
Python dispone del driver oficial PyMongo, ampliamente probado y estable, que se integra de forma directa con FastAPI. Esta combinación permite trabajar fácilmente con datos documentales, ideales para un MVP donde los modelos pueden cambiar rápidamente sin afectar el sistema.

•	Ecosistema
FastAPI se beneficia del amplio ecosistema de Python, incluyendo librerías para validación de datos, autentificación básica, serialización y manejo de errores. Además, la documentación automática (Swagger/OpenAPI) reduce el esfuerzo de mantenimiento y facilita el consumo de la API.

•	Observabilidad
El MVP requiere Observabilidad básica: logging, control de errores y métricas simples. FastAPI permite integrar fácilmente estas capacidades sin necesidad de herramientas complejas, lo que es adecuado para una etapa temprana del producto.

•	Costos
Todo el stack es open source, sin costos de licenciamiento. FastAPI es ligero y puede desplegarse en infraestructuras de bajo costo, lo que reduce la inversión inicial necesaria para validar la solución.

•	Comunidad
FastAPI cuenta con una comunidad activa y en crecimiento dentro del ecosistema Python, con abundante documentación, ejemplos y soporte, lo que reduce riesgos durante el desarrollo del MVP.
Madurez adecuada para MVP
Aunque es un framework relativamente moderno, FastAPI ha demostrado estabilidad y confiabilidad en proyectos reales, siendo especialmente adecuado para MVPs por su simplicidad y enfoque en productividad.
✅ Conclusión MVP
Python + FastAPI permiten construir rápidamente una API funcional, eficiente y económica, enfocada en validar la solución al problema de desorden y falta de seguimiento en soporte técnico.

2.1.2	Justificación técnica del Producto Final
Stack Tecnológico del Producto Final
Lenguaje: Python
Framework: Django + Django REST Framework (DRF)

•	Arquitectura y madurez
Django es uno de los frameworks más maduros del ecosistema Python. Su arquitectura estructurada favorece la mantenibilidad, escalabilidad y el trabajo colaborativo, aspectos críticos para un producto en producción y de largo plazo.

•	Rendimiento
Si bien Django no es tan liviano como FastAPI, ofrece un rendimiento estable y predecible cuando se implementa correctamente. Para un sistema de soporte técnico con mayor volumen de usuarios y datos, su robustez es una ventaja frente a soluciones más livianas.

•	Drivers de MongoDB
Django puede integrarse con MongoDB mediante PyMongo o capas intermedias como MongoEngine, permitiendo mantener el enfoque documental sin perder la organización del framework. Esto resulta adecuado para sistemas que requieren trazabilidad y consistencia.

•	Ecosistema empresarial
Django cuenta con un ecosistema extremadamente amplio, que incluye soluciones maduras para seguridad, autenticación, autorización, auditoría y gestión de usuarios, todas necesarias en un producto final.

•	Observabilidad avanzada
El framework facilita la incorporación de logging estructurado, monitoreo, trazabilidad y métricas, permitiendo un control exhaustivo del comportamiento del sistema en producción.





•	Costos a largo plazo
Aunque el desarrollo inicial requiere mayor esfuerzo, Django reduce costos futuros de mantenimiento y retrabajo gracias a su enfoque en buenas prácticas y estructura sólida.

•	Comunidad y soporte
La comunidad de Django es una de las más grandes y estables del mundo Python, con documentación extensa y soporte continuo, lo que garantiza sostenibilidad a largo plazo.

✅ Conclusión Producto Final
Python + Django + DRF ofrecen una base sólida, segura y escalable, adecuada para un sistema de gestión de soporte técnico consolidado y en crecimiento.

2.1.3	Cuadro comparativo MVP vs Producto Final
Dimensión	MVP	Producto Final
Lenguaje	Python	Python
Framework	FastAPI	Django + DRF
Enfoque	Velocidad y validación	Robustez y escalabilidad
Rendimiento	Muy alto, liviano	Estable y predecible
MongoDB	PyMongo directo	PyMongo / MongoEngine
Observabilidad	Básica	Avanzada
Costos	Bajos	Moderados
Madurez requerida	Media	Alta



Enfoque evolutivo del stack

Mantener Python como lenguaje único permite:
•	Reutilizar conocimiento del equipo
•	Reducir riesgos técnicos
•	Evolucionar el sistema sin reescritura completa
•	Ajustar la complejidad tecnológica según la etapa del producto
Este enfoque garantiza coherencia entre las necesidades del negocio y las decisiones tecnológicas.


2.2	Infraestructura de Hosting

La infraestructura de hosting se define considerando la etapa del producto, los requerimientos de disponibilidad, el control de costos y la posible escalabilidad futura. Se diferencian las decisiones para la aplicación y para la base de datos MongoDB, ya que presentan necesidades distintas.

•	Hosting de la Aplicación
•	MVP — Contenedores en entorno cloud básico
Descripción
Para el MVP, la aplicación se despliega utilizando contenedores (Docker) en un proveedor de cloud público mediante servicios PaaS o servidores virtuales de bajo costo.
Justificación
•	Costos:
La infraestructura inicial es de bajo costo, ideal para validar el producto sin una inversión elevada. Los contenedores permiten optimizar el uso de recursos y evitar sobre aprovisionamiento.
•	SLA:
Para el MVP, un SLA básico es suficiente, ya que el foco principal es validar la funcionalidad y la adopción del sistema más que garantizar alta disponibilidad.
•	Ubicación:
El despliegue se realiza en una región cercana al público objetivo para reducir latencia y mejorar la experiencia del usuario. No se requieren múltiples regiones en esta etapa.
•	Escalabilidad:
Aunque limitada, la escalabilidad vertical (aumentar recursos del servidor) es suficiente para el volumen esperado en el MVP. El uso de contenedores facilita una futura transición a esquemas más complejos.

Conclusión 
El uso de contenedores en un entorno cloud simple permite flexibilidad, rapidez de despliegue y bajos costos, adecuados para una fase de validación.


•	Producto Final — Contenedores orquestados
Descripción
Para el producto final, la aplicación se ejecuta en contenedores orquestados mediante una plataforma de orquestación (por ejemplo, Kubernetes o servicios gestionados equivalentes).

Justificación
•	Costos:
Aunque el costo es mayor que en el MVP, se justifica por la mejora en disponibilidad, escalabilidad y tolerancia a fallos. Además, el escalado automático permite optimizar recursos según la demanda real.
•	SLA:
Se requiere un SLA elevado, asegurando alta disponibilidad y continuidad del servicio, acorde a un sistema de soporte técnico en producción.
•	Ubicación:
Posibilidad de desplegar en múltiples zonas o regiones para mejorar la redundancia y reducir riesgos ante caídas regionales.
•	Escalabilidad:
Escalabilidad horizontal automática, permitiendo incrementar o reducir instancias de la aplicación según la carga. Esto es clave para soportar crecimiento en usuarios y solicitudes.
✅ Conclusión Producto Final 
La orquestación de contenedores proporciona una infraestructura robusta, escalable y preparada para crecimiento sostenido y operación continua.

•	Hosting de MongoDB
•	MVP — MongoDB Atlas (servicio gestionado)
Descripción
Para el MVP, se utiliza MongoDB Atlas, una solución completamente gestionada en la nube.
Justificación
•	Costos:
MongoDB Atlas ofrece planes de bajo costo, ideales para cargas pequeñas y medianas. Evita costos operativos asociados a administración de bases de datos.
•	SLA:
Proporciona un SLA adecuado desde etapas tempranas, garantizando disponibilidad sin necesidad de configuración avanzada.
•	Ubicación:
Permite seleccionar la región donde se almacenan los datos, favoreciendo baja latencia y cumplimiento básico de normativas.
•	Escalabilidad:
Facilita el escalado vertical simple, permitiendo aumentar capacidad sin interrupciones significativas.
✅ Conclusión MVP 
MongoDB Atlas reduce el esfuerzo operativo, permitiendo al equipo enfocarse en el desarrollo del producto y no en la infraestructura.

•	Producto Final — MongoDB Atlas avanzado o Self-Hosted
Descripción
Para el producto final, se considera mantener MongoDB Atlas en un plan superior o migrar a una opción self-hosted según necesidades específicas del negocio.

Justificación
•	Costos:
Atlas en planes avanzados implica mayor costo, pero reduce significativamente el riesgo operativo. La opción self-hosted puede ser más económica a largo plazo, pero requiere mayores recursos técnicos.
•	SLA:
En el producto final se exige un SLA alto, con replicación, backups automáticos y alta disponibilidad. Atlas ofrece estas capacidades de forma nativa.
•	Ubicación:
Permite configuraciones multi-región o georredundantes, mejorando resiliencia y cumplimiento regulatorio si es necesario.
•	Escalabilidad:
Escalabilidad horizontal y vertical según el crecimiento del volumen de datos y transacciones, asegurando continuidad del servicio.

✅ Conclusión Producto Final (MongoDB)
MongoDB Atlas avanzado o self-hosted proporciona la robustez, disponibilidad y control necesarios para un sistema crítico en producción.
















•	Comparación Resumida de Infraestructura
Componente	MVP	Producto Final
Aplicación	Contenedores simples	Contenedores orquestados
Base de datos	MongoDB Atlas básico	Atlas avanzado / Self-hosted
Costos	Bajos	Moderados / Altos
SLA	Básico	Alto
Escalabilidad	Limitada	Horizontal y automática
Ubicación	Una región	Multi-región

•	Conclusión General
La infraestructura propuesta acompaña la evolución natural del producto, permitiendo validar rápidamente en el MVP con costos controlados y evolucionar hacia una arquitectura robusta, escalable y confiable en el producto final. Este enfoque reduce riesgos técnicos y financieros, alineando la inversión en infraestructura con el crecimiento real del negocio.


2.3	Modelo de Datos — MongoDB

El modelo de datos se diseña considerando la problemática principal del sistema: ordenar, centralizar y dar seguimiento a solicitudes de soporte técnico, asegurando flexibilidad, trazabilidad y buen rendimiento.
MongoDB es especialmente adecuado para este caso debido a su enfoque documental y su capacidad para manejar estructuras de datos variables.

•	Entidades Principales
Las entidades clave del sistema son:
•	Usuarios
•	Solicitudes (Tickets)
•	Comentarios / Historial
•	Asignaciones y estados
La Solicitud es la entidad central del modelo.















•	Diagrama Conceptual del Modelo
USUARIO
 └── _id
 └── nombre
 └── email
 └── rol

SOLICITUD
 └── _id
 └── titulo
 └── descripcion
 └── estado
 └── prioridad
 └── usuario_id (ref)
 └── asignado_id (ref)
 └── eventos[] (embebido)
 └── fecha_creacion
 └── fecha_actualizacion
Este diseño prioriza el acceso rápido a la información principal de cada solicitud, minimizando la cantidad de consultas necesarias.

•	Documento de Ejemplo — Usuario
JSON
{
"_id": "usr_123",
"nombre": "Camila Sepúlveda",
"email": "camila@empresa.cl",
"rol": "usuario",
"activo": true
}
Mostrar más líneas
•	Justificación
El documento de usuario se mantiene simple y referenciable, ya que la información del usuario puede ser compartida entre múltiples solicitudes.





















•	Documento de Ejemplo — Solicitud (Ticket)
JSON
{
"_id": "req_456",
"titulo": "Error en acceso al sistema",
"descripcion": "No es posible iniciar sesión desde esta mañana",
"estado": "en_proceso",
"prioridad": "alta",
"usuario_id": "usr_123",
"asignado_id": "usr_890",
"eventos": [
{
"tipo": "creacion",
"fecha": "2026-04-10T09:30:00Z",
"comentario": "Solicitud creada por el usuario"
},
{
"tipo": "asignacion",
"fecha": "2026-04-10T10:00:00Z",
"comentario": "Asignada a soporte nivel 1"
}
],
"fecha_creacion": "2026-04-10T09:30:00Z",
"fecha_actualizacion": "2026-04-10T10:00:00Z"
}
Mostrar más líneas

•	Patrones de Diseño Aplicados
a)	Attribute Pattern
Uso: Campos como estado, prioridad y rol se manejan como atributos simples.
Justificación técnica
Permite filtrar, ordenar y consultar solicitudes de forma eficiente usando índices.
Justificación de negocio
Facilita reportes rápidos (por estado, prioridad o tipo), apoyando la toma de decisiones.

b)	Bucket Pattern
Uso: El historial de eventos (eventos) se guarda como un arreglo embebido dentro de la solicitud.
Justificación técnica
Agrupar eventos relacionados evita múltiples consultas y reduce la complejidad del modelo. El crecimiento esperado del historial es controlado.
Justificación de negocio
Permite visualizar el seguimiento completo de una solicitud en una sola consulta, aumentando la transparencia del proceso.

c)	Extended Reference Pattern
Uso: Los campos usuario_id y asignado_id referencian a usuarios, sin duplicar toda su información.
Justificación técnica
Evita la duplicación de datos y mantiene consistencia entre documentos.
Justificación de negocio
Permite actualizar información del usuario sin afectar registros históricos, manteniendo integridad de datos.




•	Decisiones: Embebido vs Referenciado
Elemento	Decisión	Justificación
Usuario	Referenciado	Puede estar asociado a muchas solicitudes
Asignado	Referenciado	Evita duplicación y mantiene consistencia
Eventos / Historial	Embebido	Siempre se consulta junto con la solicitud
Estados	Atributo simple	Optimiza filtros y búsquedas

•	Índices Propuestos
Plain Text
- estado
- prioridad
- usuario_id
- asignado_id
- fecha_creacion
Mostrar más líneas
•	Justificación técnica
o	Mejoran el rendimiento de consultas frecuentes
o	Reducen tiempos de respuesta en listados y filtros
o	Facilitan paginación y ordenamiento
•	Justificación de negocio
o	Permiten obtener métricas rápidamente
o	Mejoran la experiencia de usuarios y del equipo de soporte
o	Soportan crecimiento del volumen de solicitudes

•	Beneficios del Modelo Propuesto
o	Técnicos
o	Alto rendimiento en consultas frecuentes
o	Flexibilidad para evolucionar el modelo
o	Menor complejidad en operaciones comunes de Negocio
o	Mayor visibilidad del estado de las solicitudes
o	Mejor seguimiento y trazabilidad
o	Base sólida para reportes y mejora continua del servicio

•	Conclusión
El modelo de datos en MongoDB está diseñado para resolver el desorden y la falta de seguimiento en el soporte técnico, equilibrando eficiencia técnica y valor de negocio. La combinación de documentos embebidos, referencias controladas y patrones reconocidos asegura un sistema escalable, mantenible y alineado con los objetivos del producto.















2.4	Consultas Necesarias — API de Soporte Técnico (MongoDB)
El diseño de consultas se basa en los casos de uso críticos del sistema, priorizando eficiencia, claridad y escalabilidad. Cada consulta está alineada con los endpoints de la API y soportada por índices definidos previamente para garantizar un rendimiento óptimo.

a)	Crear una solicitud de soporte
•	Endpoint
POST /api/solicitudes
•	Operación
Inserción de un nuevo documento en la colección solicitudes.
•	Filtros
No aplica (operación de escritura).
•	Índices utilizados
No aplica directamente, pero el documento queda preparado para consultas futuras indexadas.
•	Sintaxis MongoDB (mongosh / PyMongo)
JavaScript
db.solicitudes.insertOne({
titulo: "Error en acceso al sistema",
descripcion: "No es posible iniciar sesión",
estado: "creada",
prioridad: "alta",
usuario_id: "usr_123",
asignado_id: null,
eventos: [
{
tipo: "creacion",
fecha: new Date(),
comentario: "Solicitud creada por el usuario"
}
],
fecha_creacion: new Date(),
fecha_actualizacion: new Date()
});
Mostrar más líneas
•	Justificación
Permite registrar de forma centralizada todas las solicitudes, resolviendo el problema de dispersión inicial.

b)	Listar solicitudes por usuario
•	Endpoint
GET /api/solicitudes?usuario_id={id}
•	Operación
Lectura filtrada de documentos.
•	Filtro
•	usuario_id
•	Índice asociado
Plain Text
{ usuario_id: 1 }
Mostrar más líneas




•	Sintaxis MongoDB
JavaScript
db.solicitudes.find(
{ usuario_id: "usr_123" }
).sort({ fecha_creacion: -1 });
Mostrar más líneas
•	Justificación
Es una consulta frecuente del usuario final para revisar el estado de sus solicitudes.
El índice permite acceso rápido incluso con gran volumen de datos.

c)	Listar solicitudes asignadas a un agente de soporte
•	Endpoint
GET /api/solicitudes?asignado_id={id}
•	Operación
Lectura filtrada.
•	Filtro
•	asignado_id
•	Índice asociado
Plain Text
{ asignado_id: 1 }
Mostrar más líneas
•	Sintaxis MongoDB
JavaScript
db.solicitudes.find(
{ asignado_id: "usr_890" }
).sort({ prioridad: 1, fecha_creacion: 1 });
Mostrar más líneas
•	Justificación
Optimiza la operación diaria del equipo de soporte, priorizando trabajo y evitando solicitudes olvidadas.

d)	Consultar solicitudes por estado
•	Endpoint
GET /api/solicitudes?estado={estado}
•	Operación
Lectura con filtro simple.
•	Filtro
•	estado
•	Índice asociado
Plain Text
{ estado: 1 }
Mostrar más líneas
•	Sintaxis MongoDB
JavaScript
db.solicitudes.find(db estado: "en_proceso" }
);

•	Justificación
Es clave para el seguimiento global del servicio y generación de reportes operativos.






e)	Consultar solicitudes por prioridad
•	Endpoint
GET /api/solicitudes?prioridad={nivel}
•	Operación
Lectura clasificada.
•	Filtro
•	prioridad
•	Índice asociado
Plain Text
{ prioridad: 1 }
Mostrar más líneas
•	Sintaxis MongoDB
JavaScript
db.solicitudes.find(
{ prioridad: "alta" }
);
•	Justificación
Permite identificar incidentes críticos rápidamente, reduciendo impacto en el negocio.

f)	Obtener detalle completo de una solicitud
•	Endpoint
GET /api/solicitudes/{id}
•	Operación
Lectura por clave primaria.
•	Filtro
•	_id
•	Índice asociado
Plain Text
{ _id: 1 } (índice por defecto)
Mostrar más líneas
•	Sintaxis MongoDB
JavaScript
db.solicitudes.findOne(
{ _id: "req_456" }
);
•	Justificación
Devuelve toda la información necesario incluyendo historial embebido en una sola consulta.
________________________________________
•	7. Actualizar estado de una solicitud (seguimiento)
•	Endpoint
PATCH /api/solicitudes/{id}/estado
•	Operación
Actualización parcial + append de evento.
•	Filtro
•	_id
•	Índice asociado
Índice por defecto en _id.
•	Sintaxis MongoDB
JavaScript
db.solicitudes.updateOne(
{ _id: "req_456" },
{
$set: {
estado: "resuelta",
fecha_actualizacion: new Date()
},
$push: {
eventos: {
tipo: "cambio_estado",
fecha: new Date(),
comentario: "Solicitud resuelta por soporte"
}
}
}
);
Mostrar más líneas
•	Justificación
Soporta el seguimiento completo de la solicitud sin perder trazabilidad.
________________________________________
•	8. Buscar solicitudes por rango de fechas
•	Endpoint
GET /api/solicitudes?desde={fecha}&hasta={fecha}
•	Operación
Consulta por rango.
•	Filtro
•	fecha_creacion (operador $gte / $lte)
•	Índice asociado
Plain Text
{ fecha_creacion: 1 }
Mostrar más líneas
•	Sintaxis MongoDB
JavaScript
db.solicitudes.find({
fecha_creacion: {
$gte: ISODate("2026-04-01T00:00:00Z"),
$lte: ISODate("2026-04-30T23:59:59Z")
}
});
Mostrar más líneas
•	Justificación
Fundamental para métricas, auditorías y análisis de desempeño del soporte.
________________________________________
•	9. Consultas combinadas (estado + prioridad)
•	Endpoint
GET /api/solicitudes?estado={estado}&prioridad={prioridad}
•	Operación
Consulta compuesta.
•	Filtros
•	estado
•	prioridad
•	Índice recomendado
Plain Text
{ estado: 1, prioridad: 1 }
Mostrar más líneas
•	Sintaxis MongoDB
JavaScript
db.solicitudes.find({
estado: "en_proceso",
prioridad: "alta"
});
Mostrar más líneas
•	Justificación
Optimiza búsquedas operativas avanzadas sin degradar rendimiento.
________________________________________
•	Resumen de Consultas e Índices
Caso de uso	Filtro principal	Índice
Solicitudes por usuario	usuario_id	{ usuario_id: 1 }
Solicitudes asignadas	asignado_id	{ asignado_id: 1 }
Por estado	estado	{ estado: 1 }
Por prioridad	prioridad	{ prioridad: 1 }
Por fechas	fecha_creacion	{ fecha_creacion: 1 }
Consultas combinadas	estado + prioridad	{ estado: 1, prioridad: 1 }
•	Arquitectura de la API
La arquitectura de la API se diseña siguiendo principios de modularidad, observabilidad, escalabilidad y calidad, con el objetivo de soportar eficientemente la gestión y seguimiento de solicitudes de soporte técnico.
________________________________________
•	1. Visión General de la Arquitectura
La API se implementa como un servicio RESTful, desacoplado del frontend, y se comunica con MongoDB como sistema de persistencia. Se incorporan estándares modernos de observabilidad, documentación y pruebas desde el diseño inicial.
________________________________________
•	2. Diagrama de Arquitectura (Lógico)
[ Cliente / Frontend ]
          |
          v
   [ API REST - FastAPI ]
          |
  -----------------------
  |        |           |
[Auth]  [Servicios]  [Observabilidad]
          |
          v
     [ MongoDB ]
•	Componentes principales
•	Cliente: Aplicaciones web o internas que consumen la API.
•	API REST: Punto central de acceso a la lógica de negocio.
•	Servicios: Gestión de solicitudes, usuarios y seguimiento.
•	MongoDB: Persistencia de datos documentales.
•	Observabilidad: Trazas, métricas y logs distribuidos.
________________________________________
•	3. Endpoints REST y Contrato
La API sigue convenciones REST y utiliza formatos JSON.
•	Ejemplo de Endpoints Principales
•	Crear solicitud
POST /api/solicitudes
Request Body
JSON
{
"titulo": "Error en el sistema",
"descripcion": "No se puede acceder",
"prioridad": "alta"
}
Mostrar más líneas
Response
JSON
{
"id": "req_456",
"estado": "creada",
"fecha_creacion": "2026-04-27T14:30:00Z"
}
Mostrar más líneas
________________________________________
•	Obtener solicitudes por usuario
GET /api/solicitudes?usuario_id={id}
Response
JSON
[
{
"id": "req_456",
"titulo": "Error en el sistema",
"estado": "en_proceso"
}
]
Mostrar más líneas
________________________________________
•	Actualizar estado de solicitud
PATCH /api/solicitudes/{id}/estado
Request Body
JSON
{
"estado": "resuelta",
"comentario": "Incidente solucionado"
}
Mostrar más líneas
________________________________________
✅ Los contratos están versionados y validados mediante esquemas OpenAPI.
________________________________________
•	4. Documentación — Swagger / OpenAPI 3
La API se documenta automáticamente usando OpenAPI 3, generando:
•	Documentación interactiva (Swagger UI)
•	Especificación estándar para consumo de clientes
•	Contratos claros entre frontend y backend
Beneficios técnicos
•	Reduce errores de integración
•	Facilita pruebas manuales y automatizadas
•	Mejora la mantenibilidad
Beneficios de negocio
•	Acelera la adopción del sistema
•	Reduce tiempos de onboarding técnico
________________________________________
•	5. Observabilidad con OpenTelemetry
Se adopta OpenTelemetry como estándar de observabilidad, integrando:
•	5.1 Trazas (Tracing)
•	Seguimiento completo de cada request
•	Identificación de cuellos de botella
•	Correlación entre API y base de datos
•	5.2 Métricas
•	Número de solicitudes por endpoint
•	Latencia promedio
•	Tasa de errores (4xx / 5xx)
•	5.3 Logs
•	Logs estructurados
•	Identificadores de trazas incluidos
•	Diferenciación por nivel (info, warning, error)
•	Justificación
Dimensión	Justificación técnica	Valor de negocio
Trazas	Facilitan debugging distribuido	Menor tiempo de resolución
Métricas	Permiten monitorear rendimiento	Mejora SLA
Logs	Auditoría y análisis de errores	Soporte confiable
________________________________________
•	6. Estrategia de Tests y Cobertura
•	Tipo de pruebas
•	Pruebas unitarias: lógica de negocio
•	Pruebas de integración: endpoints y base de datos
•	Pruebas de contrato: validación de requests y responses
•	Herramienta
•	pytest + coverage.py
•	Objetivo de cobertura
Cobertura mínima requerida: ≥ 80%
•	Umbral de bloqueo en CI/CD
•	Si la cobertura cae por debajo del 80%: ✅ El pipeline falla
✅ No se permite merge ni despliegue
•	Justificación
Técnica
•	Garantiza estabilidad del sistema
•	Reduce regresiones
Negocio
•	Menos incidentes en producción
•	Mayor confianza en las entregas
________________________________________
•	7. Integración en CI/CD
En cada pipeline:
1.	Ejecutar pruebas automáticas
2.	Medir cobertura de código
3.	Validar contratos OpenAPI
4.	Verificar umbral mínimo
5.	Autorizar o bloquear despliegue
Esto asegura calidad continua y alineación con estándares profesionales.

