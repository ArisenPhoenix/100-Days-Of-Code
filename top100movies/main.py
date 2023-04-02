from bs4 import BeautifulSoup as Bs
import requests
import lxml


def save_html_to_file(file_name="soup-file.html", web_page=""):
    contents = ""
    check_file_name = file_name[-5:]
    if check_file_name != ".html":
        return TypeError("The file is not of type .html")
    if web_page == "":
        return TypeError("You Must Enter A Valid Web Address")

    try:
        with open(file_name) as file:
            contents = file.read()

    except FileNotFoundError or contents == "":
        with open(file_name, mode="w") as file:
            response = requests.get(web_page)
            contents = response.text
            file.write(contents)

    finally:
        if contents == "":
            with open(file_name, mode="w") as file:
                response = requests.get(web_page)
                contents = response.text
                file.write(contents)

    send_soup = Bs(contents, "html.parser")
    return send_soup


source = "https://www.empireonline.com/movies/features/best-movies-2/"
soup = save_html_to_file("top_100_movies.html", source)

movie_numbers = soup.find_all("span", class_="jsx-4245974604 listicle-item-count")


print(movie_numbers)
movie_name = soup.find_all(name="h3", class_="jsx-4245974604")
print(movie_name)
# for i in range(len(movie_name) - 1, 100, 1):
#     print(movie_name[i])
# print(movie_name)
#
# print(movie_name)
