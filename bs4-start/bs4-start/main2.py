from bs4 import BeautifulSoup
import requests

response = requests.get("https://news.ycombinator.com/news")
yc_web_page = response.text

soup = BeautifulSoup(yc_web_page, "html.parser")
# titleline = soup.find(name="span", class_="titleline")
# print(titleline.getText())
#
# link = titleline.find("a")["href"]
# print(link)
#
# score = soup.find(name="span", class_= "score")
# print(score.getText())

# Getting most popular article
articles = soup.find_all("span", class_="titleline")
article_texts = []
article_links = []

for article in articles:
    link_tag = article.find("a")
    article_texts.append(link_tag.getText())
    link = link_tag.get("href")
    article_links.append(link)

article_scores = [int(score.getText().split()[0]) for score in soup.find_all(name="span", class_="score")]


# print(article_texts)
# print(article_links)
# print(article_scores)

# print(int(article_scores[0].split()[0]))

# most popular article will have the highest score
max_score= max(article_scores)
largest_index = article_scores.index(max_score)

# most popular article
print(f"Most popular News:- {article_texts[largest_index]}")
print(f"Link here:- {article_links[largest_index]}")
print(f"Score is {article_scores[largest_index]}")
