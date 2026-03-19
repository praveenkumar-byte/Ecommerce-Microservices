from flask import Flask, request, jsonify

app = Flask(__name__)

products = []

@app.route('/products', methods=['POST'])
def add_product():
    data = request.json
    products.append(data)
    return jsonify({"message": "Product added"}), 201

@app.route('/products', methods=['GET'])
def get_products():
    return jsonify(products)

app.run(host='0.0.0.0', port=8002)