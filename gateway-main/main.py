# dependencies -------->
from requests import post, get, put, delete
from flask import Flask, request, jsonify
from dotenv import load_dotenv
from flask_cors import CORS
import os
import stripe

# program initialization -------->
load_dotenv()

# program variables -------->
app = Flask(__name__)
CORS(app)

# end points -------->
# authentication endpoints --------
@app.route('/register', methods=['POST'])
def register():
    data = request.json
    if not data or 'email' not in data or 'password' not in data:
        return {'error': 'Missing data'}, 400
    # consume the service
    response = post(os.environ['AUTH_SERVICE']+'/register', json=data)
    return response.json(), response.status_code

@app.route('/login', methods=['POST'])
def login():
    data = request.json
    if not data or 'email' not in data or 'password' not in data:
        return {'error': 'Missing data'}, 400
    # consume the service
    response = post(os.environ['AUTH_SERVICE']+'/login', json=data)
    return response.json(), response.status_code

# order endpoints --------
@app.route('/orders', methods=['GET'])
def get_orders():
    # consume the service
    response = get(os.environ['ORDERS_SERVICE']+'/orders')
    return response.json(), response.status_code

@app.route('/orders', methods=['POST'])
def create_order():
    data = request.json
    # consume the service
    response = post(os.environ['ORDERS_SERVICE']+'/orders', json=data)
    return response.json(), response.status_code

@app.route('/orders/<int:order_id>', methods=['GET'])
def get_order(order_id):
    # consume the service
    response = get(os.environ['ORDERS_SERVICE']+f'/orders/{order_id}')
    return response.json(), response.status_code

@app.route('/orders/<int:order_id>', methods=['PUT'])
def update_order(order_id):
    data = request.json
    # consume the service
    response = put(os.environ['ORDERS_SERVICE']+f'/orders/{order_id}', json=data)
    return response.json(), response.status_code

@app.route('/orders/<int:order_id>', methods=['DELETE'])
def delete_order(order_id):
    # consume the service
    response = delete(os.environ['ORDERS_SERVICE']+f'/orders/{order_id}')
    return response.json(), response.status_code

# cart endpoints --------
@app.route('/cart', methods=['POST'])
def add_to_cart():
    data = request.json
    # consume the service
    response = post(os.environ['CART_SERVICE']+'/cart', json=data)
    return response.json(), response.status_code

@app.route('/get_cart', methods=['POST'])
def get_cart():
    data = request.json
    # consume the service
    response = post(os.environ['CART_SERVICE']+'/get-cart', json=data)
    return response.json(), response.status_code

@app.route('/cart', methods=['DELETE'])
def del_cart():
    data = request.json
    # consume the service
    response = delete(os.environ['CART_SERVICE']+'/cart', json=data)
    return response.json(), response.status_code

# products endpoints --------
# /api/v1/products
@app.route('/products/<int:page>', methods=['GET'])
def get_products(page):
    # consume the service
    response = get(os.environ['PRODUCT_SERVICE']+f'/api/v1/products/{page}')
    return response.json(), response.status_code

@app.route('/products', methods=['POST'])
def create_product():
    data = request.json
    # consume the service
    response = post(os.environ['PRODUCT_SERVICE']+'/api/v1/products', json=data)
    return response.json(), response.status_code

@app.route('/products/<string:product_id>', methods=['GET'])
def get_product(product_id):
    # consume the service
    response = get(os.environ['PRODUCT_SERVICE']+f'/api/v1/products/{product_id}')
    return response.json(), response.status_code

@app.route('/products/<string:product_id>', methods=['PUT'])
def update_product(product_id):
    data = request.json
    # consume the service
    response = put(os.environ['PRODUCT_SERVICE']+f'/api/v1/products/{product_id}', json=data)
    return response.json(), response.status_code

@app.route('/products/<string:product_id>', methods=['DELETE'])
def delete_product(product_id):
    # consume the service
    response = delete(os.environ['PRODUCT_SERVICE']+f'/api/v1/products/{product_id}')
    return response.json(), response.status_code

