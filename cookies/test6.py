#Script to skip the login.
from selenium import webdriver
from time import sleep
filepath=r"E:\SeleniumPrg\drivers\chromedriver.exe"
driver=webdriver.Chrome(executable_path=filepath)
driver.implicitly_wait(10)
driver.get("https://demo.actitime.com/login.do")
driver.find_element_by_xpath("//input[@id='username']").send_keys("admin")
driver.find_element_by_xpath("//input[@name='pwd']").send_keys("manager")
driver.find_element_by_xpath("//a[@id='loginButton']").click()
sleep(15)
c=driver.get_cookies()
driver.close()

driver=webdriver.Chrome(executable_path=filepath)
driver.maximize_window()
driver.get("https://demo.actitime.com/login.do")
for i in c:
    driver.add_cookie(i)
driver.refresh()