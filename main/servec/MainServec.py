from main.model import Modles
from main.repository import CustomerRepository, OrderRepository
import random


def get_three_random_products():
    all_products = Modles.Product.query.all()
    random_products = random.sample(all_products, 3)
    product_list = []
    for index, product in enumerate(random_products, start=1):
        product_data = {
            f'p{index}': {
                'category': product.category,
                'price': product.price,
                'size': product.size,
                'color': product.color,
                'code': product.p_code,
                'stock': product.stock,
                'photo': product.photo
            }
        }
        product_list.append(product_data)
    return product_list


def get_product_by_code(code):
    query_result = Modles.Product.query.filter_by(p_code=code).first()
    if query_result is not None:
        product = {
            'category': query_result.category,
            'stock': query_result.stock,
            'price': query_result.price,
            'size': query_result.size,
            'code': query_result.p_code,
            'color': query_result.color,
            'stock': query_result.stock,
            'photo': query_result.photo
        }
        return product
    else:
        return {'error': 'Product not found'}


def make_order(data):
    product_code = data.get('productCode')
    product = Modles.Product.query.filter_by(p_code=product_code).first()
    # can not find the product.
    if product is None:
        return {'error': 'Product not found!'}

    # product is out of stock
    if product.stock == 0:
        return {'error': 'Product is out of stock'}

    customer_name = data.get('customerName')
    customer_address = data.get('customerAddress')
    customer_phone = data.get('customerPhone')
    customer_email = data.get('customerEmail')
    customer = Modles.Customer.query.filter_by(c_email=customer_email).first()
    # the customer is not in the database
    if customer is None:
        customer = CustomerRepository.add(customer_name, customer_address, customer_email, customer_phone)
    order = OrderRepository.create_order(customer_address, customer, product)

    if order is not None:
        # the order is done:)
        order_result = {
            'date': order.o_date,
            'code': order.o_number,
            'total': order.o_total,
            'address': order.o_shippingaddress,
            'state': order.o_state
        }
        return order_result
    else:
        # an error
        return {'error': 'can not make the order!'}


def track_order(data):
    order_code = data.get('orderCode')
    query_result = Modles.Order.query.filter_by(o_number=order_code).first()
    if query_result is None:
        return {'error': 'can not find the order!'}
    order = {
        'date': query_result.o_date,
        'code': query_result.o_number,
        'total': query_result.o_total,
        'address': query_result.o_shippingaddress,
        'state': query_result.o_state
    }
    return order


def random_products_by_category(data):
    category = data.get('category')
    print(category)
    query_result = Modles.Product.query.filter(Modles.Product.category.like(f'%{category}%')).all()
    random_products = random.sample(query_result, 3)
    product_list = []
    for index, product in enumerate(random_products, start=1):
        product_data = {
            f'p{index}': {
                'category': product.category,
                'price': product.price,
                'size': product.size,
                'color': product.color,
                'code': product.p_code,
                'stock': product.stock,
                'photo': product.photo
            }
        }
        product_list.append(product_data)
    return product_list

