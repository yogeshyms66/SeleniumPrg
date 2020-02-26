from selenium import webdriver
from time import sleep
#delete_cookie
filepath=r"E:\SeleniumPrg\drivers\chromedriver.exe"
driver=webdriver.Chrome(executable_path=filepath)
driver.get("https://demo.actitime.com/login.do")
driver.delete_all_cookies()
c=driver.get_cookies()
for i in c:
    print(i)
else:
    print("no cookies")
driver.close()