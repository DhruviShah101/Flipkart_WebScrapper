from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as uReq
def geturl(search,page):
    my_url = "https://www.flipkart.com/search?q={}&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off"
    search = search.replace(" ","+")
    url = my_url.format(search)
    url += f"&page={page}"
    print(url)
    return url

search="Iphone"
index=1
finalCSV = "results.csv"
Flipkart_csv = open(finalCSV,"w")
columns="Model NO.,Name,Price,OriginalPrice,Discount,Ratings,Description\n\n"
Flipkart_csv.write(columns)
Flipkart_csv.close()

for page in range(1,464):
    url=geturl(search,page)
    print(url)
    flipkart_request = uReq(url)
    flipkart_html = flipkart_request.read()
    flipkart_request.close()
    page_soup = soup(flipkart_html, "html.parser")

    containers = page_soup.findAll("div", {"class": "_13oc-S"})
    container = containers[0]

    
    Flipkart_csv=open(finalCSV,"a")

        
    for container in containers:
        product_name=container.div.img["alt"]

        price_container=container.findAll("div", {"class":"_30jeq3 _1_WHN1"})
        price1=price_container[0].text.lstrip('₹')
        price= "Rs. " + price1
        
        originalprice_container=container.findAll("div", {"class":"_3I9_wc _27UcVY"})
        if not originalprice_container:
            originalprice=""
        else:
            originalprice=originalprice_container[0].text.lstrip('₹')
            originalprice= "Rs. " + originalprice

        discperc_container=container.findAll("div", {"class":"_3Ay6Sb"})
        if not discperc_container:
            discperc=""
        else:
            discperc=discperc_container[0].text.lstrip('₹')
            discperc= discperc
        
        rating_container=container.findAll("div",{"class": "_3LWZlK"})
        rating=rating_container[0].text.strip()
        
        description_container=container.findAll("div",{"class": "fMghEO"})
        description=description_container[0].text.strip()
        
        
        print(str(index) + " , " + product_name.replace(","," |") + " , " + price.replace(",","") + " , " + originalprice.replace(",","") + " , " + discperc.replace(",","") + " , " + rating.replace(",","") + " , " + description + "\n")
        Flipkart_csv.write(str(index) + " , " + product_name.replace(","," |") + " , " + price.replace(",","") + " , " + originalprice.replace(",","") + " , " + discperc.replace(",","") + " , " + rating.replace(",","") + " , " + description + "\n")
        
        index=index+1
        
Flipkart_csv.close()