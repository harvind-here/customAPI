# Coupon API

A RESTful API for generating, validating, and redeeming time-bound discount coupons. Implemented in both Node.js/Express and Flask.

## Directory Structure

customAPI/
├── Node.js/
│ ├── src/
│ │ ├── config/
│ │ │ └── database.js
│ │ ├── controllers/
│ │ │ └── couponController.js
│ │ ├── middleware/
│ │ │ ├── errorHandler.js
│ │ │ ├── rateLimiter.js
│ │ │ └── validator.js
│ │ ├── routes/
│ │ │ └── couponRoutes.js
│ │ ├── services/
│ │ │ └── couponService.js
│ │ ├── utils/
│ │ │ └── logger.js
│ │ └── app.js
│ ├── .env
│ └── package.json
│
└── Flask/
├── app.py
├── models.py
├── routes.py
├── services.py
├── validators.py
├── .env
└── requirements.txt


## Features

- Generate unique, time-bound discount coupons
- Validate coupons for specific products and users
- Redeem coupons with proper validation
- API request logging
- Rate limiting
- Error handling
- PostgreSQL database integration

## Prerequisites

- PostgreSQL installed and running
- Node.js (for Express implementation)
- Python 3.x (for Flask implementation)

## Setup Instructions

### Database Setup

1. Install PostgreSQL
2. Create a database:
```sql
CREATE DATABASE coupon_db;
```

### Express.js Implementation

1. Navigate to Node.js directory:
```bash
cd Node.js
```

2. Install dependencies:
```bash
npm install
```

3. Configure environment variables:
```bash
cp .env
```

4. Start the server:
```bash
npm run dev
```

### Flask Implementation

1. Navigate to Flask directory:
```bash
cd Flask
```

2. Create and activate virtual environment:
```bash
python -m venv venv
source venv/bin/activate # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Configure environment variables:
Edit .env with your database credentials

5. Run the application:
```bash
python app.py
```

## API Endpoints

### Generate Coupon
```
http
POST /api/generate-coupon
Content-Type: application/json
{
"product_id": "PROD123",
"user_id": "USER1",
"validity_period": 24
}
```

### Validate Coupon
```
http
POST /api/validate-coupon
Content-Type: application/json
{
"coupon_code": "PRODPROD123-xxxxxxxx",
"product_id": "PROD123",
"user_id": "USER1"
}
```

### Redeem Coupon
```
http
POST /api/redeem-coupon
Content-Type: application/json
{
"coupon_code": "PRODPROD123-xxxxxxxx",
"product_id": "PROD123",
"user_id": "USER1"
}
```

## Database Schema

### Coupons Table



### API Logs Table


