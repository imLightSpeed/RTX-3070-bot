from mail import mail
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import logging
from selenium.webdriver.remote.remote_connection import LOGGER

class best_buy:
    def check_stock(self,item, url):
        self.item  = item
        LOGGER.setLevel(logging.WARNING)
        options = Options()
        options.add_argument("--log-level=3")
        options.headless = True
        options.binary_location = GOOGLE_CHROME_PATH
        driver = webdriver.Chrome(CHROMEDRIVER_PATH, options=options)
        try:
            driver.get(url)
            is_instock =  driver.find_element_by_class_name('add-to-cart-button').text
            driver.close()
            driver.quit()
            print(is_instock, item)
            if is_instock == 'Add to Cart':
                x = mail()
                x.send_mail('Best Buy',item)
        except KeyError:
            driver.quit()
class newegg:
    def check_stock(self, item, url):
        self.item  = item
        options = Options()
        options.headless = True
        options.add_argument("--log-level=3")
        options.binary_location = GOOGLE_CHROME_PATH
        driver = webdriver.Chrome(CHROMEDRIVER_PATH, options=options)
        try:
            driver.get(url)
            is_instock =  driver.find_element_by_class_name('product-buy').text
            driver.close()
            driver.quit()
            print(is_instock,item)
            if is_instock == 'ADD TO CART':
                x = mail()
                x.send_mail('NEWEGG',item)
        except KeyError:
             driver.quit()