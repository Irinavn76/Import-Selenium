# В терминале скачали библиотеку, установили. Актуализовали браузер Chrome.
# Создаем код для импортирования веб-драйвера и seleniuma.
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

# Создаем переменную
options = webdriver.ChromeOptions()
options.add_experimental_option( 'detach', True)
driver = webdriver.Chrome(options=options, service=ChromeService(ChromeDriverManager().install()))
base_url = 'https://www.saucedemo.com/' # Вводим базовый url для постоянного использования
driver.get(base_url) # Вводим команду get для открытия ссылки базового url
driver.set_window_size( 1920, 1080) # Вводим команду драйверу для открытия окна браузера в заданном разрешении экрана

# Код вполняется, переходим в Swag Labs, но выдает ошибку: Pycharm не может найти модуль для импорта. Не понимаю...
# Пыталась добавить модуль для импорта через sys.psth.append(), стало хуже

