#Move by offset
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
filepath=r"E:\SeleniumPrg\drivers\chromedriver.exe"
driver=webdriver.Chrome(executable_path=filepath)
driver.get("https://www.actimind.com/")
driver.implicitly_wait(10)
action=ActionChains(driver)

area=driver.find_element_by_xpath("//a[contains(text(),'AREAS OF EXPERTISE')]")
loc=area.location
x=loc.get("x")
y=loc.get("y")
action.move_by_offset(x,y).perform()
driver.quit()
