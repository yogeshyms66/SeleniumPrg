from selenium import webdriver
from time import sleep
#add_cookie
filepath=r"E:\SeleniumPrg\drivers\chromedriver.exe"
driver=webdriver.Chrome(executable_path=filepath)
driver.get("https://demo.actitime.com/login.do")
cookie={"name":"Cookies","value":"hello"}
driver.add_cookie(cookie)
sleep(5)
print("cookies added")
driver.close()