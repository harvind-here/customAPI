from flask import Blueprint, request, jsonify
from services import CouponService, Logger
from validators import validate_coupon_generation, validate_coupon_operation

coupon_bp = Blueprint('coupon', __name__)

@coupon_bp.route('/generate-coupon', methods=['POST'])
@validate_coupon_generation
def generate_coupon():
    data = request.get_json()
    coupon = CouponService.generate_coupon(
        data['product_id'],
        data['user_id'],
        data.get('validity_period', 24)
    )
    
    response = {
        'coupon_code': coupon.coupon_code,
        'expires_at': coupon.expires_at.isoformat()
    }
    
    Logger.log_api_request(request.path, data, response)
    return jsonify(response), 201

@coupon_bp.route('/validate-coupon', methods=['POST'])
@validate_coupon_operation
def validate_coupon():
    data = request.get_json()
    is_valid = CouponService.validate_coupon(
        data['coupon_code'],
        data['product_id'],
        data['user_id']
    )
    
    response = {
        'valid': is_valid,
        'message': 'Coupon is valid.' if is_valid else 'Coupon is expired or invalid.'
    }
    
    Logger.log_api_request(request.path, data, response)
    return jsonify(response)

@coupon_bp.route('/redeem-coupon', methods=['POST'])
@validate_coupon_operation
def redeem_coupon():
    data = request.get_json()
    redeemed_coupon = CouponService.redeem_coupon(
        data['coupon_code'],
        data['product_id'],
        data['user_id']
    )
    
    response = {
        'redeemed': bool(redeemed_coupon),
        'message': 'Coupon successfully redeemed.' if redeemed_coupon else 'Coupon is invalid or already redeemed.'
    }
    
    Logger.log_api_request(request.path, data, response)
    return jsonify(response) 