#   ____________________________________________________WEB SCRAPING____________________________________________________

from bs4 import BeautifulSoup
# import lxml   # use it when "html.parser" doesn't work

with open("website.html") as file:
    contents = file.read()


soup = BeautifulSoup(contents,"html.parser")
# print(soup)
# print(soup.title)
# print(soup.title.string)
# print(soup.prettify())

# print(soup.a)
# print(soup.li)


all_anchor_tags = soup.find_all(name = "a")
# print(all_anchor_tags)

# for tag in all_anchor_tags:
    # print(tag.getText())
    # print(tag.get("href"))


heading = soup.find(name="h1", id="name")
# print(heading)

section_heading = soup.find(name="h3", class_ = "heading")
# print(section_heading)
# print(section_heading.name)
# print(section_heading.getText())
# print(section_heading.get("class"))


company_url = soup.select_one(selector="p a")
# print(company_url)

# name = soup.select_one(selector="#name")
name = soup.select_one("#name") #works same
# print(name)

headings = soup.select(".heading")
print(headings)
