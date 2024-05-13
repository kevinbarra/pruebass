# API Productos

## Descripción

API para la gestión de los productos almacenados en una base de datos MongoDB.

## Tecnologías

Lenguaje: `Python`

Framework: `Flask`

### Librerías

- `Flask`
- `Flask-CORS`
- `Flask-PyMongo` o `pymongo`
- `python-dotenv`

### Documentación y Video

[Documentación en MongoDB](https://www.mongodb.com/docs/drivers/pymongo/)

[Documentación de PyMongoDB](https://pymongo.readthedocs.io/en/stable/tutorial.html)

[Documentación de Flask-PyMongo](https://flask-pymongo.readthedocs.io/en/latest/)

[Video Corto](https://youtu.be/mCdA4bJAGGk?si=OA84M1K5vKp9HAdK)

[Serie de Videos](https://www.youtube.com/watch?v=tJxMPvzkCyo&list=PLU7aW4OZeUzwN0TsZLZUuzhc0f7OVVBcT)



## Variables de Entorno

- `MONGO_URI`: URL de la base de datos.
- `PORT`: Puerto de la aplicación.
- `HOST`: Host de la aplicación.
- `DEBUG`: Modo de depuración.

## Endpoints

Endpoint base: `/api/v1`

| Endpoint                    | Descripción                           | Método |
| --------------------------- | ------------------------------------- | ------ |
| `/products/{page}`          | Lista de todos los productos.         | GET    |
| `/products`                 | Crear un nuevo producto.              | POST   |
| `/products/{product_id}`    | Obtener un producto.                  | GET    |
| `/products/{product_id}`    | Actualizar un producto.               | PUT    |
| `/products/{product_id}`    | Eliminar un producto.                 | DELETE |
| `/search/{page}`            | Buscar un producto por sus atributos. | POST   |
| `/categories`               | Obtener todas las categorías.         | GET    |
| `/categories`               | Crear una categoría.                  | POST   |
| `/categories/{category_id}` | Obtener una categoría.                | GET    |
| `/categories/{category_id}` | Actualizar una categoría.             | PUT    |
| `/categories/{category_id}` | Eliminar una categoría.               | DELETE |

## Consideraciones adicionales

En los endpoints `/products`, `/search` se deben paginar los resultados antes de retornarlos e indicar cuantas paginas disponibles hay.

Para acceder a la siguiente se debe mandar el parámetro `page` con la misma consulta en el caso de `/search`.

La búsqueda se puede hacer por:

- categoría
- nombre
- descripción
- precio

```json
{
    "category": 1,
    "query": "laptop",
    "price_max": 1500,
    "price_min": 1000,
}
```
    
Todos los parámetros son opcionales menos `query` que es obligatorio, mediante el cual se busca productos que coincidan con el nombre o la descripción.
