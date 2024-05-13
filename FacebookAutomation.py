import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
#from selenium.webdriver.chrome.service import Service
#driver = webdriver.Chrome(service=Service(executable_path=r"C:\Users\pnish\Downloads\chromedriver_124.exe"))
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.facebook.com/")

driver.implicitly_wait(10)

driver.find_element(By.XPATH,"//*[text()='Create new account']").click()
#time.sleep(3)

driver.find_element(By.NAME,"firstname").send_keys("Nishit")
time.sleep(1)
driver.find_element(By.NAME,"lastname").send_keys("Patel")
time.sleep(1)
driver.find_element(By.NAME,"reg_email__").send_keys("nishit@gmail.com")
time.sleep(1)
driver.find_element(By.NAME,"reg_passwd__").send_keys("123456789")
time.sleep(1)
day = Select(driver.find_element(By.XPATH,"//select[@title='Day']"))
day.select_by_visible_text("23")
time.sleep(1)
month = Select(driver.find_element(By.NAME,"birthday_month"))
month.select_by_visible_text("Aug")
time.sleep(1)
year = Select(driver.find_element(By.NAME,"birthday_year"))
year.select_by_visible_text("2004")
time.sleep(1)
driver.find_element(By.XPATH,"//label[text()='Male']").click()
time.sleep(1)
driver.find_element(By.XPATH,"//button[text()='Sign Up']").click()

