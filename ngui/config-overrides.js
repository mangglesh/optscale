module.exports = function override (config, env) {
  let loaders = config.resolve
  loaders.fallback = {
      "fs": false,
      "tls": false,
      "net": false,
      "https": false,
      "buffer": false,
      "stream": false,
      "crypto": require.resolve("crypto-browserify")
  }
  
  return config
}