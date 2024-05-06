import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()

driver.get("https://www.amazon.in/ap/signin?openid.pape.max_auth_age=0&openid.return_to=https%3A%2F%2Fwww.amazon.in%2F%3Fref_%3Dnav_signin&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.assoc_handle=inflex&openid.mode=checkid_setup&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0")

username = driver.find_element(By.XPATH, "//input[@id='ap_email']").send_keys("8275038166")
driver.find_element(By.XPATH, "//input[@id='continue']").click()
password = driver.find_element(By.XPATH, "//input[@id='ap_password']").send_keys("CAKE@4649")
driver.find_element(By.XPATH, "//input[@id='signInSubmit']").click()

get_title = driver.title
print(get_title)
time.sleep(3)
m = driver.find_element(By.XPATH, "//span[text()='Account & Lists']")
a = ActionChains(driver)
a.move_to_element(m).perform()
time.sleep(5)
driver.find_element(By.XPATH,"//span[text()='Sign Out']").click()
time.sleep(5)
driver.close()




