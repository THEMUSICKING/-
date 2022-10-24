import time

from selenium import webdriver
import pytest
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome('chromedriver.exe')

url = 'https://train.qunar.com/'

driver.get(url)
driver.maximize_window()


driver.find_element(By.XPATH, '//*[@id="js-con"]/div[1]/form/div[1]/div[1]/div[1]/div/div/input').send_keys('上海南')
time.sleep(1)
driver.find_element(By.XPATH, '//*[@id="js-con"]/div[1]/form/div[1]/div[1]/div[2]/div/div/input').send_keys('太原南')
time.sleep(1)
driver.find_element('name','date').click()
driver.find_element('name','date').send_keys(Keys.CONTROL+'A')
driver.find_element('name', 'date').send_keys('2022-10-29')
time.sleep(1)
driver.find_element('name','date').click()
driver.find_element('name', 'stsSearch').click()
time.sleep(1)
driver.find_element(By.XPATH, '//*[@id="list_listInfo"]/ul[2]/li[1]/div/div[7]/a[1]/span').click()
time.sleep(3)
# driver.find_element(By.XPATH, '//*[@id="fillOrder_passengerInfo"]/div[2]/div/div/ul/li[1]/div/label').
time.sleep(1)
driver.find_element(By.XPATH, '//*[@id="fillOrder_passengerInfo"]/div[2]/div/div/ul/li[1]/div/input').send_keys('金欢')
driver.find_element(By.XPATH, '//*[@id="fillOrder_passengerInfo"]/div[2]/div/div/ul/li[2]/div[1]/div[2]/input').send_keys('342425200110020156')
driver.find_element(By.XPATH, '//*[@id="fillOrder_contactInfo"]/div[2]/div[1]/input').send_keys('金欢')
driver.find_element(By.XPATH, '//*[@id="fillOrder_contactInfo"]/div[2]/div[2]/input').send_keys('16655467002')
time.sleep(1)
driver.find_element(By.XPATH, '//*[@id="eTicketSubmit"]').click()

time.sleep(3)

