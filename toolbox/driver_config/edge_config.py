# Coleção de imports
from toolbox.collection import *
from selenium.webdriver import edge
from selenium.webdriver.edge import options
from selenium.webdriver.edge import service
from selenium.webdriver.edge.options import Options
from webautomators import WebEdgeDriver
from webautomators import SeleniumEdgeDriver

# Definição de class
class edge_config():

# Catálogo de funções
    def edge_settings(self, optional_settings = [None], optional_proxy = None):

        # Inicia o driver e carrega as configurações
        driver = webdriver.Edge(EdgeDriverManager().install('./driver/MicrosoftWebDriver.exe'))

        # Retorna o driver configurado para a aplicação principal
        return driver