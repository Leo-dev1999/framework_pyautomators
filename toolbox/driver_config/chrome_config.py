# Coleção de imports
from toolbox.collection import *
from selenium.webdriver import chrome
from selenium.webdriver.chrome import options
from selenium.webdriver.chrome import service
from selenium.webdriver.chrome import webdriver
from selenium.webdriver.chrome.options import Options
from webautomators import WebChromeDriver
from webautomators import SeleniumChromeDriver
from webautomators.extended_options import WebChromeOptions

# Definição de class
class chrome_config():

# Catálogo de funções
    def chrome_settings(self, optional_settings = [None], optional_proxy = None):

        # Definição das variáveis
        config = Options()

        # Define as configurações opcionais do driver
        if('maximized' in optional_settings):
            config.add_argument('--start-maximized')

        if('fullscreen' in optional_settings):
            config.add_argument("--start-fullscreen")

        if('headless' in optional_settings):
            config.add_argument('--headless')
            config.add_argument('--disable-gpu')

        if('proxy'  in optional_settings):
            config.add_argument('--proxy-server={}'.format(optional_proxy))

        # Define as configurações adicionais do driver
        config.add_argument('--disable-extensions')
        config.add_argument("--disable-popup-blocking")
        config.add_argument("--ignore-certificate-errors")

        # Inicia o driver e carrega as configurações
        driver = selenium.webdriver.Chrome(ChromeDriverManager().install('./driver/chromedriver.exe'), 
                                           chrome_options = config)

        # Retorna o driver configurado para a aplicação principal
        return driver