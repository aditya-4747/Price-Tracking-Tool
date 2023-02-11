
# Function to return the price of the product.
def price(url,main) :
    az = url.find('amazon')
    fk = url.find('flipkart')
    sd = url.find('snapdeal')
    if url[fk:(fk+4)] == 'flip' :
        price = main.find("div",class_="_30jeq3 _16Jk6d")
    elif url[sd:(sd+4)] == 'snap' :
        price = main.find("span",class_="payBlkBig")
    elif url[az:(az+4)] == 'amaz' :
        price = main.find("span",class_="a-price-whole")
        for item in price.strings :
            price = item
            break
    else :
        print("This is not a valid Link of either Amazon/Flipkart/Snapdeal.")
        exit()
    num_price = int((repr(price.string)).replace("₹","").replace(",","").replace("'",""))
    return num_price

# Function to return the name of the product.
def name(url,main) :
    fk = url.find('flipkart')
    sd = url.find('snapdeal')
    if url[fk:(fk+4)] == 'flip' :
        name = main.find("span",class_="B_NuCI")
        for item in name.stripped_strings :
            name = item
            break
        return name
    elif url[sd:(sd+4)] == 'snap' :
        name = main.find("h1",class_="pdp-e-i-head")
        for item in name.stripped_strings :
            name = item
            break
        return name
    else :
        name = main.find("span",id="productTitle")
        for item in name.stripped_strings :
            name = item
            break
        return name
