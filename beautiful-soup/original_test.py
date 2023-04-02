from bs4 import BeautifulSoup
import requests
import os
dirname = os.getcwd()
print(dirname)


with open("website.html") as file:
    contents = file.read()

soup = BeautifulSoup(contents, "html.parser")
# print(soup.prettify())
# print(soup.title)
# print(soup.title.string)

all_anchor_tags = soup.find_all(name="a")
# print(all_anchor_tags)

# for tag in all_anchor_tags:
#     print(tag.getText())
#     print(tag.get("href"))
#
# heading = soup.find(name="h1", id="name")
# print(heading)

# section_heading = soup.find(name="h3", class_="heading")
# print(section_heading.get("class"))
#
company_url = soup.select_one("p a")
print(company_url)
#
# class_is_heading = soup.find_all(class_="heading")
#
# name = soup.select_one("#name")
# print(name)
#
# a_class = soup.select_one(".heading")
# print(a_class)
#
# headings = soup.select(".heading")
# print(headings)