import requests
from bs4 import BeautifulSoup
import smtplib
from time import sleep
import product

# My User Agent
head = ({'User-Agent':'Your user agent should be pasted here. Search for "My user agent" on google to get it.','Accept-Language': 'en-US, en;q=0.5'})

# Taking the URL as input and requesting to the HTTP
url = input("Enter the link of the Product :")
scraper = requests.get(url,headers=head)

# Scraping the content using BeautifulSoup
main = BeautifulSoup(scraper.content,'html5lib')

# Functions are called for the price and name, which are stored in the product module.
true_price = product.price(url,main)
nameofProduct = str(product.name(url,main))

# Print the name of product and current price
print("Product Name :",nameofProduct)
print("Current Price :",true_price)

# Response of the user is taken as input.
response = input("Do you want to be notified when the price fells down (Specify Yes or No) :")
if response == "yes" or response == "Yes" :
    print("Thank You!! You'll be notified when the price drops.")
else :
    exit()

# Sending E-mail if current_price is less than the initial price.
while True :
    curr_price = product.price(url,main)
    if curr_price <= true_price :
        server = smtplib.SMTP('smtp.gmail.com',587)
        server.starttls()
        server.login("email_id","password")
        msg = "Hey!!\n\nPrice of " + nameofProduct + ", has fell down by Rs " + str(true_price-curr_price) + ".\n" 
        link = "Click this link to Purchase it : " + url
        server.sendmail("sender_email","reciever_email",(msg+link))
        server.quit()
    sleep(60)  # 60 seconds sleep
    print("Current Price :",curr_price)
