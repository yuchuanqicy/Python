import time
from selenium  import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains


driver=webdriver.Edge()
driver.maximize_window()
driver.implicitly_wait(20)
driver.get("https://www.csdn.net")
print(driver.find_element(By.LINK_TEXT,"阅读深度、前沿文章").get_attribute('href'))
driver.quit()




