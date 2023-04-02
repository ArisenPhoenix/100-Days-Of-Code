from bs4 import BeautifulSoup
import requests

contents = ""
try:
    with open("soup-file.html") as file:
        contents = file.read()

except FileNotFoundError or contents == "":
    with open("soup-file.html", mode="w") as file:
        response = requests.get("https://news.ycombinator.com/news")
        contents = response.text
        file.write(contents)

finally:
    if contents == "":
        with open("soup-file.html", mode="w") as file:
            response = requests.get("https://news.ycombinator.com/news")
            contents = response.text
            file.write(contents)

    soup = BeautifulSoup(contents, "html.parser")

articles = soup.find_all(name="a", class_="titlelink")
article_texts = []
article_links = []
for article in articles:
    text = article.getText()
    link = article.get("href")
    article_texts.append(text)
    article_links.append(link)

article_upvote_data = soup.find_all(name="span", class_="score")
article_upvotes = [int(score.getText().split(" ")[0]) for score in article_upvote_data]

largestNum = max(article_upvotes)
largestIndex = article_upvotes.index(largestNum)

print(article_texts[largestIndex])
print(article_links[largestIndex])


















