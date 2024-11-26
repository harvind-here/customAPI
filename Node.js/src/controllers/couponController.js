const couponService = require('../services/couponService');
const logger = require('../utils/logger');

class CouponController {
  async generateCoupon(req, res, next) {
    try {
      const { product_id, user_id, validity_period } = req.body;
      const coupon = await couponService.generateCoupon(product_id, user_id, validity_period);
      
      await logger.logApiRequest(req.path, req.body, coupon);
      
      res.status(201).json({
        coupon_code: coupon.coupon_code,
        expires_at: coupon.expires_at
      });
    } catch (error) {
      next(error);
    }
  }

  async validateCoupon(req, res, next) {
    try {
      const { coupon_code, product_id, user_id } = req.body;
      const isValid = await couponService.validateCoupon(coupon_code, product_id, user_id);
      
      const response = {
        valid: isValid,
        message: isValid ? 'Coupon is valid.' : 'Coupon is expired or invalid.'
      };
      
      await logger.logApiRequest(req.path, req.body, response);
      
      res.json(response);
    } catch (error) {
      next(error);
    }
  }

  async redeemCoupon(req, res, next) {
    try {
      const { coupon_code, product_id, user_id } = req.body;
      const redeemedCoupon = await couponService.redeemCoupon(coupon_code, product_id, user_id);
      
      const response = {
        redeemed: !!redeemedCoupon,
        message: redeemedCoupon 
          ? 'Coupon successfully redeemed.'
          : 'Coupon is invalid or already redeemed.'
      };
      
      await logger.logApiRequest(req.path, req.body, response);
      
      res.json(response);
    } catch (error) {
      next(error);
    }
  }
}

module.exports = new CouponController(); 