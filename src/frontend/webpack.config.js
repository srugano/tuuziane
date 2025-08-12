const path = require('path');
const BundleTracker = require('webpack-bundle-tracker');
const { VueLoaderPlugin } = require('vue-loader');
const Dotenv = require('dotenv-webpack');
require('dotenv').config();

const djangoStaticPathName = process.env.VUE_APP_DJANGO_STATIC_PATH_NAME

module.exports = {
  mode: 'development',
  entry: {
    catalogue: './src/catalogue.js',
    registration: './src/registration.js',
    basket: './src/basket.js'
  },
  output: {
    path: path.resolve(__dirname, 'dist/bundles/'),
    filename: '[name]-[contenthash].js',
    publicPath: `/${djangoStaticPathName}/bundles/`,
    clean: true,
  },
  plugins: [
    new BundleTracker({
      path: path.resolve(__dirname, 'dist'),
      filename: 'webpack-stats.json'
    }),
    new VueLoaderPlugin(),
    new Dotenv(),
  ],
  module: {
    rules: [
      {
        test: /\.vue$/,
        loader: 'vue-loader'
      },
      {
        test: /\.css$/,
        use: ['style-loader', 'css-loader']
      }
    ]
  },
  resolve: {
    extensions: ['.js', '.vue'],
    alias: {
      vue$: 'vue/dist/vue.esm-bundler.js'
    }
  }
};
