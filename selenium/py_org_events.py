from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
driver = webdriver.Chrome(service=Service(ChromeDriverManager(version="latest").install()))


def get_python_upcoming_events_from_events_page():
    driver.get("https://www.python.org/events/python-events/")
    event_names = driver.find_elements(By.CLASS_NAME, value="event-title")
    event_locations = driver.find_elements(By.CLASS_NAME, value="event-location")
    event_times = driver.find_elements(By.TAG_NAME, value="time")
    event_list = []

    for index in range(len(event_names)):
        print(event_times[index].text)
        event_list.append({index: {"name": event_names[index].text,
                                   "time": event_times[index].text},
                           "location": event_locations[index].text})

    driver.close()
    driver.quit()
    return event_list


def get_python_upcoming_events_from_main_page():
    driver.get("https://www.python.org/")
    event_div = driver.find_element(By.CLASS_NAME, value="event-widget").find_elements(By.TAG_NAME, value="li")
    raw_event_data = [event.text for event in event_div]

    events = []
    for event in raw_event_data:
        name, time = event.split("\n")
        events.append({"name": name, "time": time})
    driver.quit()
    return events


def interaction():
    driver.get("https://en.wikipedia.org/wiki/Main_Page")
    search = driver.find_element(By.NAME, "search")
    search.send_keys("Python")
    search.send_keys(Keys.ENTER)


def secure_retreat_login():
    driver.get("https://secure-retreat-92358.herokuapp.com/")
    driver_find = driver.find_element

    f_name = driver_find(By.NAME, "fName")
    f_name.send_keys("Brandon")

    l_name = driver_find(By.NAME, "lName")
    l_name.send_keys("Michael")

    email = driver_find(By.NAME, "email")
    email.send_keys("brandon_michael@com.com")

    send = driver_find(By.CLASS_NAME, "btn")
    send.send_keys(Keys.ENTER)


