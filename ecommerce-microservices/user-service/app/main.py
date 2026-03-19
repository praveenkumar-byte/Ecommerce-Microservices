from flask import Flask, request, jsonify

app = Flask(__name__)

users = []

@app.route('/users', methods=['POST'])
def create_user():
    data = request.json
    users.append(data)
    return jsonify({"message": "User created"}), 201

@app.route('/users', methods=['GET'])
def get_users():
    return jsonify(users)

app.run(host='0.0.0.0', port=8001)