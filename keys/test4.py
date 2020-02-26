#Write a script to launch the link in the new tab
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
filepath=r"E:\SeleniumPrg\drivers\chromedriver.exe"
driver=webdriver.Chrome(executable_path=filepath)
driver.get("https://demo.actitime.com/login.do")
link=driver.find_element_by_xpath("//a[text()='actiTIME Inc.']")
link.send_keys(Keys.CONTROL+Keys.ENTER)

driver.quit()