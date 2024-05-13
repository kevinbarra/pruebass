# API Pedidos

## Descripcion

API para la gestión de los pedidos almacenados en una base de datos SQL.

## Lenguaje de desarrollo 

Lenguaje: `Python`

Framework: `Flask`

## Librerías adicionales 

-`Flask`
-`flask_sqlalchemy`
-`python-dotenv`

## Link a las documentaciones adicionales 

[Documentación de Flask](https://flask-es.readthedocs.io/)

[Documentación de Flask MySQL](https://flask-mysql.readthedocs.io/en/latest//)

[Documentación de python-dotenv](https://pypi.org/project/python-dotenv/)


## Endpoints

| Endpoint             | Descripción                               | Método |
| -------------------- | ----------------------------------------- | ------ |
| `/order/{page}`      | Lista de todos los pedidos.               | GET    |
| `/orders`            | Crear un nuevo pedido.                    | POST   |
| `/orders/{order_id}` | Obtener detalles de un pedido específico. | GET    |
| `/orders/{order_id}` | Actualizar detalles de un pedido.         | PUT    |
| `/orders/{order_id}` | Eliminar un pedido.                       | DELETE |

## Consideraciones adicionales

Deben considerar que la orden le pertenece a un usuario, por lo que debe pedir esa información por medio del body de la request