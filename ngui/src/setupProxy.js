const { createProxyMiddleware } = require("http-proxy-middleware");

module.exports = (app) => {
  app.use(
    "/api/auth/*",
    createProxyMiddleware({
      target: "http://auth.optscale.svc.cluster.local:8905",
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
      target: "http://rest-api-server.optscale.svc.cluster.local:8999",
      changeOrigin: true,
      pathRewrite: {
        "^/api": "/"
      }
    })
  );
};
