import requests

# Endpoint for accessing the Sheety API
sheety_endpoint = "https://api.sheety.co/fe7000b6f03cfe7edc4aa95b68641cbc/flightDeals/prices"

class DataManager:

    def __init__(self):
        # Dictionary to store destination data
        self.destination_data = {}

    def get_destination_data(self):
        # Fetches destination data from the Sheety API
        response = requests.get(url=sheety_endpoint)
        data = response.json()
        self.destination_data = data["prices"]
        return self.destination_data

    def update_destination_codes(self):
        # Updates destination codes in the Sheety API
        for city in self.destination_data:
            new_data = {
                "price": {
                    "iataCode": city["iataCode"]
                }
            }
            response = requests.put(
                url=f"{sheety_endpoint}/{city['id']}",
                json=new_data
            )
            print(response.text)
