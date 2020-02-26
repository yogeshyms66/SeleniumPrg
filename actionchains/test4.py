#Pause

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
filepath=r"E:\SeleniumPrg\drivers\chromedriver.exe"
driver=webdriver.Chrome(executable_path=filepath)
driver.maximize_window()
driver.get("https://www.istqb.in/")
driver.implicitly_wait(10)
action=ActionChains(driver)
fn=driver.find_element_by_xpath("//a[contains(text(),'FOUNDATION')]")
action.move_to_element(fn).pause(2)
driver.quit()
