from save_page_to_html import save_page_to_html

item_address = "https://www.amazon.com/MSI-GeForce-RTX-3050-8G/dp/B09QB28Y5M/ref=sr_1_4?crid=2JXI3F0YOJ5GS&keywords=Graphics+card&qid=1652488794&sprefix=graphics+ca%2Caps%2C374&sr=8-4"

req_headers = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.64 Safari/537.36",
               "Accept-Language": "en-US,en;q=0.9"
               }
test_address = "https://www.amazon.com/"

file_name = "graphics_card.html"

soup = save_page_to_html(file_name=file_name, web_page=item_address, page_headers=req_headers)
product_title = soup.select_one("span#productTitle").getText()
product_name = product_title.strip(" ")


product_price_info = soup.select_one("span.a-offscreen")
product_price = product_price_info.getText()

price = float(product_price.strip("$"))


product_shipping_details = soup.select_one("span.a-size-base").getText().strip(" ").split(" ")

shipping_price = float(product_shipping_details[0].strip("$"))

product_shipping_text_details = product_shipping_details[1:]
product_shipping_info = " ".join(product_shipping_text_details)
total_price = price + shipping_price

print(product_name)
print(price)
print(shipping_price)
print(product_shipping_info)

print(total_price)
