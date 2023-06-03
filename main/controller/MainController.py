from flask import jsonify, request
from main.main import app
from main.servec import MainServec


@app.route('/', methods=['GET'])
def api():
    data = {
        'message': 'Hello, World!'
    }
    return jsonify(data)


@app.route('/marketChatbot/api/v1/randomProduct', methods=['GET'])
def random_products():
    products = MainServec.get_three_random_products()
    return jsonify(products)


@app.route('/marketChatbot/api/v1/getProductByCode', methods=['POST'])
def get_product_by_code():
    data = request.json
    code = data.get('code')
    product = MainServec.get_product_by_code(code)
    return jsonify(product)


@app.route('/marketChatbot/api/v1/newOrder', methods=['POST'])
def make_order():
    data = request.json
    order = MainServec.make_order(data)
    return jsonify(order)


@app.route('/marketChatbot/api/v1/trackOrder', methods=['POST'])
def track_order():
    data = request.json
    order = MainServec.track_order(data)
    return jsonify(order)


@app.route('/marketChatbot/api/v1/productsByCategory', methods=['POST'])
def random_products_by_category():
    data = request.json
    products = MainServec.random_products_by_category(data)
    return jsonify(products)
