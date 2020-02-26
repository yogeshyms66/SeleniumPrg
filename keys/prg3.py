#Write a script to copy & paste the value present in one text box into another text box?
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
filepath=r"E:\SeleniumPrg\drivers\chromedriver.exe"
driver=webdriver.Chrome(executable_path=filepath)
driver.get("https://demo.actitime.com/login.do")
username=driver.find_element_by_xpath("//input[@id='username']")
username.send_keys("admin")
username.send_keys(Keys.CONTROL+"a")
username.send_keys(Keys.CONTROL+"c")
pwd=driver.find_element_by_xpath("//input[@name='pwd']")
pwd.send_keys(Keys.CONTROL+"v")
driver.quit()