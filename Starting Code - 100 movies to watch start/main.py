import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# Write your code below this line 👇

response = requests.get(URL)
website_html = response.text

soup = BeautifulSoup(website_html, "html.parser")

all_movies = soup.find_all(name="h3", class_="title")
# print(all_movies)

movie_titles  = [movie.getText() for movie in all_movies]
# print(movie_titles)


#reverse the order of the list
movies = movie_titles[::-1]
# OR,
# for n in range(len(movie_titles)-1, -1, -1):
#     print(movie_titles[n])

with open("movies.txt", mode="w", encoding="utf-8") as file:
    for movie in movies:
        file.write(f"{movie}\n")