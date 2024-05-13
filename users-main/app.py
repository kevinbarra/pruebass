"""
Main App
"""
from datetime import datetime as dt

from flask import Flask, request, jsonify
from flask_cors import CORS
from dotenv import load_dotenv

from my_lib.general import database, URI, crud_template

#? -----------------------------------------------------------------------------

load_dotenv()

app = Flask(__name__)

CORS(app)

#? -----------------------------------------------------------------------------

# Create a new user
@app.route(URI + 'users/create', methods=['POST'])
@crud_template(request, ['email', 'password', 'name', 'lastname', 'id_role'])
def create_user():
    """
    Create a new user

    Returns:
        response with the user created
    """

    if database.exist_user(request.json['email']):
        return jsonify({
            "message": "User already exist"
        }), 302

    if database.read_by_id('roles', int(request.json['id_role'])) is not None:
        created, user = database.create_table_row(
            'users',
            {
                "id_role": int(request.json['id_role']),
                'name': request.json['name'],
                'lastname': request.json['lastname'],
                'email': request.json['email'],
                'password': request.json['password'],
            }
        )

        if created:

            return jsonify({
                "message": "Created Successfully",
                "user": user.serialize()
            }), 201

    return jsonify({
        "message": "Error while creating"
    }), 501

# Read all users or user by id
@app.route(URI + 'users', methods=['GET'])
@app.route(URI + 'users/<int:user_id>', methods=['GET'])
def get_users(user_id=None):
    """
    Get all users or user by id

    Returns:
        response with all users or with the user
    """

    if user_id is None:

        users = database.read_all_table('users')

        return jsonify({
            "users": [user.serialize() for user in users]
        }), 200
    
    user = database.read_by_id('users', user_id)

    if user is None:
        return jsonify({
            "message": "User not found"
        }), 404
    
    return jsonify({
        "user": user.serialize()
    }), 200

# Update a user
@app.route(URI + 'users/update/<int:user_id>', methods=['PUT'])
@crud_template(request, optional_fields=['email', 'password', 'name', 'lastname', 'id_role', 'is_banned'])
def update_user(user_id):
    """
    Update a user

    Returns:
        response with the user updated
    """

    user = database.read_by_id('users', user_id)

    if user is None:
        return jsonify({
            "message": "User not found"
        }), 404
    
    rowInfo = request.json

    rowInfo['updated_at'] = dt.now()

    user = database.update_table_row('users', user_id, rowInfo)

    if user is not None:

        return jsonify({
            "message": "Updated Successfully",
            "user": user.serialize()
        }), 200
    
    return jsonify({
        "message": "Error while updating"
    }), 501

# Delete a user
@app.route(URI + 'users/delete/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    """
    Delete a user

    Returns:
        response with the user deleted
    """

    user = database.read_by_id('users', user_id)

    if user is None:
        return jsonify({
            "message": "User not found"
        }), 404
    
    deleted = database.delete_table_row('users', user_id)

    if deleted:

        return jsonify({
            "message": "Deleted Successfully",
        }), 200
    
    return jsonify({
        "message": "Error while deleting"
    }), 501

#? -----------------------------------------------------------------------------

# Create a new role
@app.route(URI + 'roles/create', methods=['POST'])
@crud_template(request, ['nombre'])
def create_role():
    """
    Create a new role

    Returns:
        response with the role created
    """

    created, role = database.create_table_row(
        'roles',
        {
            'nombre': request.json['nombre'],
        }
    )

    if created:

        return jsonify({
            "message": "Created Successfully",
            "role": role.serialize()
        }), 201

    return jsonify({
        "message": "Error while creating"
    }), 501

# Read all roles or role by id
@app.route(URI + 'roles', methods=['GET'])
@app.route(URI + 'roles/<int:role_id>', methods=['GET'])
def get_roles(role_id=None):
    """
    Get all roles or role by id

    Returns:
        response with all roles or with the role
    """

    if role_id is None:

        roles = database.read_all_table('roles')

        return jsonify({
            "roles": [role.serialize() for role in roles]
        }), 200
    
    role = database.read_by_id('roles', role_id)

    if role is None:
        return jsonify({
            "message": "Role not found"
        }), 404
    
    return jsonify({
        "role": role.serialize()
    }), 200    

# Update a role
@app.route(URI + 'roles/update/<int:role_id>', methods=['PUT'])
@crud_template(request, optional_fields=['nombre'])
def update_role(role_id):
    """
    Update a role

    Returns:
        response with the role updated
    """

    role = database.read_by_id('roles', role_id)

    if role is None:
        return jsonify({
            "message": "Role not found"
        }), 404

    role = database.update_table_row('roles', role_id, request.json)

    if role is not None:

        return jsonify({
            "message": "Updated Successfully",
            "role": role.serialize()
        }), 200
    
    return jsonify({
        "message": "Error while updating"
    }), 501

# Delete a role
@app.route(URI + 'roles/delete/<int:role_id>', methods=['DELETE'])
def delete_role(role_id):
    """
    Delete a role

    Returns:
        response with the role deleted
    """

    role = database.read_by_id('roles', role_id)

    if role is None:
        return jsonify({
            "message": "Role not found"
        }), 404
    
    deleted = database.delete_table_row('roles', role_id)

    if deleted:

        return jsonify({
            "message": "Deleted Successfully",
        }), 200
    
    return jsonify({
        "message": "Error while deleting"
    }), 501

#? -----------------------------------------------------------------------------

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')