from src.utils.Helpers import *
from src.core.config import *
from index import *

def click_controller():
    logger.info("Dado que o usuário expanda o controlador:")
    click_element_by_id("operations-tag-edition-controller")

def getEditionsTest():
    click_controller()
    click_get()
    click_try()
    click_execute()

    status_code = BROWSER.find_elements(By.CLASS_NAME, "response-col_status")[1].text
    response_body = BROWSER.find_elements(By.CLASS_NAME, "microlight")[0].text
 
    if status_code == '200':
        logger.info("Edições obtidas com sucesso!")
        logger.info("Corpo da resposta:\n " + response_body)
        
    elif response_body == "[]":
        logger.error("Não foi possível realizar a função de Listar Edições: O sistema não possui dados!")

    else:
        raise Exception("Não foi possível realizar a função de Listar Edições")

