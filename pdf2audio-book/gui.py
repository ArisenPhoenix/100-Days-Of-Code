from tkinter import *
# from tkinter import ttk
BACKGROUND_COLOR = "black"


def start():
    window = Tk()
    window.title('PDF 2 Audiobook')
    window.geometry("1000x1000")
    window.config(padx=50, pady=20, bg=BACKGROUND_COLOR)


def pdf_path(location):
    path = open(location, "rb")
    return path

# front_card = PhotoImage(file=front_card_img)
# flash_card = Canvas(width=800, height=526)
# a_card_img = flash_card.create_image(400, 264, image=front_card)
# flash_card.config(bg=BACKGROUND_COLOR, highlightthickness=0)
# no_button = Button(image=no_button_img, highlightthickness=0, command=show_back_save_pair)
# no_button.grid(row=2, column=1, rowspan=2)