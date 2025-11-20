from flask import Flask, jsonify

app = Flask(__name__)

products = [
    {"id": 1, "name": "Wireless Noise-Cancelling Headphones", "price": 199.99},
    {"id": 2, "name": "Smartphone 6.7\" OLED 256GB", "price": 899.00},
    {"id": 3, "name": "Portable SSD 1TB USB-C", "price": 129.50},
]

@app.route("/products", methods=["GET"])
def get_products():
    return jsonify(products), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)