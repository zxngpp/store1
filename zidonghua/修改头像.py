from selenium import webdriver
import  time
driver=webdriver.Chrome()
driver.get("http://www.localhost:8080/HKR")
driver.maximize_window()
driver.find_element_by_xpath("//*[@id='loginname']").send_keys("jason")
driver.find_element_by_xpath("//*[@id='password']").send_keys("1234567")
driver.find_element_by_xpath('//*[@id="submit"]').click()
driver.find_element_by_xpath('//*[@id="img"]').click()
time.sleep(3)
driver.find_element_by_xpath('//*[@id="ul_pic"]/li[5]/img').click()


