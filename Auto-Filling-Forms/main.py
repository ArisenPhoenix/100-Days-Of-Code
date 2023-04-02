from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.common.action_chains import ActionChains
import time

service = Service(ChromeDriverManager(version="latest").install())
chrome_driver_location = "/home/merk/.wdm/drivers/chromedriver/linux64/101.0.4951.41/chromedriver"
# driver = webdriver.Chrome(service=service)
driver = webdriver.Chrome(service=service)

hover = ActionChains(driver).move_to_element


# def buy_what(list_of_products):
#     for a_product in list_of_products:
#         price = a_product["price"]

    
def countdown(t):
    while t:
        minutes, secs = divmod(t, 60)
        timer1 = '{:02d}:{:02d}'.format(minutes, secs)
        print(timer1, end="\r")
        time.sleep(1)
        t -= 1
        if t == 0:
            return 0


def get_product_info(a_product):
    million = 1000000
    billion = million * 1000
    trillion = billion * 1000
    multiplier_dict = {"million": million, "billion": billion, "trillion": trillion}
    
    multiplier = 1
    product_details = a_product.split()
    if len(product_details) > 2:
        for key in multiplier_dict:
            print(key)
            value = multiplier_dict[key]
            if product_details[2] == key:
                multiplier = value
                print(f"multiplier is: {value}")
                break
        product_dictionary = {
            "name": product_details[0], "price":
                transform_to_num(product_details[1].replace(",", "").replace(".", ""), multiplier)
        }
    
    else:
        product_dictionary = {
            "name": product_details[0], "price":
                transform_to_num(product_details[1].replace(",", "").replace(".", ""))
        }

    return product_dictionary
        
        
def transform_to_num(num_cookies, multiplier=1):
    
    try:
        number = float(num_cookies.split()[0]) * multiplier
    except ValueError:
        number = float(num_cookies.split()[0].replace(",", "").replace(".", "")) * multiplier
    return number


location = "https://orteil.dashnet.org/cookieclicker/"
driver.get(location)


def get_products():
    print("in get_products")
    list_of_products = []
    for i in range(20):
        try:
            item = driver.find_element(By.ID, f"product{i}")
            list_of_products.append(item)

        except:
            break
    return list_of_products


lang = WebDriverWait(driver, 10).until(ec.element_to_be_clickable((By.ID, "langSelect-EN"))).click()
cookieB = driver.find_element(By.ID, "bigCookie")
countdown(3)

start_time = time.time()

seconds = 10
playing = True
products = get_products()

while playing:
    current_time = time.time()
    elapsed_time = current_time - start_time
    cookies = driver.find_element(By.ID, "cookies").text
    cps = ""

    try:
        cookieB.click()
        cps = driver.find_element(By.ID, "cookiesPerSecond").text
        
    except StaleElementReferenceException:
        continue
    finally:
        seen_products = []
        if elapsed_time > seconds:
            for product in products:
                if product.is_displayed():
                    seen_products.append(product)
                    # hover(product).perform()
            
            products_can_buy = []
            for index, product in enumerate(seen_products):
                data = get_product_info(product.text)
                product_name = data["name"]
                product_price = data["price"]
                
                if product_price < transform_to_num(cookies):
                    products_can_buy.append(product)
                start_time = time.time()
            
            toBuy = ""
            total = 0
            for product in products_can_buy:
                price = get_product_info(product.text)["price"]
                if price > total:
                    total = price
                
                toBuy = product
            
            if toBuy == "":
                continue
            else:
                toBuy.click()
