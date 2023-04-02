import pyttsx3
from PyPDF2 import PdfFileReader
from gui import *
start()
pdf_path = open("DATA_SCIENCE_SYLLABUS.pdf", "rb")
pdf = PdfFileReader(pdf_path)
speak = pyttsx3.init()

mainloop()







# def start():
#     print("starting")
#
#
# def stop():
#     print("stopping")
#     speak.stop()
#
#
# voice = {
#     'age': 100,
#     'gender': 'female',
#     'name': 'Stephanie'
# }
#
#
# from_page = pdf.getPage(0)
# text = from_page.extractText()
#
#
# speak.setProperty('rate', 120)
# v = speak.getProperty('voice')
# voices = speak.getProperty('voices')
# print(v)
# speak.setProperty('gender', voice['gender'])
# speak.setProperty('age', voice['age'])
#
# speak.say(text)
# speak.runAndWait()
# speak.stop()
#
