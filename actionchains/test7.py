
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
filepath=r"E:\SeleniumPrg\drivers\chromedriver.exe"
driver=webdriver.Chrome(executable_path=filepath)
driver.get("https://demo.actitime.com/login.do")
driver.implicitly_wait(10)
action=ActionChains(driver)
link=driver.find_element_by_xpath("//a[text()='actiTIME Inc.']")
action.click_and_hold(link)
action.release(link)
action.perform()
driver.quit()