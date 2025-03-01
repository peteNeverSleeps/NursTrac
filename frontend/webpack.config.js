// webpack.config.js
const path = require('path');
const HtmlWebpackPlugin = require('html-webpack-plugin');

module.exports = {
  // The entry file where your app starts
  entry: './src/index.js',

  // Where Webpack outputs the bundles and assets
  output: {
    path: path.resolve(__dirname, '../backend/nursTrac/static/frontend'),
    filename: 'bundle.js',
    publicPath: '/',
    clean: true, // optional, cleans 'dist' on each build
  },

  // Set the mode to 'development' (or 'production' for a production build)
  mode: 'development',

  // Configuration for the development server
  devServer: {
    static: {
      directory: path.join(__dirname, 'dist'),
    },
    port: 3000,
    open: true,         // opens the browser automatically
    hot: true,          // enables hot module replacement
    historyApiFallback: true, // supports client-side routing
  },

  module: {
    rules: [
      {
        // Transpile JS and JSX files using Babel
        test: /\.(js|jsx)$/,
        exclude: /node_modules/,
        use: {
          loader: 'babel-loader',
          options: {
            // Babel presets for modern JS and React
            presets: [
              '@babel/preset-env',
              '@babel/preset-react'
            ]
          }
        }
      },
      {
        // Load and bundle CSS files
        test: /\.css$/,
        use: ['style-loader', 'css-loader']
      }
    ]
  },

  // Allows importing JS/JSX without specifying extensions
  resolve: {
    extensions: ['.js', '.jsx']
  },

  // Generate an HTML file that includes your bundles
  plugins: [
    new HtmlWebpackPlugin({
      template: './public/index.html', // Make sure you have this file
      filename: 'index.html'
    })
  ],
};
