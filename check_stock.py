from mail import mail
import os
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import logging
from selenium.webdriver.remote.remote_connection import LOGGER
from selenium.common.exceptions import NoSuchElementException

class best_buy:
    def check_stock(self,item, url):
        self.item  = item
        LOGGER.setLevel(logging.WARNING)
        options = Options()
        options.headless = True
        #Bellow is for heroku
        chrome_options = webdriver.ChromeOptions()
        chrome_options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--disable-dev-shm-usage")
        chrome_options.add_argument("--no-sandbox")
        # PATH = "chromedriver.exe"
        # driver = webdriver.Chrome(PATH, options=options)
        driver = webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"), chrome_options=chrome_options)
        try:
            driver.get(url)
            time.sleep(5)
            is_instock =  driver.find_element_by_class_name('add-to-cart-button').text
            driver.close()
            driver.quit()
            print(is_instock, item)
            if is_instock == 'Add to Cart':
                x = mail()
                x.send_mail('Best Buy',item)
        except NoSuchElementException:
            print(NoSuchElementException)
            driver.quit()
class newegg:
    def check_stock(self, item, url):
        self.item  = item
        LOGGER.setLevel(logging.WARNING)
        options = Options()
        options.headless = True
        #Bellow is for heroku
        chrome_options = webdriver.ChromeOptions()
        chrome_options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--disable-dev-shm-usage")
        chrome_options.add_argument("--no-sandbox")
        # PATH = "chromedriver.exe"
        # driver = webdriver.Chrome(PATH, options=options)
        driver = webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"), chrome_options=chrome_options)
        try:
            driver.get(url)
            time.sleep(5)
            is_instock =  driver.find_element_by_class_name('product-buy').text
            driver.close()
            driver.quit()
            print(is_instock,item)
            if is_instock == 'ADD TO CART':
                x = mail()
                x.send_mail('NEWEGG',item)
        except NoSuchElementException:
            print(NoSuchElementException)
            driver.quit()