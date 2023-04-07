import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"
response = requests.get(URL)
website_html = response.text
soup = BeautifulSoup(website_html, "html.parser")
# print(soup)

all_movies = soup.findAll(name="h3", class_="title")
movie_titles = [movie.getText() for movie in reversed(all_movies)]

with open("movies.txt", mode="w", encoding="utf-8") as file:
    for movie in movie_titles:
        print(movie)
        file.write(f"{movie}\n")
