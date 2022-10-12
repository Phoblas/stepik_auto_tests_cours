from selenium.webdriver.common.by import By
import pytest
import time
import math


@pytest.mark.parametrize("link", ['236895', '236896', '236897', '236898', '236899', '236903', '236904', '236905'])
def test_open_browser(browser, link):
    browser.implicitly_wait(5) #
    browser.get(f"https://stepik.org/lesson/{link}/step/1") # открываю нужную страницу
    input_answer = browser.find_element(By.CSS_SELECTOR, 'textarea') # нахожу поле для ввода
    answer = math.log(int(time.time())) # нахожу правильный ответ, не вынес отдельно, т.к. нужно каждый раз точное время
    input_answer.send_keys(str(answer)) # вставляю ответ в поле для него, через строку
    button = browser.find_element(By.CSS_SELECTOR, "button.submit-submission") # нахожу кнопку отправить
    button.click() # нажимаю на кнопку отправить
    feedback = browser.find_element(By.CSS_SELECTOR, '.attempt__message p').text # нахожу текст фидбэка
    assert feedback == "Correct!", f"{feedback}" # сравнивая фидбэк с нужным, в случае ошибки вывожу фидбэк
