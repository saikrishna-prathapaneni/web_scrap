from selenium import webdriver 
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC
import time
import csv

driver = webdriver.Chrome()
wait = WebDriverWait(driver, 10)


link = 'https://endlessfrontierlabs.com/mentors/#(mediaboxes-grid-5ef6bef578b87|popup)=/portfolio/?pfl=1000055;'  # Replace with the actual link
driver.get(link)

names = []
pfl_ids = [] 

button = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[4]/div[2]/div[3]/button[2]')))
#button = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[4]/div[2]/div[3]/button[2]')))
# button is not None:
while True:
  print("start")
  url = driver.current_url
  print(url)
  pfl_id = url.split('pfl=')[1].split(';')[0]
  pfl_ids.append(pfl_id)

  name_element = wait.until(EC.visibility_of_element_located((By.XPATH, '/html/body/div[4]/div[2]/div[3]/button[2]')))
  name = name_element.text
  names.append(name)

  button.click()

  try:
    button = wait.until(EC.element_to_be_clickable((By.XPATH, '//button[@data-fancyboxmb-next]')))
  except:
    button = None
  time.sleep(1)

with open('mentor_data.csv', 'w', newline='') as file:
  writer = csv.writer(file)
  writer.writerow(['Name', 'Pfl Id'])
  for name, pfl_id in zip(names, pfl_ids):
    writer.writerow([name, pfl_id])

driver.quit()