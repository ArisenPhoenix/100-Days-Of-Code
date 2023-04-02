from bs4 import BeautifulSoup as Bs
import requests
import lxml


def save_page_to_html(file_name="soup-file.html", web_page="", page_headers=""):
    contents = ""
    check_file_name = file_name[-5:]
    if check_file_name != ".html":
        return TypeError("The file is not of type .html")
    if web_page == "":
        return TypeError("You Must Enter A Valid Web Address")
    if page_headers == "":
        headers = input("are you sure you don't want to add any headers? \n Y/N")
        if headers.lower() == "y" or headers.lower() == "yes":
            pass
        else:
            return

    def write_to_file(name_of_file):
        with open(name_of_file, mode="w") as html_file:
            res = requests.get(url=web_page, headers=page_headers)
            data = res.text
            html_file.write(data)
            print(data)
            return data

    try:
        with open(file_name) as file:
            contents = file.read()

    except FileNotFoundError or contents == "":
        contents = write_to_file(file_name)

    finally:
        if contents == "":
            contents = write_to_file(file_name)

    soup_data = Bs(contents, "lxml")
    # print(soup_data)
    return soup_data


