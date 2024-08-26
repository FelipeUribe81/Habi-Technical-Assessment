# Prueba Técnica - Habi

## Descripción del Proyecto

Este proyecto tiene como finalidad desarrollar dos microservicios: uno funcional para la consulta de inmuebles 
disponibles y vendidos, y otro conceptual para gestionar los "me gusta" de los usuarios en los inmuebles. 
El objetivo es crear una herramienta robusta y escalable que permita a los usuarios de Habi buscar inmuebles 
aplicando diferentes filtros y registrar sus preferencias a través de 
un sistema de favoritos.


## Tecnologías Utilizadas

- **Lenguaje de Programación:** Python 3.12.2
- **Base de Datos:** MySQL
- **Gestión de Dependencias:** `pip`
- **Conección con la Base de Datos** `mysql-connector-python`
- **Gestión de variables de entorno** `python-dotenv`
- **Pruebas Unitarias:** `unittest`
- **Control de Versiones:** Git & GitHub
- **Entorno de Desarrollo:** PyCharm

## Enfoque de Desarrollo

### Servicio de Consulta

1. **Análisis y Diseño:**
   - Los usuarios únicamente pueden consultar inmuebles con los estados: `pre_venta`, `en_venta`, y `vendido`.
   - Diseñar una consulta SQL eficiente que recupere los inmuebles según los filtros aplicados.
   - Implementar filtros por año de construcción, ciudad, y estado.
   - Construir un microservicio que pueda ser consumido por una arquitectura REST.
   - Crear un archivo JSON que simule los datos que se esperan recibir desde el front-end con los filtros aplicados por los usuarios.

2. **Implementación:**
   - Implementación de la query: 
     1. Extraer el estado más reciente.
     2. Identificar el nombre del estado cruzando 'status_history' con 'status'.
     3. Obtener los datos que se muestran al usuario cruzando con la tabla de propiedades.
     4. Descartar los estados invalidos.
     5. Eliminar los datos inconcistentes.
     6. Implementar filtros por año de construcción, ciudad, y estado.
   - Desarrollar la lógica backend para manejar las consultas y los filtros. Para asemejar el comportamiento de un
   microservicio, se establecera un controlador para capturar excepciones en la estructura de los datos y ejecutar 
   el servicio dependiendo de la demanda solicitada. Ej: (**_Obtener Inmuebles_**)
   - Los datos que vienen del front serán similares a lo que recibe el parametro _**'event'**_ del 
   las funciones **_'lambda'_** de AWS (**[Event parameter](https://aws-lambda-for-python-developers.readthedocs.io/en/latest/02_event_and_context/)**)

3. **Pruebas:**
   - Implementar pruebas unitarias para garantizar que las consultas y filtros funcionen correctamente.

### Servicio de "Me gusta"

1. **Diseño Conceptual:**
   - Diseñar un diagrama de Entidad-Relación (ERD) para extender el modelo de la base de datos y soportar la funcionalidad de "me gusta".
   - El diagrama debe reflejar cómo se almacenarán los "me gusta" y cómo se relacionan con los usuarios y los inmuebles.

2. **Implementación SQL:**
   - Escribir el código SQL necesario para extender el modelo de la base de datos con las tablas y relaciones requeridas.

### Pruebas y Documentación

- **Pruebas Unitarias:** 
   - Asegurarse de que cada funcionalidad esté cubierta por pruebas unitarias, validando los resultados esperados y manejando errores.

- **Documentación:** 
   - Documentar detalladamente el código, el diagrama ERD y las decisiones de diseño tomadas durante el desarrollo.
