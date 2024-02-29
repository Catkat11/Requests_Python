import requests
from datetime import datetime

# Pixela endpoint for user creation
pixela_endpoint = "https://pixe.la/v1/users"

# User data
USERNAME = "lukaszz"
TOKEN = "jdkasnvijrniauovnakjdsvn"

# Graph ID
ID = "graph1"

# User parameters for creating a new user
user_params = {
    "token": TOKEN,
    "username": USERNAME,
    'agreeTermsofService': "yes",
    "notMinor": "yes",
}

# Graph endpoint for creating a new graph
graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

# Graph configuration
graph_config = {
    "id": ID,
    "name": "Coding graph",
    "unit": "Hours",
    "type": "float",
    "color": "momiji",
}

# Headers containing user token
headers = {
    "X-USER-TOKEN": TOKEN
}

# Uncomment to create a new graph
# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)

# Pixela endpoint for posting data to the graph
post_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{ID}"

# Get today's date
today = datetime.now()

# Configuration for posting data to the graph
post_config = {
    "date": today.strftime("%Y%m%d"),
    "quantity": input("How many hours did you code today?"),
}

# Post data to the graph
response = requests.post(url=post_endpoint, json=post_config, headers=headers)
print(response.text)

# Uncomment to update data in the graph
# put_endpoint = f"{post_endpoint}/{today.strftime('%Y%m%d')}"
# put_config = {
#     "quantity": "2.5",
# }
# response = requests.put(url=put_endpoint, json=put_config, headers=headers)
# print(response.text)

# Uncomment to delete data from the graph
# response = requests.delete(url=put_endpoint, headers=headers)
# print(response.text)
