For this project you will need to call the API provided by dummyjson to query products.
In particular, we will use this endpoint:
https://dummyjson.com/products

This REST endpoint responds with a JSON response that contains some mocked up products with
various attributes of information. We are in particular interested in three attributes: The product's title,
the price, and the discount percentage:
We are interested in listing all the items on a page, displaying their name, price, discount in %, and
the calculated final price, as soon as a user presses the LOAD button. Note: All this info should not
be shown before the LOAD button is pressed!

Naturally we don't want to present the user with JSON formatted data, so you will need to present the
JSON data to the user in readable and formatted HTML (e.g. in individual labels, in form of a list, as
individual paragraphs, etc.) The presentation choice is yours.
The user should see a headline on the website stating that this is a website to list all inventory products
and their prices. Beneath there should be the button that says “Load”.
