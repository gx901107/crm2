from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()
driver.maximize_window()
driver.get('http://192.168.1.213/crm')
username_locator = (By.NAME, "name")
password_locator = (By.NAME, 'password')
submit_locator = (By.NAME, 'submit')
clue_locator = (By.LINK_TEXT,'线索')
client_locator = (By.CSS_SELECTOR,'body > div.navbar.navbar-inverse.navbar-fixed-top > div > div > div.nav-collapse.collapse > ul:nth-child(1) > li:nth-child(2) > a')
opportunity_locator = (By.CSS_SELECTOR, 'body > div.navbar.navbar-inverse.navbar-fixed-top > div > div > div.nav-collapse.collapse > ul:nth-child(1) > li:nth-child(3) > a')

driver.find_element(*username_locator).send_keys('xiaoyang')
driver.find_element(*password_locator).send_keys('123456')
driver.find_element(*submit_locator).click()




sleep(4)
driver.quit()