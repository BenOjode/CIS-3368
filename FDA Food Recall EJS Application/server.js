// Import modules
const express = require('express');
const axios = require('axios');

// Initialize Express app
const app = express();

// Set EJS as the view engine for rendering
app.set('view engine', 'ejs');

// Parse URL-encoded data (from forms)
app.use(express.urlencoded({ extended: true }));

// Displays the main page with the form
app.get('/', (req, res) => {
    // Render the index ejs view
    res.render('index');
});

// Route to handle form submission (POST request)
app.post('/getData', async (req, res) => {
    // Extract the number of records to fetch from the form input
    const numRecords = req.body.numRecords;

    try {
        // Make a GET request to the FDA API with the specified number of records
        const response = await axios.get(`https://api.fda.gov/food/enforcement.json?search=report_date:[20040101+TO+20131231]&limit=${numRecords}`);

        //Response data extracts only necessary fields and sort by report date
        const recalls = response.data.results.map(r => ({
            product_description: r.product_description,
            reason_for_recall: r.reason_for_recall,
            report_date: r.report_date
        })).sort((a, b) => a.report_date.localeCompare(b.report_date));

        // Render the results view with the fetched recall data
        res.render('results', { recalls });
    } catch (error) {
        // Log the error and send an error message if the request fails
        console.error(error);
        res.send('An error occurred');
    }
});

// Set the port for the server
const PORT = 3000;

// Start the server and listen on the specified port
app.listen(PORT, () => {
    console.log(`Server is running on port ${PORT}`);
});
