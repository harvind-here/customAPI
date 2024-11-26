const validateCouponGeneration = (req, res, next) => {
  const { product_id, user_id, validity_period } = req.body;

  if (!product_id || !user_id) {
    return res.status(400).json({
      error: 'Missing required fields: product_id and user_id are required'
    });
  }

  if (validity_period && (isNaN(validity_period) || validity_period <= 0)) {
    return res.status(400).json({
      error: 'validity_period must be a positive number'
    });
  }

  next();
};

const validateCouponOperation = (req, res, next) => {
  const { coupon_code, product_id, user_id } = req.body;

  if (!coupon_code || !product_id || !user_id) {
    return res.status(400).json({
      error: 'Missing required fields: coupon_code, product_id, and user_id are required'
    });
  }

  next();
};

module.exports = {
  validateCouponGeneration,
  validateCouponOperation
}; 