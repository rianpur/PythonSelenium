from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Data pengguna yang akan dimasukkan
users = [
    {"Firstname": "Aria", "Lastname": "Suseno", "Age": "200", "Email": "uno@idejongkok.co", "Salary": "60000", "Department": "Store"},
    {"Firstname": "Budi", "Lastname": "Santoso", "Age": "35", "Email": "budi@company.com", "Salary": "50000", "Department": "IT"},
    {"Firstname": "Citra", "Lastname": "Lestari", "Age": "28", "Email": "citra@company.com", "Salary": "45000", "Department": "HR"}
]

# Setup WebDriver
driver = webdriver.Chrome()
driver.get("https://demoqa.com/webtables")


# Loop untuk memasukkan data pengguna
for user in users:
    # Klik tombol "Add"
    add_button = driver.find_element(By.ID, "addNewRecordButton")
    add_button.click()
    time.sleep(1)
    
    # Isi form dengan data user
    driver.find_element(By.ID, "firstName").send_keys(user["Firstname"])
    driver.find_element(By.ID, "lastName").send_keys(user["Lastname"])
    driver.find_element(By.ID, "userEmail").send_keys(user["Email"])
    driver.find_element(By.ID, "age").send_keys(user["Age"])
    driver.find_element(By.ID, "salary").send_keys(user["Salary"])
    driver.find_element(By.ID, "department").send_keys(user["Department"])
    
    # Klik tombol "Submit"
    submit_button = driver.find_element(By.ID, "submit")
    submit_button.click()
    time.sleep(1)

# Tutup browser
driver.quit()
