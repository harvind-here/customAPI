from flask import Flask, request, jsonify
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
from dotenv import load_dotenv
from models import db, init_db
from routes import coupon_bp
import os
from urllib.parse import quote_plus

load_dotenv()

app = Flask(__name__)

# Database configuration
password = quote_plus(os.getenv('POSTGRES_PASSWORD'))
app.config['SQLALCHEMY_DATABASE_URI'] = (
    f"postgresql://{os.getenv('POSTGRES_USER')}:{password}"
    f"@{os.getenv('POSTGRES_HOST')}:{os.getenv('POSTGRES_PORT')}/{os.getenv('POSTGRES_DB')}"
)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize database
db.init_app(app)

# Rate limiter
limiter = Limiter(
    app=app,
    key_func=get_remote_address,
    default_limits=["100 per 15 minutes"]
)

# Register blueprints
app.register_blueprint(coupon_bp, url_prefix='/api')

# Root route
@app.route('/')
def home():
    return jsonify({
        'message': 'Welcome to Coupon API',
        'endpoints': {
            'generate_coupon': '/api/generate-coupon',
            'validate_coupon': '/api/validate-coupon',
            'redeem_coupon': '/api/redeem-coupon'
        }
    })

# Error handler
@app.errorhandler(Exception)
def handle_error(error):
    print(f"Error: {str(error)}")
    return jsonify({
        'error': 'Internal Server Error',
        'message': str(error) if app.debug else 'Something went wrong'
    }), 500

if __name__ == '__main__':
    with app.app_context():
        init_db()
    app.run(port=int(os.getenv('FLASK_PORT', 3000)), debug=True) 