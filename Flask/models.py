from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import json

db = SQLAlchemy()

class Coupon(db.Model):
    __tablename__ = 'coupons'
    
    coupon_code = db.Column(db.String(50), primary_key=True)
    product_id = db.Column(db.String(50), nullable=False)
    user_id = db.Column(db.String(50), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    expires_at = db.Column(db.DateTime, nullable=False)
    redeemed = db.Column(db.Boolean, default=False)

class ApiLog(db.Model):
    __tablename__ = 'api_logs'
    
    id = db.Column(db.Integer, primary_key=True)
    endpoint = db.Column(db.String(50), nullable=False)
    request_data = db.Column(db.JSON)
    response_data = db.Column(db.JSON)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)

def init_db():
    db.create_all() 