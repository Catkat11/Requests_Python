import requests  # Importing the requests module

# Endpoint for the Sheety API
sheety_endpoint = "https://api.sheety.co/fe7000b6f03cfe7edc4aa95b68641cbc/flightDealsUsers/users"

# Function to post a new row of data to the Sheety endpoint
def post_new_row(first_name, last_name, email):
    # Creating the body of the request with user data
    body = {
        "user": {
            "firstName": first_name,
            "lastName": last_name,
            "email": email,
        }
    }

    # Sending a POST request to the Sheety endpoint with the user data
    response = requests.post(url=sheety_endpoint, json=body)
    response.raise_for_status()  # Checking for errors in the response
    print(response.text)  # Printing the response text
