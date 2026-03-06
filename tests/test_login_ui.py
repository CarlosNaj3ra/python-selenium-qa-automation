from selenium import webdriver
from selenium.webdriver.common.by import By
import time


def test_login_correcto():

    driver = webdriver.Edge()

    driver.get("http://127.0.0.1:5000/login")

    driver.find_element(By.ID, "username").send_keys("admin")
    driver.find_element(By.ID, "password").send_keys("123456")

    driver.find_element(By.ID, "login-btn").click()

    time.sleep(2)

    assert "Dashboard" in driver.page_source

    driver.quit()

def test_login_password_incorrecto():

    driver = webdriver.Edge()

    driver.get("http://127.0.0.1:5000/login")

    driver.find_element(By.ID, "username").send_keys("admin")
    driver.find_element(By.ID, "password").send_keys("wrongpass")

    driver.find_element(By.ID, "login-btn").click()

    assert "Credenciales incorrectas" in driver.page_source

    driver.quit()

def test_login_usuario_vacio():

    driver = webdriver.Edge()

    driver.get("http://127.0.0.1:5000/login")

    driver.find_element(By.ID, "username").send_keys("")
    driver.find_element(By.ID, "password").send_keys("123456")

    driver.find_element(By.ID, "login-btn").click()

    assert "El campo de usuario esta vacio" in driver.page_source

    driver.quit()


def test_login_password_vacio():

    driver = webdriver.Edge()
    driver.get("http://127.0.0.1:5000/login")

    driver.find_element(By.ID, "username").send_keys("admin")
    driver.find_element(By.ID, "login-btn").click()

    time.sleep(2)

    assert "El campo de password esta vacio" in driver.page_source

    driver.quit()