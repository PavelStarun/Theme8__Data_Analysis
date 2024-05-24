import time
import csv
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

url = 'https://www.divan.by/category/ortopedicheskie-divany-dlya-sna'
driver.get(url)
time.sleep(3)

divan_list = driver.find_elements(By.CLASS_NAME, 'WdR1o')

category = []

for divan in divan_list:
    try:
        price = divan.find_element(By.CLASS_NAME, 'ui-LD-ZU').text
        if price:
            price = price.replace('руб.', '')

    except:
        print("Произошла ошибка при парсинге данных")
        continue

    category.append([price])

with open("sofas.csv", 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['Цена'])
    writer.writerows(category)

driver.quit()