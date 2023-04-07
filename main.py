import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"
response = requests.get(URL)
web_page = response.text
soup = BeautifulSoup(web_page, "html.parser")
# print(soup)

movies = soup.findAll(name="h3", class_="title")

with open("movies.txt", mode="a") as file:
    for movie in reversed(movies):
        print(movie.getText())
        file.write(f"{movie.getText()}\n")
