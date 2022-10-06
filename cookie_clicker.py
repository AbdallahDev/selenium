import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from datetime import datetime

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", False)
driver = webdriver.Chrome(options=options, service=ChromeService(ChromeDriverManager().install()))

url = "http://orteil.dashnet.org/experiments/cookie/"
driver.get(url)

index = 0
while True:
    driver.find_element(By.ID, 'cookie').click()

    # click_color = "rgba(238, 238, 238, 1)"

    # if buy_grandma_rgba == click_color:
    #     driver.find_element(By.ID, 'buyGrandma').click()
    # elif buy_cursor_rgba == click_color:
    #     driver.find_element(By.ID, 'buyCursor').click()

    # if buy_time_rgba == click_color:
    #     driver.find_element(By.ID, 'buyTime machine').click()
    # elif buy_grandma_rgba == click_color:
    #     driver.find_element(By.ID, 'buyGrandma').click()
    # elif buy_factory_rgba == click_color:
    #     driver.find_element(By.ID, 'buyFactory').click()

    # elif buy_cursor_rgba == click_color:
    #     driver.find_element(By.ID, 'buyCursor').click()

    second = datetime.now().second
    minute = datetime.now().minute
    print(f"minute:second: {minute}:{second}")
    if minute % 5 == 0 and second % 50 == 0:
        print(f"{index}: {minute}:{second}")
        index = index + 1

        buy_cursor_rgba = driver.find_element(By.ID, 'buyCursor').value_of_css_property('background-color')
        buy_grandma_rgba = driver.find_element(By.ID, 'buyGrandma').value_of_css_property('background-color')
        buy_factory_rgba = driver.find_element(By.ID, 'buyFactory').value_of_css_property('background-color')
        buy_mine_rgba = driver.find_element(By.ID, 'buyMine').value_of_css_property('background-color')
        buy_shipment_rgba = driver.find_element(By.ID, 'buyShipment').value_of_css_property('background-color')
        buy_alchemy_rgba = driver.find_element(By.ID, 'buyAlchemy lab').value_of_css_property('background-color')
        buy_portal_rgba = driver.find_element(By.ID, 'buyPortal').value_of_css_property('background-color')
        buy_time_rgba = driver.find_element(By.ID, 'buyTime machine').value_of_css_property('background-color')

        click_color = "rgba(238, 238, 238, 1)"

        if buy_time_rgba == click_color:
            driver.find_element(By.ID, 'buyTime machine').click()
        elif buy_portal_rgba == click_color:
            driver.find_element(By.ID, 'buyPortal').click()
        elif buy_alchemy_rgba == click_color:
            driver.find_element(By.ID, 'buyAlchemy lab').click()
        elif buy_shipment_rgba == click_color:
            driver.find_element(By.ID, 'buyShipment').click()
        elif buy_mine_rgba == click_color:
            driver.find_element(By.ID, 'buyMine').click()
        elif buy_factory_rgba == click_color:
            driver.find_element(By.ID, 'buyFactory').click()
        elif buy_grandma_rgba == click_color:
            driver.find_element(By.ID, 'buyGrandma').click()
        elif buy_cursor_rgba == click_color:
            driver.find_element(By.ID, 'buyCursor').click()

    time.sleep(0.0000000000001)
    # index = index + 1
    # print(index)
