# я хз что написать в assertEqual, как вариант сравнил приветственный текст
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By

class TestAbs(unittest.TestCase):
    def test_url1(self):
        browser = webdriver.Chrome()
        browser.get("http://suninjuly.github.io/registration1.html")

        first_name = browser.find_element(By.CSS_SELECTOR, "[placeholder='Input your first name']")
        first_name.send_keys('dima')
        last_name = browser.find_element(By.CSS_SELECTOR, '[placeholder="Input your last name"]')
        last_name.send_keys("matveev")
        email_input = browser.find_element(By.CSS_SELECTOR, "[placeholder='Input your email']")
        email_input.send_keys('dima.matveev@lox.ru')

        button = browser.find_element(By.CSS_SELECTOR, 'button.btn')
        button.click()

        self.assertEqual('Congratulations! You have successfully registered!', browser.find_element(By.TAG_NAME, 'h1').text, "Проверям что мы зарегестрировались")

    def test_url2(self):
        browser = webdriver.Chrome()
        browser.get("http://suninjuly.github.io/registration2.html")

        first_name = browser.find_element(By.CSS_SELECTOR, "[placeholder='Input your first name']")
        first_name.send_keys('dima')
        last_name = browser.find_element(By.CSS_SELECTOR, '[placeholder="Input your last name"]')
        last_name.send_keys("matveev")
        email_input = browser.find_element(By.CSS_SELECTOR, "[placeholder='Input your email']")
        email_input.send_keys('dima.matveev@lox.ru')

        button = browser.find_element(By.CSS_SELECTOR, 'button.btn')
        button.click()

        self.assertEqual('Congratulations! You have successfully registered!', browser.find_element(By.TAG_NAME, 'h1').text, "Проверям что мы зарегестрировались")

if __name__ == '__main__':
    unittest.main()
