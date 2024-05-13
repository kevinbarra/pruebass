// Importar librerías necesarias
const express = require('express');
const bodyParser = require('body-parser');
const sgMail = require('@sendgrid/mail');

// Cargar variables de entorno
require('dotenv').config();

// Configurar la clave API de SendGrid
sgMail.setApiKey(process.env.SENDGRID_API_KEY);

// Configuración del servidor Express
const app = express();
const port = process.env.SENDGRID_PORT || 3888;
app.use(bodyParser.json()); // Para parsing de application/json

// Definir el sender
const sender = '180522@iberopuebla.mx';

// Endpoint para enviar código de verificación
app.post('/sendVerification', (req, res) => {
  const { email, codigo, index_url } = req.body;
  const msg = {
    to: email,
    from: sender,
    templateId: 'd-7af7ec957cc648f5a3af2ffa73fcccbf',
    dynamicTemplateData: {
      codigo_verificacion: codigo,
      url: index_url
    }
  };

  sgMail
    .send(msg)
    .then(() => res.status(200).send({message: 'Código de verificación enviado'}))
    .catch(error => res.status(500).send(error.toString()));
});

// Endpoint para enviar link de cambio de contraseña
app.post('/sendPasswordChange', (req, res) => {
  const { email, nombreUsuario, link } = req.body;
  const msg = {
    to: email,
    from: sender,
    templateId: 'd-78f6e56f07064a48b15a0a53700c6f71',
    dynamicTemplateData: {
      nombre_usuario: nombreUsuario,
      url: link
    }
  };

  sgMail
    .send(msg)
    .then(() => res.status(200).send({message: 'Email para cambio de contraseña enviado'}))
    .catch(error => res.status(500).send(error.toString()));
});

// Endpoint para enviar confirmación de creación de cuenta
app.post('/sendAccountConfirmation', (req, res) => {
  const { email, nombreUsuario, index_url } = req.body;
  const msg = {
    to: email,
    from: sender,
    templateId: 'd-d4e094e625874b6abcae49ae342b4f4b',
    dynamicTemplateData: {
      nombre_usuario: nombreUsuario,
      url: index_url
    }
  };

  sgMail
    .send(msg)
    .then(() => res.status(200).send({message: 'Confirmación de creación de cuenta enviada'}))
    .catch(error => res.status(500).send(error.toString()));
});

// Endpoint para enviar confirmación de orden
app.post('/sendOrderConfirmation', (req, res) => {
  const { email, nombreUsuario, idOrden, index_url } = req.body;
  const msg = {
    to: email,
    from: sender,
    templateId: 'd-ede4b8f64d4a4e27b59502c7e13c640d',
    dynamicTemplateData: {
      nombre_usuario: nombreUsuario,
      id_orden: idOrden,
      url: index_url
    }
  };

  sgMail
    .send(msg)
    .then(() => res.status(200).send({message: 'Confirmación de orden enviada'}))
    .catch(error => res.status(500).send(error.toString()));
});

// Iniciar el servidor
app.listen(port, () => {
  console.log(`Servidor corriendo en http://localhost:${port}`);
});

// Ejemplo de uso: 
    // sendVerificacion('sistemasdist2024@gmail.com')
// sendConfirmacionOrden('sistemasdist2024@gmail.com', 'Perrito', '12345')
