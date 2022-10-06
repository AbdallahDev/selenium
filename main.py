from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

driver.get("https://www.python.org/")

xpath = '//*[@id="content"]/div/section/div[2]/div[2]/div/ul'
menu_element = driver.find_element(By.XPATH, xpath)

li_elements = menu_element.find_elements(By.TAG_NAME, 'li')
a_elements = menu_element.find_elements(By.TAG_NAME, 'a')
time_elements = menu_element.find_elements(By.TAG_NAME, 'time')

events = {}

index = 0
for li in li_elements:
    date = f"{li.find_element(By.TAG_NAME, 'span').get_attribute('innerText')}{li.find_element(By.TAG_NAME, 'time').text}"
    name = li.find_element(By.TAG_NAME, 'a').text
    events[index] = {'time': date, 'name': name}
    index += 1

print(events)
