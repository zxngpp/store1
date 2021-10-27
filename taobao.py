from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time
driver = webdriver.Chrome()
driver.get("https://www.taobao.com")
driver.maximize_window()
driver.find_element_by_xpath('//*[@id="J_SiteNavLogin"]/div[1]/div[1]/a[1]').click()
driver.find_element_by_xpath('//*[@id="fm-login-id"]').send_keys('17733541571')
driver.find_element_by_xpath('//*[@id="fm-login-password"]').send_keys('zhangxuwning666')
ac = ActionChains(driver)

# 获取滑块
ele=driver.find_element_by_xpath('//*[@id="nc_1__scale_text"]/span')
time.sleep(2)

ac.click_and_hold(ele).move_by_offset(300,0).perform() # perform立即执行

ac.release() # 释放鼠标