# Coleção de imports
from toolbox.collection import *
from selenium.webdriver import firefox
from selenium.webdriver.firefox import options
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox import webdriver
from selenium.webdriver.firefox import firefox_profile
from selenium.webdriver.firefox import firefox_binary
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from webautomators import WebGeckoDriver
from webautomators import SeleniumGeckoDriver
from webautomators.extended_options import WebFirefoxOptions
from webautomators.extended_options import WebFirefoxProfile

# Definição de class
class firefox_config():

# Catálogo de funções
    def firefox_settings(self, optional_settings = [None], optional_proxy = None):

        # Definição das variáveis
        config = Options()
        binary = ('C:/Program Files/Mozilla Firefox/firefox.exe')

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

        # Define as configurações adcionais do driver
        config.add_argument('--disable-extensions')
        config.add_argument("--disable-popup-blocking")
        config.add_argument("--ignore-certificate-errors")

        # Inicia o driver e carrega as configurações
        driver = selenium.webdriver.Firefox(executable_path = GeckoDriverManager().install('./driver/geckodriver.exe'),
                                            firefox_binary = binary,
                                            firefox_options = config)

        # Retorna o driver configurado para a aplicação principal
        return driver