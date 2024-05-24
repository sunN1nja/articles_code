from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

# Инициализация драйвера Chrome
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# Открытие страницы Google
driver.get("https://www.google.com")

# Поиск строки поиска и ввод текста
search_box = driver.find_element(By.NAME, "q")
search_box.send_keys("sunninja dzen" + Keys.RETURN)

# Даем странице немного времени, чтобы загрузить результаты
time.sleep(3)

# Находим и кликаем по первой ссылке в выдаче
first_result = driver.find_element(By.XPATH, "(//a/h3)[1]/../../..")
first_result.click()

# Даем странице немного времени, чтобы загрузиться
time.sleep(3)

# Закрытие браузера
driver.quit()