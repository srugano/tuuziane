const path = require('path');
const webpack = require('webpack');
const BundleTracker = require('webpack-bundle-tracker');
const { VueLoaderPlugin } = require('vue-loader');

const djangoStaticPathName = process.env.STATIC_PATH_NAME || 'static';

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
    new webpack.DefinePlugin({
      __VUE_OPTIONS_API__: JSON.stringify(true),
      __VUE_PROD_DEVTOOLS__: JSON.stringify(false),
      __VUE_PROD_HYDRATION_MISMATCH_DETAILS__: JSON.stringify(false)
    }),
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
