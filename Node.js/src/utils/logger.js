const { pool } = require('../config/database');

class Logger {
  async logApiRequest(endpoint, requestData, responseData) {
    const query = `
      INSERT INTO api_logs (endpoint, request_data, response_data)
      VALUES ($1, $2, $3)
      RETURNING id
    `;

    try {
      await pool.query(query, [endpoint, requestData, responseData]);
    } catch (error) {
      console.error('Error logging API request:', error);
      // Don't throw the error to prevent affecting the main operation
    }
  }
}

module.exports = new Logger(); 