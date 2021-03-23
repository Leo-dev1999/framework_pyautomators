# Coleção de imports
from toolbox.collection import *
from selenium.webdriver import ie
from selenium.webdriver.ie import options
from selenium.webdriver.ie import service
from selenium.webdriver.ie import webdriver
from selenium.webdriver.ie.options import Options
from selenium.webdriver.ie.service import Service
from selenium.webdriver.ie.webdriver import WebDriver
from webautomators import WebIeDriver
from webautomators import SeleniumIeDriver

# Definição de class
class ie_config():

# Catálogo de funções
    def ie_settings(self, optional_settings = [None], optional_proxy = None):

        # Definição das variáveis
        ie_options = Options()

        # Define as configurações adcionais do driver
        ie_options.ignore_protected_mode_settings = True

        # Inicia o driver e carrega as configurações
        driver = webdriver.Ie(IEDriverManager('').install('./driver/IEDriverServer_win.exe'), 
                              options=ie_options)

        # Retorna o driver configurado para a aplicação principal
        return driver