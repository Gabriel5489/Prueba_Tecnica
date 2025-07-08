# API para gestionar tareas basicas

Desarrollada con Django REST Framework
- Inicio de sesión con JWT (JSON Web Tokens).
- Registro de nuevos usuarios.
- Detalle del perfil de usuario (solo para el usuario autenticado).
- Listado de tareas (solo para el usuario autenticado).
- Creación de nuevas tareas.
- Actualización de tareas existentes.
- Eliminación de tareas.
- Filtro por estado (completed=true/false).


## Requisitos
- Python 3.8 o superior
- pip
- Entorno virtual 'virtualenv'

## Instalación
1. Clona el repositorio:

   ```bash
   git clone https://github.com/Gabriel5489/Prueba_Tecnica.git
   cd Prueba_Tecnica
2. Crea un entorno virtual y activalo:

   ```bash
   python -m virtualenv venv

3. Instala las dependencias:

   ```bash
   pip install -r requirements.txt

4. Realiza las migraciones:

   ```bash
   python manage.py makemigrations
   python manage.py migrate

5. Inicia el servidor:

   ```bash
   python manage.py runserver

# Documentación Swagger

Una vez que el servidor esté activo:
- Swagger UI: http://localhost:8000/api/docs/
- Esquema OpenAPI: http://localhost:8000/api/schema/

# Peticiones CURL
Ejemplos de peticiones para probar la API.

## Usuarios

- Registro de usuario:

   ```bash
   curl -X POST http://localhost:8000/api/registro
        -H "Content-Type: application/json" 
        -d '{"username":"nuevo", "email":"correo@ejemplo.com", "password":"claveSegura123"}'

- Inicio de sesión (con JWT), copiar Token access para autenticarse en los siguientes endpoints:

   ```bash
   curl -X POST http://localhost:8000/api/token/ 
        -H "Content-Type: application/json" 
        -d '{"username":"usuario", "password":"contraseña"}'

- Perfil de usuario:

   ```bash
   curl -H "Authorization: Bearer <access_token>" http://localhost:8000/api/perfil/

## Tareas

- Agregar Tareas

   ```bash
   curl -X POST http://localhost:8000/api/tareas/
        -H "Authorization: Bearer <access_token>"
        -H "Content-Type: application/json"
        -d '{"title":"Redactar README", "description":"Explicar paso a paso la funicionalidad de la API"}'

- Listar Tareas

   ```bash
   curl -H "Authorization: Bearer <access_token>" http://localhost:8000/api/tareas/

- Obtener una tarea

   ```bash
   curl -H "Authorization: Bearer <access_token>" http://localhost:8000/api/tareas/{id}/

- Actualizar Tarea

   ```bash
   curl -X PUT http://localhost:8000/api/tareas/{id}/
        -H "Authorization: Bearer <access_token>"
        -H "Content-Type: application/json"
        -d '{"title":"Redactar README", "description":"Explicar paso a paso la funicionalidad de la API", "completed"=true}'
- Eliminar Tarea

   ```bash
   curl -X DELETE http://localhost:8000/api/tareas/{id}/
        -H "Authorization: Bearer <access_token>"
- Obtener Tarea con filtro por estado

   ```bash
   curl -H "Authorization: Bearer <access_token>" http://localhost:8000/api/tareas/?completed=true
