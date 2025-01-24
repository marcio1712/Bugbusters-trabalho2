from src.utils.Helpers import *
from src.core.config import *
from index import *

def getEventsTest():
    logger.info("Dado que o usuário expanda o controlador: ")
    click_element_by_id("operations-tag-event-controller")

    logger.info("Dado que o usuário selecione a opção de listar eventos:")
    click_element_by_id("operations-event-controller-listarUsingGET_1")

    logger.info("Dado que o usuário selecione o botão 'Try it out':")
    click_element_by_class("try-out__btn")

    logger.info("Dado que o usuário selecione a opção 'Execute':")
    click_element_by_class("opblock-control__btn")

    status_code = BROWSER.find_elements(By.CLASS_NAME, "response-col_status")[1].text
    response_body = BROWSER.find_elements(By.CLASS_NAME, "microlight")[0].text

    if status_code == '200':
        logger.info("Eventos obtidos com sucesso!")
        logger.info("Corpo da resposta:\n " + response_body)
        return True
    
    elif response_body == "[]":
        logger.error("Não foi possível realizar a função de Listar Eventos: O sistema não possui dados!")
        return False
    
    else:
        raise Exception("Não foi possível realizar a função de Listar Eventos")


def getEventsByIdTest(id):
    logger.info("Testando listar eventos por Id do usuário de identificador: " + str(id))
    
    logger.info("Dado que o usuário expanda o controlador: ")
    click_element_by_id("operations-tag-event-controller")
    
    getById = BROWSER.find_elements(By.CLASS_NAME, "opblock-summary-get")[1]

    logger.info("Dado que o usuário selecione a opção de listar eventos por Id:")
    getById.click()

    logger.info("Dado que o usuário selecione o botão 'Try it out':")
    click_element_by_class("try-out__btn")

    logger.info("Dado que o usuário preencha com o Id 1:")
    insert_string_by_xpath("/html/body/div/section/div[2]/div[2]/div[5]/section/div/span[3]/div/div/span[2]/div/div[2]/div/div[1]/div[2]/table/tbody/tr/td[2]/input", id)

    logger.info("Dado que o usuário selecione a opção 'Execute':")
    click_element_by_class("opblock-control__btn")

    status_code = BROWSER.find_elements(By.CLASS_NAME, "response-col_status")[1].text
    response_body = BROWSER.find_elements(By.CLASS_NAME, "microlight")[0].text

    if status_code == '200':
        logger.info("Eventos obtidos com sucesso!")
        logger.info("Corpo da resposta:\n " + response_body)
    elif response_body == "[]":
        logger.error("Não foi possível realizar a função de Listar Eventos: O sistema não possui dados!")
    else:
        raise Exception("Não foi possível realizar a função de Listar Eventos")

