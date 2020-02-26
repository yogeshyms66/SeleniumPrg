#Write a script to click on enter without using the click method
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
filepath=r"E:\SeleniumPrg\drivers\chromedriver.exe"
driver=webdriver.Chrome(executable_path=filepath)
driver.get("https://demo.actitime.com/login.do")
driver.find_element_by_xpath("//input[@id='username']").send_keys("admin")
driver.find_element_by_xpath("//input[@name='pwd']").send_keys("manager")
driver.find_element_by_xpath("//a[@id='loginButton']").send_keys(Keys.ENTER)
driver.quit()
