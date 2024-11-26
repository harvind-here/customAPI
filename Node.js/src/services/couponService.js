const { v4: uuidv4 } = require('uuid');
const { pool } = require('../config/database');

class CouponService {
  async generateCoupon(productId, userId, validityPeriod = 24) {
    const couponCode = `PROD${productId}-${uuidv4().substring(0, 8)}`;
    const expiresAt = new Date(Date.now() + validityPeriod * 60 * 60 * 1000);

    const query = `
      INSERT INTO coupons (coupon_code, product_id, user_id, expires_at)
      VALUES ($1, $2, $3, $4)
      RETURNING *
    `;

    const result = await pool.query(query, [couponCode, productId, userId, expiresAt]);
    return result.rows[0];
  }

  async validateCoupon(couponCode, productId, userId) {
    const query = `
      SELECT * FROM coupons
      WHERE coupon_code = $1
        AND product_id = $2
        AND user_id = $3
        AND NOT redeemed
        AND expires_at > NOW()
    `;

    const result = await pool.query(query, [couponCode, productId, userId]);
    return result.rows[0] ? true : false;
  }

  async redeemCoupon(couponCode, productId, userId) {
    const query = `
      UPDATE coupons
      SET redeemed = true
      WHERE coupon_code = $1
        AND product_id = $2
        AND user_id = $3
        AND NOT redeemed
        AND expires_at > NOW()
      RETURNING *
    `;

    const result = await pool.query(query, [couponCode, productId, userId]);
    return result.rows[0];
  }
}

module.exports = new CouponService(); 