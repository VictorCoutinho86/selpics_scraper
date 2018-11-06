from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from config import Config

import time

config = Config


def start(url):
    print("Abrindo a pagina...")
    driver = webdriver.Chrome(config.DIR_DRIVER)
    driver.get(url)

    return driver


def login(driver):
    print("Realizando o Login...")

    # Preenchendo o usuário e clicando
    usuario = driver.find_element_by_css_selector("#login-selecao")
    usuario.send_keys(config.USUARIO)
    time.sleep(5)

    # Preenchendo a senha e clicando
    senha = driver.find_element_by_css_selector("#senha-selecao")
    senha.send_keys(config.SENHA)
    time.sleep(5)

    # Clicando no botão de login
    botao = driver.find_element_by_css_selector("#bt_login")
    botao.click()

    try:
        element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "lb-title")))
    finally:
        print("Encontrou o title")
        element.click()

    return driver


def downloadFotos(driver):
    print("Iniciando o download das fotos...")
    time.sleep(5)
    try:
        element = driver.find_element_by_xpath\
            (u"(.//*[normalize-space(text()) and normalize-space(.)=''])[1]/following::a[1]")
        element.click()
        time.sleep(5)
    finally:
        return


def principal():
    driver = start(config.BASE_URL)
    time.sleep(5)
    login(driver)

    popup = driver.find_element_by_css_selector(".lb-button")

    if popup:
        popup.click()
    else:
        print("Sem Alerta!!")

    i = 0
    while i < 91:
        if i == 0:
            time.sleep(5)
            foto = driver.find_element_by_xpath\
                ("(.//*[normalize-space(text()) and normalize-space(.)='SAMARA'])[1]/following::img[1]")
            foto.click()
        downloadFotos(driver)
        proximo = driver.find_element_by_css_selector("a[title='Próxima']")
        proximo.click()
        i += 1

    print("Finalizando o programa...")
    driver.close()


principal()





