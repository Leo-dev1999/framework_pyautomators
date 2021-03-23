# Coleção de imports
from toolbox.collection import *
from toolbox.funcoes_selenium import select_type
from toolbox.funcoes_selenium import funcoes_selenium

# Definição de class
class funcoes_csf(funcoes_selenium):

# Catálogo de funções
    def menu_navigate(self, primary_menu, secondary_menu, additional_menu_I='', additional_menu_II=''):

        # Definição das variáveis
        counter_attempts = 10
        action = ActionChains(self.driver)

        # Executa a navegação pelos menus informados
        while(counter_attempts > 0):
            try:
                element = self.driver.find_element_by_link_text(primary_menu)
                action.move_to_element(element).perform()

                element = self.driver.find_element_by_link_text(secondary_menu)
                action.move_to_element(element).perform()

                if(additional_menu_I != ''):
                    element = self.driver.find_element_by_link_text(additional_menu_I)
                    action.move_to_element(element).perform()

                if(additional_menu_II != ''):
                    element = self.driver.find_element_by_link_text(additional_menu_II)
                    action.move_to_element(element).perform()

                element.click()
                break

            except:
                counter_attempts = (counter_attempts - 1)

        if(counter_attempts == 0):
            raise('Não foi possivel interagir com o menu informado!')