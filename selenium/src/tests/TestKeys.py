from src.utils.Helpers import *
from src.core.config import *
from index import *

def getKeysTest() :
    logger.info("Dado que o usuário expanda o controlador: ")
    click_element_by_id("operations-tag-key-controller")
    
    logger.info("Dado que o usuário selecione a opção do método GET:")
    click_element_by_class("opblock-get")

    logger.info("Dado que o usuário selecione o botão 'Try it out':")
    click_element_by_class("try-out__btn")

    logger.info("Dado que o usuário selecione a opção 'Execute':")
    click_element_by_class("opblock-control__btn")

    status_code = BROWSER.find_elements(By.CLASS_NAME, "response-col_status")[1].text
    response_body = BROWSER.find_elements(By.CLASS_NAME, "microlight")[0].text

    if status_code == '200':
        logger.info("Chaves obtidas com sucesso!")
        logger.info("Corpo da resposta:\n " + response_body)

    elif response_body == "[]":
        logger.error("Não foi possível realizar a função de Listar Chaves: O sistema não possui dados!")
    
    else:
        raise Exception("Não foi possível realizar a função de Listar Chaves")    