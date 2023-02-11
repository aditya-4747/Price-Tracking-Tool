import requests
from bs4 import BeautifulSoup
import smtplib
from time import sleep
import product

head = ({'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36','Accept-Language': 'en-US, en;q=0.5'})

url = input("Enter the link of the Product :")
scraper = requests.get(url,headers=head)

main = BeautifulSoup(scraper.content,'html5lib')


true_price = product.price(url,main)
nameofProduct = str(product.name(url,main))
print("Product Name :",nameofProduct)
print("Current Price :",true_price)
response = input("Do you want to be notified when the price fells down (Specify Yes or No) :")
if response == "yes" or response == "Yes" :
    print("Thank You!! You'll be notified when the price drops.")
else :
    exit()


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
