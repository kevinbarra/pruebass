from flask import Flask, request, jsonify
from flask_cors import CORS
from pymongo import MongoClient
from bson import ObjectId
from datetime import datetime
from dotenv import load_dotenv
import os
from general import crud_template

load_dotenv()

app = Flask(__name__)
CORS(app)

PAGE_SIZE = int(os.getenv('PAGE_SIZE'))
URI = os.getenv('URI')

mongodb_uri = os.getenv('MONGODB_URI')
database_name = os.getenv('DATABASE_NAME')

client = MongoClient(mongodb_uri)
db = client[database_name]
products_collection = db[os.getenv('PRODUCTS_COLLECTION_NAME')]
categories_collection = db[os.getenv('CATEGORIES_COLLECTION_NAME')]


@app.route(f'/{URI}products/<int:page>', methods=['GET'])
def get_products(page):
    offset = (page - 1) * PAGE_SIZE
    products = list(products_collection.find().skip(offset).limit(PAGE_SIZE))
    total_products = products_collection.count_documents({})
    total_pages = (total_products + PAGE_SIZE - 1) // PAGE_SIZE

    for product in products:
        product['_id'] = str(product['_id'])

    return jsonify({
        'products': products,
        'total_pages': total_pages
    })


@app.route(f'/{URI}products', methods=['POST'])
@crud_template(request, needed_fields=['id_category', 'name', 'description', 'stock', 'price'])
def create_product():
    data = request.get_json()

    category_id = data.get('id_category')

    category = categories_collection.find_one({'_id': ObjectId(category_id)})

    if not category:
        return jsonify({'message': 'Category not found'}), 404

    campos_categoria = category.get('fields')

    campos_adicionales = data.keys()

    for campo in campos_adicionales:
        if campo in ['id_category', 'name', 'description', 'stock', 'price']:
            continue

        if campo not in campos_categoria:
            return jsonify({'message': f'Campo "{campo}" no permitido para esta categoría'}), 400

    campos_faltantes = [campo for campo in campos_categoria if campo not in campos_adicionales]

    if campos_faltantes:
        return jsonify({'message': f'Missing required additional field(s): {", ".join(campos_faltantes)}'}), 400

    data['timestamps'] = {'created_at': datetime.now(), 'updated_at': None}

    product_id = products_collection.insert_one(data).inserted_id

    new_product = products_collection.find_one({'_id': product_id})

    new_product['_id'] = str(new_product['_id'])

    return jsonify({'message': 'Product created successfully', 'product': new_product})


@app.route(f'/{URI}products/<string:product_id>', methods=['GET'])
def get_product(product_id):
    product = products_collection.find_one({'_id': ObjectId(product_id)})
    if product:
        product['_id'] = str(product['_id'])
        return jsonify(product)
    else:
        return jsonify({'message': 'Product not found'}), 404


@app.route(f'/{URI}products/<string:product_id>', methods=['PUT'])
@crud_template(request, optional_fields=['name', 'description', 'stock', 'price', 'fields'])
def update_product(product_id):
    data = request.get_json()
    if not data:
        return jsonify({'message': 'No data provided'}), 400

    data['timestamps'] = {'updated_at': datetime.now()}
    updated_product = products_collection.update_one(
        {'_id': ObjectId(product_id)}, {'$set': data})
    if updated_product.modified_count:
        return jsonify({'message': 'Product updated successfully'})
    else:
        return jsonify({'message': 'Product not found'}), 404


@app.route(f'/{URI}products/<string:product_id>', methods=['DELETE'])
def delete_product(product_id):
    deleted_product = products_collection.delete_one(
        {'_id': ObjectId(product_id)})
    if deleted_product.deleted_count:
        return jsonify({'message': 'Product deleted successfully'})
    else:
        return jsonify({'message': 'Product not found'}), 404


@app.route(f'/{URI}search/<int:page>', methods=['POST'])
def search_product(page):
    query_data = request.get_json()
    category_id = query_data.get('id_category')
    product_name = query_data.get('query')
    price_min = query_data.get('price_min')
    price_max = query_data.get('price_max')

    query = {}
    if category_id:
        query['id_category'] = category_id
    if product_name:
        query['$or'] = [
            {'name': {'$regex': f".*{product_name}.*", '$options': 'i'}},
            {'description': {'$regex': f".*{product_name}.*", '$options': 'i'}}
        ]
    if price_min is not None:
        query['price'] = {'$gte': price_min}
    if price_max is not None:
        query.setdefault('price', {})['$lte'] = price_max

    page_size = PAGE_SIZE
    offset = (page - 1) * page_size
    products = list(products_collection.find(
        query).skip(offset).limit(page_size))
    total_products = products_collection.count_documents(query)
    total_pages = (total_products + page_size - 1) // page_size

    for product in products:
        product['_id'] = str(product['_id'])

    return jsonify({
        'products': products,
        'total_pages': total_pages
    })


@app.route(f'/{URI}categories', methods=['GET'])
def get_categories():
    categories = list(categories_collection.find())
    for category in categories:
        category['_id'] = str(category['_id'])
    return jsonify({'categories': categories})


@app.route(f'/{URI}categories', methods=['POST'])
@crud_template(request, needed_fields=['name', 'description', 'fields'])
def create_category():
    data = request.get_json()

    if not data['fields']:
        return jsonify({'message': 'The "campos" list cannot be empty'}), 400

    data['created_at'] = datetime.now()
    category_id = categories_collection.insert_one(data).inserted_id
    new_category = categories_collection.find_one({'_id': category_id})

    new_category['_id'] = str(new_category['_id'])

    return jsonify({'message': 'Category created successfully', 'category': new_category})


@app.route(f'/{URI}categories/<string:category_id>', methods=['GET'])
def get_category(category_id):
    category = categories_collection.find_one({'_id': ObjectId(category_id)})
    if category:
        category['_id'] = str(category['_id'])
        return jsonify(category)
    else:
        return jsonify({'message': 'Category not found'}), 404


@app.route(f'/{URI}categories/<string:category_id>', methods=['PUT'])
@crud_template(request, optional_fields=['name', 'description', 'fields'])
def update_category(category_id):
    data = request.get_json()
    if not data:
        return jsonify({'message': 'No data provided'}), 400

    data['updated_at'] = datetime.now()
    updated_category = categories_collection.update_one(
        {'_id': ObjectId(category_id)}, {'$set': data})
    if updated_category.modified_count:
        return jsonify({'message': 'Category updated successfully'})
    else:
        return jsonify({'message': 'Category not found'}), 404


@app.route(f'/{URI}categories/<string:category_id>', methods=['DELETE'])
def delete_category(category_id):
    deleted_category = categories_collection.delete_one(
        {'_id': ObjectId(category_id)})
    if deleted_category.deleted_count:
        return jsonify({'message': 'Category deleted successfully'})
    else:
        return jsonify({'message': 'Category not found'}), 404


if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=5000)
