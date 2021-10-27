from selenium import webdriver
driver = webdriver.Chrome()
driver.get("https://www.bilibili.com")
driver.maximize_window()
driver.implicitly_wait(4)
driver.find_element_by_xpath('//*[@id="internationalHeader"]/div[1]/div/div[3]/div[2]/span[1]/div/span/div').click()
date=driver.window_handles
driver.switch_to.window(date[1])

driver.find_element_by_xpath('//*[@id="login-username"]').send_keys('17733541571')
driver.find_element_by_xpath('//*[@id="login-passwd"]').send_keys('zhangxuening666')
driver.find_element_by_xpath('//*[@id="geetest-wrap"]/div/div[5]/a[1]').click()


