const express = require('express');
const router = express.Router();
const couponController = require('../controllers/couponController');
const { validateCouponGeneration, validateCouponOperation } = require('../middleware/validator');
const rateLimiter = require('../middleware/rateLimiter');

router.post('/generate-coupon', 
  rateLimiter,
  validateCouponGeneration,
  couponController.generateCoupon
);

router.post('/validate-coupon',
  validateCouponOperation,
  couponController.validateCoupon
);

router.post('/redeem-coupon',
  validateCouponOperation,
  couponController.redeemCoupon
);

module.exports = router; 