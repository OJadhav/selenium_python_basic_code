from time import sleep

from PIL import ImageGrab
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()

driver.get("https://www.google.com")
sleep(5)
search_box = driver.find_element(By.XPATH, "//textarea[@name='q']").send_keys("Amazon")
sleep(9)
driver.find_element(By.XPATH, "//input[@type='submit']").click()
sleep(9)
screenBuffer = ImageGrab.grab()
save_path = 'C:/Users/Admin/PycharmProjects/pythonBasic_Project/Test.jpg'
screenBuffer.save(save_path)
