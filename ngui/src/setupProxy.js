const { createProxyMiddleware } = require("http-proxy-middleware");

module.exports = (app) => {
  app.use(
    "/api/auth/*",
    createProxyMiddleware({
      target: "http://10.128.0.2:8905",
      changeOrigin: true,
      secure: false,
      pathRewrite: {
        "^/api": "/"
      }
    })
  );
  app.use(
    '/api/restapi/*',
    createProxyMiddleware({
      target: "http://10.128.0.2:8999",
      changeOrigin: true,
      pathRewrite: {
        "^/api": "/"
      }
    })
  );
};
