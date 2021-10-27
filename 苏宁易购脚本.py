from selenium import webdriver
import time
driver = webdriver.Chrome()

driver.get(r"https://www.suning.com")

driver.maximize_window()
driver.find_element_by_xpath('//*[@id="reg-bar-node"]/a[1]').click()

driver.find_element_by_xpath('/html/body/div[2]/div[1]/div/div[1]/a[2]/span').click()
date = driver.window_handles
driver.switch_to.window(date[0])
driver.find_element_by_xpath('//*[@id="userName"]').send_keys('17733541571')
driver.find_element_by_xpath('//*[@id="password"]').send_keys('zhangxuening666')
driver.find_element_by_xpath('//*[@id="submit"]').click()
time.sleep(3)
driver.find_element_by_xpath('//*[@id="iar1_sncaptcha_button"]/span').click()
