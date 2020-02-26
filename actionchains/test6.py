#using Keyboard module
from selenium import webdriver
import keyboard
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
filepath=r"E:\SeleniumPrg\drivers\chromedriver.exe"
driver=webdriver.Chrome(executable_path=filepath)
driver.get("https://www.actimind.com/")
driver.implicitly_wait(10)
action=ActionChains(driver)
ac=driver.find_element_by_xpath("//a[contains(text(),'ABOUT COMPANY')]")
action.context_click(ac)
action.perform()
keyboard.press("t")
#keyboard.press("w")
#action.context_click(ac).send_keys(Keys.CONTROL + Keys.ENTER).perform()
#action.context_click(ac).send_keys(Keys.SHIFT + Keys.ENTER).perform()
driver.quit()