const path =  require('path');
const autoprefixer  = require('autoprefixer');
const HtmlWebpackPlugin = require('html-webpack-plugin');

module.exports = {
    mode: 'development',
    entry: {
        cards: './src/cards/CardsDisplay.js',
        cardDetail: './src/cardDetail/CardDetail.js',
        search: './src/search/search.js',
        searchBar: './src/search/SearchBar/SearchBar.js',
        userCards: './src/userCards/UserCards.js',
        decksRec: './src/decksRec/DecksRec.js'
    },
    watch: true,
    output: {
        filename: '[name].js',
        path: __dirname + 'dist'
    },
    devtool: 'source-map',
    module: {
        rules: [
            {
                test: /\.js$/,
                loader: 'babel-loader',
                exclude: /node_modules/
            },
            {
                test: /\.css$/,
                exclude: /node_modules/,
                use: [
                    {loader: 'style-loader'},
                    {
                        loader: 'css-loader',
                        options: {
                            importLoaders: 1,
                            modules: {
                                localIdentName: '[name]__[local]__[hash:base64:5]'
                            }
                        }
                    },
                    {
                        loader: 'postcss-loader',
                        options:{
                            ident: 'postcss',
                            plugins: () => [autoprefixer()]
                        }
                    }
                ]
            }

        ]
    }
    // plugins: [
    //     new HtmlWebpackPlugin({
    //         template:
    //     })
    // ]
};