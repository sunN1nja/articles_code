from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

# Указываем URL, на который хотим перейти
url = 'https://dzen.ru/sunninja'

# Настройка WebDriver
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

# Открытие страницы в браузере Chrome
driver.get(url)

# Подождём
time.sleep(3)

# Не забывайте закрыть браузер после завершения работы
driver.quit()