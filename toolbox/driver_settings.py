# Coleção de imports
from toolbox.collection import *
from toolbox.driver_config.ie_config import ie_config
from toolbox.driver_config.edge_config import edge_config
from toolbox.driver_config.chrome_config import chrome_config
from toolbox.driver_config.firefox_config import firefox_config

# Definição de class
class tipo_browser(Enum):
    chrome = 1
    firefox = 2
    microsoft_edge = 3
    internet_explorer = 4

class driver_settings(chrome_config, edge_config, ie_config, firefox_config):

# Catálogo de funções
    def browser_manager(self, tipo_browser, optional_settings = [None], optional_proxy = None):

        # Configura e executa o browser selecionado
        try:
            if tipo_browser.value == 1:
                driver = self.chrome_settings(optional_settings, optional_proxy)
            elif tipo_browser.value == 2:
                driver = self.firefox_settings(optional_settings, optional_proxy)
            elif tipo_browser.value == 3:
                driver = self.ie_settings(optional_settings, optional_proxy)
            elif tipo_browser.value == 4:
                driver = self.edge_settings(optional_settings, optional_proxy)
        except:
            # Tenta executar o navegador chrome no lugar do browser escolhido
            try:
                driver = self.chrome_settings(optional_settings, optional_proxy)
            except:
                raise Exception ('Não foi possivel executar nenhum dos Browsers')

        # realiza as configurações adicionais do browser escolhido
        driver.implicitly_wait(60)

        return driver