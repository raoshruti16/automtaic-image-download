# -*- coding: utf-8 -*-
"""
Created on Mon Jul  6 21:29:53 2020

@author: shruti
"""

from selenium import webdriver
import time
import urllib.request

options = webdriver.ChromeOptions()
options.add_argument("--headless") 
driver = webdriver.Chrome('C:\chromedriver_win32\chromedriver', options=options)
time.sleep(1)

driver.get('https://unsplash.com/t/architecture')
time.sleep(1)

i = 1

unsplash = driver.find_element_by_xpath('//*[@id="app"]/div/div[3]/div[2]')
wallpapers = unsplash.find_elements_by_css_selector('img._2VWD4._2zEKz')
for images in wallpapers:
    urllib.request.urlretrieve(images.get_attribute('src'),"{}.jpg".format(i))
    i+=1
