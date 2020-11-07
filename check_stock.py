from mail import mail
import os
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import logging
from selenium.webdriver.remote.remote_connection import LOGGER
from selenium.common.exceptions import NoSuchElementException
import threading
from threading import Thread
class stock(Thread):
    def __init__(self, item, url):
        Thread.__init__(self)
        self.item = item
        self.url =url
        
    def best_buy(self):
        self.html_class  = 'add-to-cart-button'
        self.store_name = 'Best Buy'
        self.cart = 'Add to Cart'
    def newegg(self):
        self.html_class  = 'product-buy'
        self.store_name = 'Newegg'
        self.cart = 'ADD TO CART'
        
    def run(self):
        url = self.url
        item = self.item
        # options = Options()
        # options.headless = True
        # PATH = "chromedriver.exe"
        # driver = webdriver.Chrome(PATH, options=options)
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument('--headless')
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--disable-dev-shm-usage')
        driver = webdriver.Chrome(chrome_options=chrome_options)
        try:
            driver.get(self.url)
            time.sleep(6)
            is_instock =  driver.find_element_by_class_name(self.html_class).text
            driver.close()
            driver.quit()
            print(is_instock, self.item)
            if is_instock == self.cart:
                x = mail()
                x.send_mail(self.store_name,self.item)
        except NoSuchElementException:
            print('NoSuchElementException', self.item)
            driver.quit()
def main(bb, ne):
    threads = []
    for key,value in bb.items():
        t1 = stock(key,value)
        t1.best_buy()
        t1.start()
        threads.append(t1)
    for i in threads:
        i.join()
    threads = []
    for key,value in ne.items():
        t1 = stock(key,value)
        t1.newegg()
        t1.start()
        threads.append(t1)
    for i in threads:
        i.join()
