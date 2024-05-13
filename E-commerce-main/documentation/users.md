# Gestión de Usuarios

## Descripción

Sistema CRUD para la gestión de usuarios en la plataforma de e-commerce.

## Tecnologías

Lenguaje: `Python`

Framework: `Flask`

### Librerías

- `Flask`
- `SQLAlchemy`

### Documentación

[Documentación de Flask](https://flask.palletsprojects.com/en/3.0.x/quickstart/#routing)

[Documentación de SQLAlchemy](https://docs.sqlalchemy.org/en/latest/)

## Variables de Entorno

- `DB_URI`: URL de la base de datos.
- `PORT`: Puerto de la aplicación.
- `HOST`: Host de la aplicación.
- `DEBUG`: Modo de depuración.

## Endpoints

Endpoint base: `/api/v1`

| Endpoint        | Descripción                                | Método |
| --------------- | ------------------------------------------ | ------ |
| `/users/{page}` | Obtener la lista de todos los usuarios.    | GET    |
| `/users`        | Crear un nuevo usuario.                    | POST   |
| `/users/{id}`   | Obtener detalles de un usuario específico. | GET    |
| `/users/{id}`   | Actualizar detalles de un usuario.         | PUT    |
| `/users/{id}`   | Eliminar un usuario.                       | DELETE |
| `/roles/{page}` | Obtener la lista de todos los roles.       | GET    |
| `/roles`        | Crear un nuevo rol.                        | POST   |
| `/roles/{id}`   | Obtener detalles de un rol.                | GET    |
| `/roles/{id}`   | Actualizar detalles de un rol.             | PUT    |
| `/roles/{id}`   | Eliminar un rol.                           | DELETE |
