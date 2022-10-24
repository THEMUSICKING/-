import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from qunaer.base_code import *

def book_ticket(start, end, n, name, id,mobile):
    open('https://train.qunar.com/')
    action = ActionChains(driver)
    byname('fromStation').send_keys(start)
    action.move_by_offset(0,0)
    action.click()
    action.perform()

    byname('toStation').send_keys(end)
    action.move_by_offset(0, 0)
    action.click()
    action.perform()

    date_1 = date_n(n)

    byname('date').send_keys(Keys.CONTROL, "a")
    byname("date").send_keys(Keys.BACKSPACE)
    byname('date').send_keys(date_1)
    byname('date').click()

    byname('stsSearch').click()
    time.sleep(2)

    xpath('//*[@id="list_listInfo"]/ul[2]/li[1]/div/div[7]/a[1]/span').click()
    time.sleep(1)

    xpath('//*[@id="fillOrder_passengerInfo"]/div[2]/div/div/ul/li[1]/div/input').send_keys(name)
    xpath('//*[@id="fillOrder_passengerInfo"]/div[2]/div/div/ul/li[2]/div[1]/div[2]/input').send_keys(id)
    xpath('//*[@id="fillOrder_contactInfo"]/div[2]/div[1]/input').send_keys(name)
    xpath('//*[@id="fillOrder_contactInfo"]/div[2]/div[2]/input').send_keys(mobile)
    time.sleep(1)
    find('.g-btn02').click()
    time.sleep(5)

    close()