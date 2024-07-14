from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

file_path="/Users/saikrishnamj/Downloads/download (1).xlsx"

driver = webdriver.Chrome()
driver.implicitly_wait(20)
driver.get("https://rahulshettyacademy.com/upload-download-test/index.html")
driver.find_element(By.ID,"downloadButton").click()
file_input=driver.find_element(By.CSS_SELECTOR,"input[type='file']")
file_input.send_keys(file_path)
WebDriverWait(driver,10).until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR, ".Toastify__toast-body div:nth-child(2)")))
message = driver.find_element(By.CSS_SELECTOR, ".Toastify__toast-body div:nth-child(2)").text
print(message)

driver.close()

