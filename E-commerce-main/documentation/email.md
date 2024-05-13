# API Productos

## Descripción

API para la gestión de Emails mandados al usuario al hacer una compra

## Tecnologías

Lenguaje: `Python`

Framework: `Flask`

### Librerías

- `sendgrid`
- `os`
- `curl`

### Documentación y Video

[Repositorio GitHub de Sendgrid con ejemplos](https://github.com/sendgrid/sendgrid-python)

[Documentación de Sendgrid](https://docs.sendgrid.com/for-developers/sending-email/api-getting-started?_gl=1*wdt58u*_ga*MTc4MjU1MzQ2MC4xNzE0NTE4NDcz*_ga_8W5LR442LD*MTcxNDUxODQ3Mi4xLjEuMTcxNDUxODUyNC4wLjAuMA..)

[Documentación de Curl](https://curl.se/docs/)

[Video Corto](https://www.youtube.com/watch?v=qFDgH6dHRA4)

[Video Corto](https://www.youtube.com/watch?v=YqR4kfyO6hc)


## Endpoints

Endpoint base: `/api/v1`

| Endpoint                          | Descripción                                    | Método |
| --------------------------------- | ---------------------------------------------- | ------ |
| `/verify-email/{id_user}`         | Envía correo de validación de correo           | GET    |
| `/reset-password/{id_user}`       | Envía un enlace para restablecer la contraseña | GET    |
| `/purchase/{id_user}/{id_order}`  | Envía correo de confirmación de compra         | GET    |
| `/delivered/{id_user}/{id_order}` | Envía correo de confirmación de entrega        | GET    |



## Variables de Entorno

- `SENDGRID_KEY`: Llave de la API sendgrid

## Consideraciones adicionales

Hay que asegurarse de tener la llave de la API correcta o crear una nueva con una nueva cuenta Sendgrid, Es importante tambien trener instalado en la maquina en donde se vayan a hacer las pruebas el software Curl
