# API de Envío de Correos con SendGrid

Esta API permite enviar correos electrónicos utilizando plantillas dinámicas de SendGrid, incluyendo correos de verificación, cambio de contraseña, confirmación de cuenta y confirmación de orden.

## Requisitos Previos

- Node.js (versión 14 o superior)
- Cuenta de SendGrid con una API Key
- Docker (opcional, para el uso de contenedores)

## Configuración Inicial

1. Clona este repositorio:
   ```bash
   git clone https://github.com/sistemas-distribuidos-ibero/email.git

## Instala las dependencias

npm install

## Crea un archivo .env en la raíz del proyecto con el contenido segun lo indica el archivo .env.example

# Endpoints

## POST /sendVerification

Descripción: Envía un código de verificación a un correo electrónico.

Cuerpo de la Solicitud (Formato JSON):
{
  "email": "usuario@example.com",
  "codigo": "123456",
  "index_url": "http://example.com/verify"
}

### Respuestas:

200 OK: El código de verificación se ha enviado con éxito.
500 Internal Server Error: Error al enviar el código de verificación.

## POST /sendPasswordChange

Descripción: Envía un enlace de cambio de contraseña a un correo electrónico.

Cuerpo de la Solicitud (Formato JSON):

{
  "email": "usuario@example.com",
  "nombreUsuario": "Nombre del Usuario",
  "link": "http://example.com/reset-password"
}

### Respuestas:

200 OK: El enlace de cambio de contraseña se ha enviado con éxito.
500 Internal Server Error: Error al enviar el enlace de cambio de contraseña.

## POST /sendAccountConfirmation

Descripción: Envía un correo electrónico para confirmar la creación de una cuenta.

Cuerpo de la Solicitud (Formato JSON):

{
  "email": "usuario@example.com",
  "nombreUsuario": "Nombre del Usuario",
  "index_url": "http://example.com/dashboard"
}

### Respuestas:

200 OK: El correo de confirmación se ha enviado con éxito.
500 Internal Server Error: Error al enviar el correo de confirmación.

## POST /sendOrderConfirmation

Descripción: Envía un correo de confirmación para una orden.

Cuerpo de la Solicitud (Formato JSON):

{
  "email": "usuario@example.com",
  "nombreUsuario": "Nombre del Usuario",
  "idOrden": "ORD12345",
  "index_url": "http://example.com/order-details"
}

### Respuestas:

200 OK: La confirmación de orden se ha enviado con éxito.
500 Internal Server Error: Error al enviar la confirmación de orden.
