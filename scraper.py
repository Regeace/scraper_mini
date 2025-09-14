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
    options.add_argument("--window-size=1920,1200")

    driver = webdriver.Chrome(options=options)

    for town, web_address in url.items():
        driver.get(web_address)
        date_and_time = datetime.datetime.now().replace(microsecond=0)
        try:
            soup = BeautifulSoup(driver.page_source, "html.parser")
            temperature = soup.find('div', class_='now-weather').get_text()
            with open('scraps/scraps.txt', 'a', encoding='utf-8') as file:
                file.write(f'{date_and_time} {town} {temperature}\n')

        except AttributeError:
            with open('scraps/errors.txt', 'a', encoding='utf-8') as file:
                file.write(f'{date_and_time} Ошибка при запросе страницы: {town} {web_address}\n')
            continue

    else:
        driver.quit()


url = {'Люберцы': 'https://www.gismeteo.ru/weather-lyubertsy-11433/now/',
       'Подольск': 'https://www.gismeteo.ru/weather-podolsk-11955/now/',
       'Одинцово': 'https://www.gismeteo.ru/weather-odintsovo-11938/now/',
       'Химки': 'https://www.gismeteo.ru/weather-khimki-11582/now/'}

while True:
    scrape_temperature(url)
    sleep(3590)
