import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

addr = os.environ['BIN_ADDR']
driver = webdriver.Firefox()

driver.get('https://maps.cheltenham.gov.uk/map/Aurora.svc/run?script=\Aurora\CBC%20Waste%20Streets.AuroraScript%24&workflow_id=wastestreet')
# assert '?' in driver.title

loc_search = driver.find_element(By.CLASS_NAME, 'auroraComboBoxInput')  # Find the search box
loc_search.send_keys(addr + Keys.ENTER)
#loc_select = driver.find_element(By.CLASS_NAME, 'auroraResultBullet auroraResultNo1')
loc_select = driver.find_element(By.CLASS_NAME, 'summary') # div.summary

result = loc_select.click()
print(result)

driver.quit()