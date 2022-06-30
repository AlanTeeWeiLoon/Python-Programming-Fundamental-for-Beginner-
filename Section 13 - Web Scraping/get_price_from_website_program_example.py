import bs4, requests

def getPrice(productUrl):
    res = requests.get(productUrl)
    res.raise_for_status()

    soup = bs4.BeautifulSoup(res.text, 'html.parser')
    elems = soup.select('#main > div > div._1Bj1VS > div.page-product > div.container > div.product-briefing.flex.card._2cRTS4 > div.flex.flex-auto.k-mj2F > div > div:nth-child(3) > div > div > div > div')
    return elems[0].text.scrip()


price = getPrice('https://shopee.com.my/G.-SHOCK-Bullbar-DW6900-DW5600-GX56-GW9400-GA110-G9300-G7900-GA2100-i.182791685.5810295620')
print('The price is ' + price )
