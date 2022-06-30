# beautiful soup module

import bs4
import requests

res = requests.get('https://shopee.com.my/G.-SHOCK-Bullbar-DW6900-DW5600-GX56-GW9400-GA110-G9300-G7900-GA2100-i.182791685.5810295620')

print(res.raise_for_status()) # None - everything is OK

soup = bs4.BeautifulSoup(res.text, 'html.parser')

print(soup)

a = soup.select('#main > div > div._1Bj1VS > div.page-product > div.container > div.product-briefing.flex.card._2cRTS4 > div.flex.flex-auto.k-mj2F > div > div:nth-child(3) > div > div > div > div')

print(a) # cant put the content inside the list


#To recap:
# - Web pages are plaintext files formatted as HTML.
# - HTML can be parsed with the BeautifulSoup module.
# - BeautifulSoup is imported with the name bs4.
# - Pass the string with the HTML to the bs4.BeautfiulSoup() function to get a Soup object.
# - The Soup object has a select() method that can be passed a string of the CSS selector for an HTML tag.
# - You can get a CSS selector string from the browser's developer tools by right-clicking the element and selecting Copy 'Selector'.
# - The select() method will return a list of matching Element objects.

