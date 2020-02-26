#Context Click
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
filepath=r"E:\SeleniumPrg\drivers\chromedriver.exe"
driver=webdriver.Chrome(executable_path=filepath)
driver.get("https://www.actimind.com/")
driver.implicitly_wait(10)
action=ActionChains(driver)
action.context_click().perform()
ac=driver.find_element_by_xpath("//a[contains(text(),'ABOUT COMPANY')]")
action.context_click(ac).perform()
driver.quit()