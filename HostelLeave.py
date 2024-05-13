import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://glexas.com/hostel/login")
time.sleep(10)
driver.find_element(By.XPATH, '//*[@id="username"]').send_keys("studenttest")
time.sleep(2)
driver.find_element(By.XPATH, '//*[@id="password"]').send_keys("studenttest")
time.sleep(2)
driver.find_element(By.XPATH, '//*[@id="submit_button"]').click()
time.sleep(5)

driver.find_element(By.XPATH, '/html/body/div[2]/div[1]/div[1]/div/div[1]/a/div/div/div').click()
time.sleep(2)
driver.find_element(By.XPATH, '//*[@id="add"]').click()
time.sleep(2)

#title = Select(driver.find_element(By.XPATH, '//*[@id="leave_main_id"]'))
#title.select_by_visible_text("event visit")
Select(driver.find_element(By.XPATH, '//*[@id="leave_main_id"]')).select_by_visible_text("event visit")
time.sleep(2)
driver.find_element(By.XPATH, '//*[@id="leave_place"]').send_keys("Ahmedabad")
time.sleep(2)
driver.find_element(By.XPATH, '//*[@id="reason"]').send_keys("Visiting an event in ahmedabad")
time.sleep(2)

# let from date be 13th may
driver.find_element(By.XPATH, '//*[@id="from_date"]').send_keys("13052004")
time.sleep(2)
# let to date be 14th may
driver.find_element(By.XPATH, '//*[@id="to_date"]').send_keys("14052004")
time.sleep(2)

# from time = 09:00
driver.find_element(By.XPATH, '//*[@id="from_time"]').send_keys("0900")
time.sleep(2)
# to time = 20:00
driver.find_element(By.XPATH, '//*[@id="to_time"]').send_keys("2000")
time.sleep(2)

driver.find_element(By.XPATH, '//*[@id="parameterModalSubmit"]').click()
time.sleep(10)
