# Coleção de imports
from toolbox.collection import *

# Definição de class
class select_type(Enum):
    seleciona_por_index = 1
    seleciona_por_texto = 2
    seleciona_por_valor = 3

class funcoes_selenium():
    def __init__(self):
        super().__init__()

# Catálogo de funções
    def selecionar_item_da_lista(self, by, elemento, select_type, options, optional_elemento = None, optional_parar_aplicacao_no_erro = True):
        # Seleciona um item de uma lista
        # dropdown list ou um combobox */
        # Essa função usa a classe select_type para dar a opções ao usuário
        try:
            if (optional_elemento != None):
                elemento_selecionado = optional_elemento.find_element(by,elemento)
            else:
                elemento_selecionado = self.driver.find_element(by,elemento)
            if (select_type.value == 1):
                try:
                    Select(elemento_selecionado).select_by_index(options)
                except Exception:
                    raise Exception("[Por favor, informe um indice valido do combo para selecionar o item.]")
            elif (select_type.value == 2):
                Select(elemento_selecionado).select_by_visible_text(str(options))
            elif (select_type.value == 3):
                Select(elemento_selecionado).select_by_value(options)
            else:
                raise Exception("[Não foi possível selecionar o item na lista.]")
        except Exception:
            if (optional_parar_aplicacao_no_erro == True):
                if (optional_elemento != None):
                    raise Exception("[Não foi possível interar com o objeto: (Name:"+optional_elemento.get_attribute("name") + ", ID: "+ optional_elemento.get_attribute("id") + ", Class: "+ optional_elemento.get_attribute("class") +")]")
                else:
                    raise Exception("[Não foi possível interar com o objeto: " + elemento +" ]")
    # Fim da função selecionar_item_da_lista

    def digitar_texto(self,by,nome_objeto,text,optional_elemento = None,optional_parar_aplicacao_no_erro = True):
        # Digita uma String em um campo selecionado

        elemento = None

        # Verifica se o objeto foi passado e se ele é acessivel
        try:
            if(optional_elemento is None):
                elemento = self.driver.find_element(by,nome_objeto)                                  
            else:
                elemento = optional_elemento.find_element(by,nome_objeto)
            # Verifica se o elemento está disponível para digitar, se sim, digita o texto passado por parâmetro
            if(elemento.is_displayed and elemento.is_enabled()):
                elemento.clear()    
                elemento.send_keys(text.strip())
        except Exception:
            if (optional_parar_aplicacao_no_erro == True):
                if(optional_elemento != None):
                    raise Exception("Não foi possível interar com o objeto: (Name: " + optional_elemento.get_attribute("name") + ", ID: "+ optional_elemento.get_attribute("id") + ", Class: "+ optional_elemento.get_attribute("class") +")]")
                else:
                    raise Exception("[ Não foi possível interagir com o objeto: " + nome_objeto +" ]\n")
    # Fim da função digitar_texto

    def click(self, by, nome_objeto, optional_elemento = None, optional_parar_aplicacao_no_erro = True):
        # Clica no elemento passado por parâmetros
        elemento = None
        action = ActionChains(self.driver)

        # Procura o elemento e se for possível clica nele
        try: 
            if (optional_elemento == None):
                elemento = self.driver.find_element(by,nome_objeto)
            else:
                elemento = optional_elemento.find_element(by,nome_objeto)
            # Verifica se o elemento passado está disponível para digitar, se sim, clica no mesmo
            if(elemento != None and elemento.is_displayed and elemento.is_enabled()):
                action.move_to_element(elemento).perform()
                self.driver.execute_script("arguments[0].scrollIntoView(true);", elemento)
                elemento.click()
        except Exception:
            if(optional_parar_aplicacao_no_erro == True):
                if(optional_elemento != None):
                    raise Exception("[Não foi possível interar com o objeto: (Name: " + optional_elemento.get_attribute("name") + ", ID: "+ optional_elemento.get_attribute("id") + ", Class: "+ optional_elemento.get_attribute("class") +")]")
                else:
                    raise Exception("[ Não foi possível manipular o objeto: " + nome_objeto +" ]")
    # Fim da função click

    def troca_frame(self, nome_frame, optional_parar_aplicacao_no_erro = True): 
        # Troca de HTML na mesma página
        try:
            self.driver.switch_to.frame(str(nome_frame))
        except:
            if (optional_parar_aplicacao_no_erro == True):
                raise Exception("[Não foi possível realizar a troca do frame para: " + str(nome_frame) + "]")
    # Fim da função troca_frame

    def verifica_elemento(self, by, nome_do_elemento, optional_elemento = None):
        # Verifica se o elemento existe na página e retorna o mesmo
        elemento = None
        action = ActionChains(self.driver)

        if (optional_elemento == None):
            elemento = self.driver.find_element(by, nome_do_elemento)                    
        else:
            elemento = optional_elemento.find_element(by, nome_do_elemento)

        # Procura o elemento
        try:    
            action.move_to_element(elemento).perform()
            self.driver.execute_script("arguments[0].scrollIntoView(true);", elemento)
            if(elemento != None and elemento.is_displayed and elemento.is_enabled()): 
                return elemento                    
        except:
            pass
        return None
    # Fim da função verifica_elemento

    def aguardar_enquanto_pagina_carrega(self, optional_parar_aplicacao_no_erro = False):
        # Aguarda a página carregar para executar os próximos comandos
        page_state = self.driver.execute_script('return document.readyState;')
        return page_state == 'complete'
    # Fim da função aguardar_enquanto_pagina_carrega

    def troca_janela (self, titulo_janela_popup):
        # Troca a janela atual por outra requisitada
        janela_encontrada = False
        nova_janela = None

        # Verifica em qual janela está e troca se necessário
        try:
            nova_janela = self.driver.window_handles[1]
            if(nova_janela != None):
                self.driver.switch_to.window(nova_janela)
                self.driver.maximize_window()
                titulo2=self.driver.title
            if(titulo2 == titulo_janela_popup):                
                janela_encontrada = True   
        except Exception:
            if(janela_encontrada == False):
                raise Exception("[ERRO] Não foi possível trocar de Janela : {}".format(titulo2))
    # Fim da função troca_janela
    
    
    def aguarda_elemento_para_interagir(self, by, nome_do_elemento, optional_elemento = None, optional_numero_tentativas = 30):
        # Verifica se o elemento existe na página e retorna o mesmo
        elemento = None
        action = ActionChains(self.driver)
        contador = optional_numero_tentativas

        if (optional_elemento == None):
            elemento = self.driver.find_element(by, nome_do_elemento)                    
        else:
            elemento = optional_elemento.find_element(by, nome_do_elemento)

        # Procura o elemento
        while contador >= 0:
            try:    
                action.move_to_element(elemento).perform()
                self.driver.execute_script("arguments[0].scrollIntoView(true);", elemento)
                if(elemento != None and elemento.is_displayed and elemento.is_enabled()): 
                    return elemento                    
            except:
                contador = contador - 1
                time.sleep(1)
                        
        return None
    # Fim da função verifica_elemento
    
    def elemento_esta_visivel(self, by, elemento, optional_numero_de_tentativas = 30):
        # Este método tem como função, fazer um numero determinado de tentativas e verificar se o objeto está visivel na tela

        numero_tentativas = optional_numero_de_tentativas;

        if(self.elemento_esta_habilitado(by, elemento)):
            while (numero_tentativas >= 0):
                try:
                    if (self.driver.find_element(by, elemento) != None):
                        return self.driver.find_element(by, elemento).is_displayed                    
                except:
                    pass

                if(numero_tentativas >= 0):
                    time.Sleep(1)

                numero_tentativas = numero_tentativas - 1

        return False
    # ElementoEstaVisivel
    
    def elemento_esta_habilitado(self, by, elemento, optional_numero_de_tentativas = 30):
        numero_tentativas = optional_numero_de_tentativas;

        while (numero_tentativas >= 0):
            try:
                if (self.driver.FindElements(by, elemento) != None):
                    return self.driver.find_element(by, elemento).is_enabled()                
            except:
                pass

            time.sleep(1);
            numero_tentativas = numero_tentativas - 1

        return False;
    # ElementoEstaHabilitado