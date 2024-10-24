from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

PATH = r"C:\Program Files (x86)\chromedriver.exe" 

service = Service(PATH)
driver = webdriver.Chrome(service=service)

driver.get("https://itti.com.np/")
print(driver.title) 


search_element = driver.find_element(By.CSS_SELECTOR, ".w-full.p-2\\.5.ml-\\[5px\\].rounded-t-md.border-0.focus\\:outline-none.placeholder\\:text-gray")


search_element.send_keys("test")  
search_element.send_keys(Keys.RETURN) 


input("Press Enter to close the window")

# Close the browser
driver.quit()
