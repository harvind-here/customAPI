from models import db, Coupon, ApiLog
from datetime import datetime, timedelta
import uuid

class CouponService:
    @staticmethod
    def generate_coupon(product_id, user_id, validity_period=24):
        coupon_code = f"PROD{product_id}-{str(uuid.uuid4())[:8]}"
        expires_at = datetime.utcnow() + timedelta(hours=validity_period)
        
        coupon = Coupon(
            coupon_code=coupon_code,
            product_id=product_id,
            user_id=user_id,
            expires_at=expires_at
        )
        
        db.session.add(coupon)
        db.session.commit()
        return coupon

    @staticmethod
    def validate_coupon(coupon_code, product_id, user_id):
        coupon = Coupon.query.filter_by(
            coupon_code=coupon_code,
            product_id=product_id,
            user_id=user_id,
            redeemed=False
        ).first()
        
        if coupon and coupon.expires_at > datetime.utcnow():
            return True
        return False

    @staticmethod
    def redeem_coupon(coupon_code, product_id, user_id):
        coupon = Coupon.query.filter_by(
            coupon_code=coupon_code,
            product_id=product_id,
            user_id=user_id,
            redeemed=False
        ).first()
        
        if coupon and coupon.expires_at > datetime.utcnow():
            coupon.redeemed = True
            db.session.commit()
            return coupon
        return None

class Logger:
    @staticmethod
    def log_api_request(endpoint, request_data, response_data):
        log = ApiLog(
            endpoint=endpoint,
            request_data=request_data,
            response_data=response_data
        )
        db.session.add(log)
        db.session.commit() 