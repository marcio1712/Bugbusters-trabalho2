from src.tests.TestEditions import *
from src.tests.TestRatings import *
from src.tests.TestTickets import *
from src.tests.TestEvents import *
from src.tests.TestUsers import *
from src.tests.TestKeys import *
from src.utils.Helpers import *
from src.core.config import *
from index import *


logger.info("Acessando sistema...")
BROWSER.get(API)

try:
    logger.info("---------- Testando RF1: Deve ser possível obter todas as Edições de eventos cadastrados no sistema. ----------")
    getEditionsTest()
    
    logger.info("---------- Testando RF3: Deve ser possível obter todos os Eventos cadastrados no sistema. ----------")
    open_new_tab(API)
    getEventsTest()

    logger.info("---------- Testando RF4: Deve ser possível listar os Eventos em que um usuário está cadastrado. ----------")
    open_new_tab(API)
    getEventsByIdTest(2)

    logger.info("---------- Testando RF5: Deve ser possível obter todas as Chaves cadastradas no sistema. ----------")
    open_new_tab(API)
    getKeysTest()

    logger.info("---------- Testando RF6: Deve ser possível obter todas as Avaliações cadastrados no sistema. ----------")
    open_new_tab(API)
    getRatingsTest()

    logger.info("---------- Testando RF7: Deve ser possível obter todos os Tickets cadastrados no sistema. ----------")
    open_new_tab(API)
    getTicketsTest()

    logger.info("---------- Testando RF8: Deve ser possível obter todos os Usuários cadastrados no sistema. ----------")
    open_new_tab(API)
    getUsersTest()

except Exception as error:
    logger.error("Houve um erro na execução dos Testes: " + repr(error))