@app.route('/search/<int:page>', methods=['POST'])
def search_product(page):
    data = request.json
    # consume the service
    response = post(os.environ['PRODUCT_SERVICE']+f'/api/v1/search/{page}', json=data)
    return response.json(), response.status_code

@app.route('/categories', methods=['GET'])
def get_categories():
    # consume the service
    response = get(os.environ['PRODUCT_SERVICE']+'/api/v1/categories')
    return response.json(), response.status_code

@app.route('/categories', methods=['POST'])
def create_category():
    data = request.json
    # consume the service
    response = post(os.environ['PRODUCT_SERVICE']+'/api/v1/categories', json=data)
    return response.json(), response.status_code

@app.route('/categories/<string:category_id>', methods=['GET'])
def get_category(category_id):
    # consume the service
    response = get(os.environ['PRODUCT_SERVICE']+f'/api/v1/categories/{category_id}')
    return response.json(), response.status_code


@app.route('/categories/<string:category_id>', methods=['PUT'])
def update_category(category_id):
    data = request.json
    # consume the service
    response = put(os.environ['PRODUCT_SERVICE']+f'/api/v1/categories/{category_id}', json=data)
    return response.json(), response.status_code

@app.route('/categories/<string:category_id>', methods=['DELETE'])
def delete_category(category_id):
    # consume the service
    response = delete(os.environ['PRODUCT_SERVICE']+f'/api/v1/categories/{category_id}')
    return response.json(), response.status_code

# /api/v1/
# user endpoints --------
@app.route('/users/create', methods=['POST'])
def create_user():
    data = request.json
    # consume the service
    response = post(os.environ['USER_SERVICE']+'/api/v1/users/create', json=data)
    return response.json(), response.status_code


# Read all users or user by id
@app.route('/users', methods=['GET'])
@app.route('/users/<int:user_id>', methods=['GET'])
def get_users(user_id=None):
    if user_id is None:
        # consume the service
        response = get(os.environ['USER_SERVICE']+'/api/v1/users')
        return response.json(), response.status_code
    else:
        # consume the service
        response = get(os.environ['USER_SERVICE']+f'/api/v1/users/{user_id}')
        return response.json(), response.status_code

