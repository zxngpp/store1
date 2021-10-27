from selenium import webdriver

from selenium.webdriver.common.action_chains import ActionChains
import time
driver = webdriver.Chrome()


driver.get("https://www.jd.com")
driver.maximize_window()


driver.find_element_by_xpath('//*[@id="ttbar-login"]').click()
driver.find_element_by_xpath('//*[@id="content"]/div[2]/div[1]/div/div[3]').click()
driver.find_element_by_xpath('//*[@id="loginname"]').send_keys('17733541571')
driver.find_element_by_xpath('//*[@id="nloginpwd"]').send_keys('zhangxuening666')
driver.find_element_by_xpath('//*[@id="loginsubmit"]').click()
ele=driver.find_element_by_xpath('//*[@id="JDJRV-wrap-loginsubmit"]/div/div/div/div[1]/div[2]/div[1]/img')
ac = ActionChains(driver)

ac.click_and_hold(ele).move_by_offset(198,0).perform() # perform立即执行
ac.release() # 释放鼠标