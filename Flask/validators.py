from functools import wraps
from flask import request, jsonify

def validate_coupon_generation(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        data = request.get_json()
        
        if not data.get('product_id') or not data.get('user_id'):
            return jsonify({
                'error': 'Missing required fields: product_id and user_id are required'
            }), 400
            
        validity_period = data.get('validity_period')
        if validity_period and (not isinstance(validity_period, (int, float)) or validity_period <= 0):
            return jsonify({
                'error': 'validity_period must be a positive number'
            }), 400
            
        return f(*args, **kwargs)
    return decorated_function

def validate_coupon_operation(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        data = request.get_json()
        
        if not all(k in data for k in ['coupon_code', 'product_id', 'user_id']):
            return jsonify({
                'error': 'Missing required fields: coupon_code, product_id, and user_id are required'
            }), 400
            
        return f(*args, **kwargs)
    return decorated_function 