# Update a user
@app.route('/users/update/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    data = request.json
    # consume the service
    response = put(os.environ['USER_SERVICE']+f'/api/v1/users/update/{user_id}', json=data)
    return response.json(), response.status_code

# Delete a user
@app.route('/users/delete/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    # consume the service
    response = delete(os.environ['USER_SERVICE']+f'/api/v1/users/delete/{user_id}')
    return response.json(), response.status_code

# Create a new role
@app.route('/roles/create', methods=['POST'])
def create_role():
    data = request.json
    # consume the service
    response = post(os.environ['USER_SERVICE']+'/api/v1/roles/create', json=data)
    return response.json(), response.status_code

# Read all roles or role by id
@app.route('/roles', methods=['GET'])
@app.route('/roles/<int:role_id>', methods=['GET'])
def get_roles(role_id=None):
    if role_id is None:
        # consume the service
        response = get(os.environ['USER_SERVICE']+'/api/v1/roles')
        return response.json(), response.status_code
    else:
        # consume the service
        response = get(os.environ['USER_SERVICE']+f'/api/v1/roles/{role_id}')
        return response.json(), response.status_code

# Update a role
@app.route('/roles/update/<int:role_id>', methods=['PUT'])
def update_role(role_id):
    data = request.json
    # consume the service
    response = put(os.environ['USER_SERVICE']+f'/api/v1/roles/update/{role_id}', json=data)
    return response.json(), response.status_code

# Delete a role
@app.route('/roles/delete/<int:role_id>', methods=['DELETE'])
def delete_role(role_id):
    # consume the service
    response = delete(os.environ['USER_SERVICE']+f'/api/v1/roles/delete/{role_id}')
    return response.json(), response.status_code

# mail endpoints --------
@app.route('/sendVerification', methods=['POST'])
def send_verification():
    data = request.json
    # consume the service
    response = post(os.environ['EMAIL_SERVICE']+'/sendVerification', json=data)
    return response.json(), response.status_code

@app.route('/sendPasswordChange', methods=['POST'])
def send_passwd_change():
    data = request.json
    # consume the service
    response = post(os.environ['EMAIL_SERVICE']+'/sendPasswordChange', json=data)
    return response.json(), response.status_code

@app.route('/sendAccountConfirmation', methods=['POST'])
def send_account_conf():
    data = request.json
    # consume the service
    response = post(os.environ['EMAIL_SERVICE']+'/sendAccountConfirmation', json=data)
    return response.json(), response.status_code

@app.route('/sendOrderConfirmation', methods=['POST'])
def send_order_conf():
    data = request.json
    # consume the service
    response = post(os.environ['EMAIL_SERVICE']+'/sendOrderConfirmation', json=data)
    return response.json(), response.status_code

# special endpoints --------
@app.route('/buy/<int:user_id>', methods=['POST'])
def buy(user_id):
    # local variables
    index_url = request.json['index_url']
    products = []
    temp = {}
    try:
        # get user data
        # consume the service
        user_data = get(os.environ['USER_SERVICE']+f'/api/v1/users/{user_id}').json()
        # consume the service
        response = post(os.environ['CART_SERVICE']+'/get-cart', json={'user_id' : user_id}).json()
        # dictionary list [{}]
        # item is the key for the product id
        # quantity is the key for the quantity of the product
        for key in response.keys():
            # key is the item and the item is the quantity 
            temp['id_producto'] = key
            temp['cantidad'] = response[key]
            products.append(temp)
            temp = {}
        # generate order and retrieve order_id
        response = post(os.environ['ORDERS_SERVICE']+'/orders', json={'id_usuario' : user_id, 'productos' : products})
        order_id = response.json()['order_id']
        # send order confirmation
        response = post(os.environ['EMAIL_SERVICE']+'/sendOrderConfirmation', json={'email' : user_data['email'], 'nombreUsuario' : user_data['name'], 'idOrden' : order_id, 'index_url' : index_url})
        return "Successful Transaction", 200
    except Exception as e:
        return e.message, 400
    
@app.route('/cart/add', methods=['POST'])
def add_product_to_cart():
    # local variables
    count = 0
    data = request.json
    # consume the service
    response = post(os.environ['CART_SERVICE']+'/get-cart', json=data).json()
    if data['item_id'] in response.keys():
        # get total quantity
        count = data['quantity']
        # delete the previous data of the product
        response = post(os.environ['CART_SERVICE']+'/cart', json={'item_id' : data['item_id'], 'quantity' : 0, 'user_id' : data['user_id']})
        # update the product in the db
        response = post(os.environ['CART_SERVICE']+'/cart', json={'item_id' : data['item_id'], 'quantity' : count, 'user_id' : data['user_id']})
        return response.json()
    else:
        # add the product in the db
        response = post(os.environ['CART_SERVICE']+'/cart', json={'item_id' : data['item_id'], 'quantity' : data['quantity'], 'user_id' : data['user_id']})
        return response.json()

@app.route('/users/add', methods=['POST'])
def add_user():
    # local variables
    user = 0
    data = request.json
    # consume the service
    response = post(os.environ['USER_SERVICE']+'/api/v1/users/create', json=data).json()
    # get user
    user = response['user']
    # send confirmation mail
    response = post(os.environ['EMAIL_SERVICE']+'/sendAccountConfirmation', json={'email' : user['email'], 'nombreUsuario' : user['name'], 'index_url' : data['index_url']})
    return response.json(), response.status_code

@app.route('/create-payment-intent', methods=['POST'])
def create_payment():
    try:
        stripe_keys = {
            "secret_key": os.getenv("STRIPE_SECRET_KEY"),
            "publishable_key": os.getenv("STRIPE_PUBLISHABLE_KEY"),
        }

        stripe.api_key = stripe_keys["secret_key"]

        data = request.get_json()

        intent = stripe.PaymentIntent.create(
            amount=data['amount'] * 100,
            currency='usd',
            automatic_payment_methods={
                'enabled': True,
            },
            metadata={'customer': data['customer']}
        )

        return ({
            'clientSecret': intent['client_secret']
        })

    except Exception as e:
        return jsonify(error=str(e)), 403

# program execution -------->
if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=6789)