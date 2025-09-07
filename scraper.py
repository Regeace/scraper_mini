from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
from time import sleep
import datetime


def scrape_temperature(url: dict):
    """Собирает данные о текущей температуре."""
    options = Options()
    'Для проверки окна браузера закомментируйте следующую строку'
    options.add_argument('--headless')
    # options.add_argument("--window-size=1920,1200")

    driver = webdriver.Chrome(options=options)

    try:
        for town, web_address in url.items():
            driver.get(web_address)
            html = driver.page_source
            soup = BeautifulSoup(html, "html.parser")
            # print(soup)
            date_and_time = datetime.datetime.now().replace(microsecond=0)
            with open('scraps/scraps.txt', 'a', encoding='utf-8') as file:
                file.write(str(date_and_time) + ' ' + town + ' text' + '\n')


    finally:
        driver.quit()


url = {'Люберцы': 'https://www.gismeteo.ru/weather-lyubertsy-11433/now/'}

# while True:
scrape_temperature(url)
# sleep(3600)
