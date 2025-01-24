from selenium.webdriver.common.action_chains import ActionChains
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
import logging

Log_Format = "%(levelname)s %(asctime)s - %(message)s"

logging.basicConfig(filename = "log_execucao_testes.log",
                    filemode = "w",
                    format = Log_Format,
                    level=logging.INFO,
                    encoding= "utf-8")

logger = logging.getLogger()
API = "http://localhost:8080/swagger-ui.html"
SERVICE = Service(ChromeDriverManager().install())
OPTIONS = webdriver.ChromeOptions()
OPTIONS.add_argument("--ignore-certificate-errors")
OPTIONS.add_argument("--ignore-ssl-errors")
OPTIONS.add_argument("--disable-popup-blocking")
OPTIONS.add_argument("--start-maximized")
OPTIONS.add_experimental_option("excludeSwitches", ["enable-logging"])
BROWSER = webdriver.Chrome(service=SERVICE, options=OPTIONS)
ACTION_CHAINS = ActionChains(BROWSER)
WAIT = WebDriverWait(BROWSER, 100)

