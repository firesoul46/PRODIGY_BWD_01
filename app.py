from flask import Flask, request, jsonify
import uuid
import re

app = Flask(__name__)

# In-memory user storage
users = {}

# Email validation regex
EMAIL_REGEX = re.compile(r"[^@]+@[^@]+\.[^@]+")

# Helper to validate user data
def validate_user_data(data):
    if not data.get('name') or not isinstance(data['name'], str):
        return False, "Name is required and must be a string."
    if not data.get('email') or not EMAIL_REGEX.match(data['email']):
        return False, "Invalid or missing email."
    if not data.get('age') or not isinstance(data['age'], int):
        return False, "Age is required and must be an integer."
    return True, None

# Create user
@app.route('/users', methods=['POST'])
def create_user():
    data = request.get_json()
    valid, error = validate_user_data(data)
    if not valid:
        return jsonify({"error": error}), 400

    user_id = str(uuid.uuid4())
    users[user_id] = {
        "id": user_id,
        "name": data['name'],
        "email": data['email'],
        "age": data['age']
    }
    return jsonify(users[user_id]), 201

# Read all users
@app.route('/users', methods=['GET'])
def get_users():
    return jsonify(list(users.values())), 200

# Read single user
@app.route('/users/<user_id>', methods=['GET'])
def get_user(user_id):
    user = users.get(user_id)
    if not user:
        return jsonify({"error": "User not found"}), 404
    return jsonify(user), 200

# Update user
@app.route('/users/<user_id>', methods=['PUT'])
def update_user(user_id):
    user = users.get(user_id)
    if not user:
        return jsonify({"error": "User not found"}), 404

    data = request.get_json()
    valid, error = validate_user_data(data)
    if not valid:
        return jsonify({"error": error}), 400

    user.update({
        "name": data['name'],
        "email": data['email'],
        "age": data['age']
    })
    return jsonify(user), 200

# Delete user
@app.route('/users/<user_id>', methods=['DELETE'])
def delete_user(user_id):
    if user_id not in users:
        return jsonify({"error": "User not found"}), 404
    del users[user_id]
    return jsonify({"message": "User deleted successfully."}), 200

if __name__ == '__main__':
    app.run(debug=True)
