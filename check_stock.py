from mail import mail
import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import logging
from selenium.webdriver.remote.remote_connection import LOGGER

class best_buy:
    def check_stock(self,item, url):
        self.item  = item
        LOGGER.setLevel(logging.WARNING)
        options = Options()
        options.headless = True
        #Bellow is for heroku
        options.add_argument("--log-level=3")
        options.add_argument("-- disable-gpu")
        options.add_argument("-- no-sandbox")
        CHROMEDRIVER_PATH = "/app/.chromedriver/bin/chromedriver"
        chrome_bin = os.environ.get("GOOGLE_CHROME_BIN", "chromedriver")
        # PATH = "chromedriver.exe"
        # driver = webdriver.Chrome(PATH, options=options)
        driver = webdriver.Chrome(executable_path=CHROMEDRIVER_PATH, options=options)
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
        LOGGER.setLevel(logging.WARNING)
        options = Options()
        options.headless = True
        #Bellow is for heroku
        options.add_argument("--log-level=3")
        options.add_argument("-- disable-gpu")
        options.add_argument("-- no-sandbox")
        CHROMEDRIVER_PATH = "/app/.chromedriver/bin/chromedriver"
        chrome_bin = os.environ.get("GOOGLE_CHROME_BIN", "chromedriver")
        # PATH = "chromedriver.exe"
        # driver = webdriver.Chrome(PATH, options=options)
        driver = webdriver.Chrome(executable_path=CHROMEDRIVER_PATH, options=options)
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