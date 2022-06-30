from selenium import webdriver
import chromedriver_binary

browser = webdriver.Chrome()
browser.get('https://automatetheboringstuff.com') # cant run with chrome


# To Recap:
# - To import selenium, you need to run: "from selenium import webdriver" (and not "import selenium").
# - To open the browser, run: browser = webdriver.Firefox()
# - To send the browser to a URL, run: browser.get(‘https://inventwithpython.com')
# - The browser.find_elements_by_css_selector() method will return a list of WebElement objects: elems = browser.find_elements_by_css_selector(‘img')
# - WebElement objects have a "text" variable that contains the element's HTML in a string: elems[0].text
# - The click() method will click on an element in the browser.
# - The send_keys() method will type into a specific element in the browser.
# - The submit() method will simulate clicking on the Submit button for a form.
# - The browser can also be controlled with these methods: back(), forward(), refresh(), quit().
