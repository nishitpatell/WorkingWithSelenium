import time
from selenium import webdriver
from selenium.webdriver.common.by import By
# from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://demo.automationtesting.in/Windows.html")

parent_window = driver.current_window_handle

time.sleep(5)
driver.find_element(By.XPATH, '/html/body/div[2]/div/div[5]/footer/div/div/div[2]/a[1]/span').click()
time.sleep(2)

child_windows = driver.window_handles  # returns list
time.sleep(2)
for child in child_windows:
    print(child)
    if parent_window != child:
        print("Switching to new window /n")
        time.sleep(2)
        driver.switch_to.window(child)
        print("title is ", driver.title)
        time.sleep(2)
        driver.find_element(By.XPATH, '//*[@id=":rt:"]').send_keys("abc@gmail.com")
        time.sleep(2)
        driver.close()

time.sleep(2)
driver.switch_to.window(parent_window)
print("parent window title", driver.title)
time.sleep(2)
driver.find_element(By.XPATH, '/html/body/div[2]/div/div[5]/footer/div/div/div[2]/a[2]').click()
