from datetime import datetime, date, timedelta
from selenium import webdriver
from selenium.webdriver.common.by import By


def date_n(n):
    return str(date.today() + timedelta(days=int(n)))

driver = webdriver.Chrome('../chromedriver.exe')

def find(element):
    return driver.find_element(By.CSS_SELECTOR, element)

def byname(element):
    return driver.find_element('name', element)

def get_driver():
    return driver

def xpath(element):
    return driver.find_element(By.XPATH, element)

def open(url):
    driver.get(url)
    driver.maximize_window()

def close():
    driver.quit()