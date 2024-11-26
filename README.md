# Coupon API
A RESTful API for generating, validating, and redeeming time-bound discount coupons. Implemented in both Node.js/Express and Flask.

## Skills
<img src="https://img.shields.io/badge/Flask-3776AB?style=flat-square&logo=Flask&logoColor=white" alt="Flask"> <img src="https://img.shields.io/badge/NodeJS-FFA500?style=flat-square&logo=Node.js&logoColor=white" alt="Node.js"> <img src="https://img.shields.io/badge/PostgreSQL-FFD700?style=flat-square&logo=PostgreSQL&logoColor=white" alt="PostgreSQL">

```
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
```

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
![Screenshot 2024-11-26 234104](https://github.com/user-attachments/assets/f9330a70-688d-435c-8fce-1b1a89d5b19e)

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
![Screenshot 2024-11-26 234040](https://github.com/user-attachments/assets/4536abdd-152c-40fb-8acb-d1d334a0b87a)

### API Logs Table
![Screenshot 2024-11-27 002448](https://github.com/user-attachments/assets/0799c796-d67f-46bc-88f7-19792869a5ba)
