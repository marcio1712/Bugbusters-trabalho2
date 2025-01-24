from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from src.core.config import *

def insert_string_by_xpath(localizacao_xpath, string):
    try:
        logger.info("Inserindo string no elemento de xpath: " + localizacao_xpath)
        element = WAIT.until(
            EC.visibility_of_element_located((By.XPATH, localizacao_xpath))
        )
        element.send_keys(string)
    except:
        logger.info("Não foi possível clicar no elemento solicitado")
    finally:
        logger.info("Sucesso!")

def open_new_tab(url):
    BROWSER.execute_script("""window.open("about:blank");""")
    BROWSER.switch_to.window(BROWSER.window_handles[1])
    BROWSER.get(url)


def click_element_by_class(classe):
    try:
        logger.info("Clicando no elemento de Classe: " + classe)
        element = WAIT.until(EC.element_to_be_clickable((By.CLASS_NAME, classe)))
        element.click()
    except:
        logger.info("Não foi possível clicar no elemento solicitado")
    finally:
        logger.info("Sucesso!")

def click_element_by_id(id):
    try:
        logger.info("Clicando no elemento de Id: " + id)
        element = WAIT.until(EC.visibility_of_element_located((By.ID, id)))
        element.click()
    except:
        logger.info("Não foi possível clicar no elemento solicitado")
    finally:
        logger.info("Sucesso!")

def clear_input_by_class(className):
    element = WAIT.until(EC.element_to_be_clickable((By.CLASS_NAME, className)))
    element.clear()

def click_get():
    logger.info("Dado que o usuário selecione a opção do método GET:")
    click_element_by_class("opblock-get")

def click_try():
    logger.info("Dado que o usuário selecione o botão 'Try it out':")
    click_element_by_class("try-out__btn")

def click_execute():
    logger.info("Dado que o usuário selecione a opção 'Execute':")
    click_element_by_class("opblock-control__btn")