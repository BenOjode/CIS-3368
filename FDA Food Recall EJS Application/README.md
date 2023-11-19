Create an EJS application that utilizes the following given REST API, which returns FDA food recall
information (recalled products). We want to see some of those recall reasons on a web application. We are only
interested in the properties for "product_description" and "reason_for_recall" of the JSON response.

The following endpoint can be used to request list of 5 FDA food recalls:
https://api.fda.gov/food/enforcement.json?search=report_date:[20040101+TO+20131231]&limit=5
Use a JSON formatter to better visualize your response (for instance here or here)

UI REQUIREMENTS:
When the page loads, there should be nothing on the page except for a text box, and one button that says:
“Retrieve Data”.
The user needs to enter a number between 1 and 5 in the textbox. (You do not have to check for wrong user
inputs). When the user clicks the button, the page should make the API call to retrieve the FDA records.
We are interested to see the product description, and the reason for the recall of however many products the
user wants to see (1, 2, 3, 4, or 5). No other data needs to be displayed.

There is a property on every recall named "report_date" . For the extra credit, you need to sort the displayed
recalls by their report date, in ascending order.
So for instance, a report made in July 2012 should be displayed before a report made in October 2013.

Technical requirements:
You must use EJS as your JavaScript Framework, and utilize the libraries learned in the course such as express,
and axios. You're welcome to use additional libraries as you choose.


