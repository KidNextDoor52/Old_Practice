from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

ACCOUNT_EMAIL = "MY_EMAIL_ADDRESS"
ACCOUNT_PASSWORD = "MY_PW"

#-------------------OPTIONAL--------------------------------
#Keeps the browser open for diagnostics

driver = webdriver.Chrome(options=chrome_options)







#-------------------- Click Reject Cookies Button---------------------
time.sleep(2)
reject_button = driver.find_element(by=By.CSS_SELECTOR, value='button[action-type="DENY"]')







#---------------------click sign in button----------------




#------------------------Sign in-------------------------



#You may be presented with a CAPTCHA - Solve the Puzzle Manually
input("Press Enter When you have solved the Captcha")




