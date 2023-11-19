const express = require('express');
const axios = require('axios');

const app = express();
const PORT = 3000;

//setting EJS for view rendering
app.set('view engine', 'ejs');

//using a GET route for the root URL
app.get('/', (req, res) => {
    //render the index view, products are empty
    res.render('index', { products: null });
});

//using a GET route for the load URL
app.get('/load', async (req, res) => {
    try {
        //async HTTP GET request for product fetching
        const response = await axios.get('https://dummyjson.com/products');
        const products = response.data.products;
        res.render('index', { products });
    } catch (err) {
        //error message if request does not succeed
        console.error(err);
        res.status(500).send('Error fetching products.');
    }
});

//Start server on the designated PORT
app.listen(PORT, () => {
    console.log(`Server started on http://localhost:${PORT}`);
});

