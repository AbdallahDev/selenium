from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options, service=ChromeService(ChromeDriverManager().install()))

url = "https://en.wikipedia.org/wiki/Main_Page"
url1 = "http://secure-retreat-92358.herokuapp.com/"
driver.get(url1)

f_name = driver.find_element(By.NAME, 'fName')
f_name.send_keys("Abdallah")
l_name = driver.find_element(By.NAME, 'lName')
l_name.send_keys("Ahmad")
email = driver.find_element(By.NAME, 'email')
email.send_keys("paython.smtp@gmail.com")

driver.find_element(By.CSS_SELECTOR, 'button.btn').click()


# xpath = '//*[@id="articlecount"]/a[1]'
# menu_element = driver.find_element(By.XPATH, xpath)
#
# print(menu_element.text)
