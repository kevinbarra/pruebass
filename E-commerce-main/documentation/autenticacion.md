# Authentication

Sistema de autenticación para los usuarios registrados en la aplicación de e-comerce

## Tecnologías

Lenguaje: `Python`

Framework: `Flask`

### Librerías

- `Flask` 
- `Flask_Login`
- `flask_sqlalchemy`
- `SQLAlchemy`
- `Werkzeug`

### Documentación y Video

[Documentación en hashing de Werkzeug](https://werkzeug.palletsprojects.com/en/3.0.x/utils/#module-werkzeug.security)

[Documentación de Flask_Login](https://flask-login.readthedocs.io/en/latest/)

[Documentación de Flask](https://flask.palletsprojects.com/en/3.0.x/quickstart/#routing)

## Variables de Entorno

- `DB_URI`: URL de la base de datos.
- `app-key`: lleve aplicación.

## Endpoints

Endpoint base: `/api/v1`

| Endpoint  | Descripción                            | Método |
| --------- | -------------------------------------- | ------ |
| `/login`  | Dar acceso a un usuario ya registrado. | POST   |
| `/logout` | Cerrar la sesión del usuario.          |        |

## Consideraciones adicionales

Si se utiliza la librería de `Werkzeug` para hashear los passwords de los usuarios es necesario usar la misma librería para revisar hashes.