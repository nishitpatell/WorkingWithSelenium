import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import pandas as pd

def process_excel_data(Id, Wrows, WebSheet):
    for rows in range(2, Wrows + 1):
        WTitle = WebSheet.iloc[rows - 1, 1]
        if(WTitle == Id):
            path = WebSheet.iloc[rows - 1, 3]
            val = WebSheet.iloc[rows - 1, 4]

            if val == 0:
                driver.find_element(By.XPATH, path).click()
                time.sleep(2)
            else:
                if val == "event visit":
                    title = Select(driver.find_element(By.XPATH, 'leave_main_id'))
                    title.select_by_visible_text("event visit")
                    time.sleep(5)
                else:
                    driver.find_element(By.XPATH, path).send_keys(val)
                    time.sleep(2)

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://glexas.com/hostel/login")
time.sleep(10)

sample = pd.read_excel("EXCELFILE/MainAndWeb.xlsx", sheet_name=['Main','Web'])
MainSheet = sample["Main"]
WebSheet = sample["Web"]

MRows = MainSheet.shape[0]
MCols = MainSheet.shape[1]
Wrows = WebSheet.shape[0]

for row in range(1, MRows+1):
    Id = MainSheet.iloc[row - 1, 1]
    process_excel_data(Id, Wrows, WebSheet)
