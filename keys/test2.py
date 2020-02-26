#Write a script to clear the text entered in text box without using the clear metho
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
filepath=r"E:\SeleniumPrg\drivers\chromedriver.exe"
driver=webdriver.Chrome(executable_path=filepath)
driver.get("https://demo.actitime.com/login.do")
username=driver.find_element_by_xpath("//input[@id='username']")
username.send_keys("admin")
username.send_keys(Keys.CONTROL+"a")
username.send_keys(Keys.DELETE)

driver.quit()
