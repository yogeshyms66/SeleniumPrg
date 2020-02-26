#Composite Actions:

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
filepath=r"E:\SeleniumPrg\drivers\chromedriver.exe"
driver=webdriver.Chrome(executable_path=filepath)
driver.get("https://www.actimind.com/")
driver.implicitly_wait(10)
action=ActionChains(driver)
area=driver.find_element_by_xpath("//a[contains(text(),'AREAS OF EXPERTISE')]")
cloud=driver.find_element_by_xpath("//a[contains(text(),'Cloud Applications')]")
action.move_to_element(area).click(cloud).perform()
driver.quit()
