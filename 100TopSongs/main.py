from bs4 import BeautifulSoup as Bs
import requests



def top_100_songs():
    def check_date_info(date_type, date_letter, format_amount):
        date_format = date_letter * format_amount
        date_info = ""
        incorrect = True
        while incorrect:
            date_info = input(f"Please Enter the {date_type} you are looking for in {date_format} format. ")
            if len(date_info) != format_amount:
                print(f"{date_info} is not in the {date_format} format")
                break
            try:
                int(date_info)
                incorrect = False

            except ValueError:
                print("That is not a number")

        return date_info

    def save_html_to_file(file_name="soup-file.html", web_page=""):
        contents = ""
        check_file_name = file_name[-5:]
        # print(check_file_name)
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
        soup_data = Bs(contents, "html.parser")
        return soup_data

    def save_list_to_txt(file_title, file_data, listed_date):
        print(file_data)
        file_title = f"{file_title}.txt"
        new_list = [f"{data['chart']})        Song:  {data['song']}       Artist:{data['artist']}\n"
                    for data in file_data]
        new_list.insert(0, f"Billboard's Top 100 of {listed_date}\n")
        with open(file_title, mode="w") as file:
            file.writelines(new_list)

    year = check_date_info("year", "y", 4)
    month = check_date_info("month", "m", 2)
    day = check_date_info("day", "d", 2)
    date = f"{year}-{month}-{day}"

    source = f"https://www.billboard.com/charts/hot-100/{date}"
    soup = save_html_to_file(file_name=f"top-100_{date}.html", web_page=source)

    top_100 = []
    songs = soup.select("li.o-chart-results-list__item.lrv-u-flex-grow-1.lrv-u-flex.lrv-u-flex-direction-column")
    for index, song in enumerate(songs):
        song_data_pieces = song.getText(separator=": ", strip=True).split(":")
        name = song_data_pieces[0]
        artist = song_data_pieces[1]
        top_100.append({"chart": index + 1, "song": name, "artist": artist})

    save_list_to_txt(date, top_100, date)
    return top_100

