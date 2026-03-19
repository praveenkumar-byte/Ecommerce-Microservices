from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

orders = []

@app.route('/orders', methods=['POST'])
def create_order():
    data = request.json

    # simulate service-to-service call
    product = requests.get("http://product-service:8002/products").json()

    orders.append({
        "order": data,
        "products_available": product
    })

    return jsonify({"message": "Order created"}), 201

@app.route('/orders', methods=['GET'])
def get_orders():
    return jsonify(orders)

app.run(host='0.0.0.0', port=8003)