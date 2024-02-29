import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# Load the webpage content
response = requests.get(URL)
website_html = response.text

# Parse the HTML using BeautifulSoup
soup = BeautifulSoup(website_html, "html.parser")

# Find all movie titles on the page
all_movies = soup.find_all(name="h3", class_="title")
movie_titles = [movie.getText() for movie in all_movies]

# Reverse the order of titles (initially from worst to best)
movies = movie_titles[::-1]

# Save the titles to a text file
with open("movies.txt", mode="w") as file:
    for movie in movies:
        file.write(f"{movie}\n")
