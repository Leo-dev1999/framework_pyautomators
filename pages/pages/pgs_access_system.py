# Coleção de imports
from toolbox.collection import *
from pages.navigations.nvg_access_system import *
from toolbox.funcoes_csf import funcoes_csf
from toolbox.funcoes_globais import funcoes_globais
from toolbox.funcoes_selenium import select_type
from toolbox.funcoes_selenium import funcoes_selenium

# Definição de class
class access_system(funcoes_csf, funcoes_globais, funcoes_selenium):
    def __init__(self, driver):
        self.driver = driver

# Catálogo de funções
    def efetua_login(self):

        try:
            # Variaveis
            mensagem = ''

            # Insere as informações de login no campo usuario
            self.digitar_texto(by.ID, 'LoginModel_Usuario', dic_login['usuario'])

            # Insere as informações de password no campo senha
            self.digitar_texto(by.ID, 'LoginModel_Senha', dic_login['senha'])

            # Marca o botão de mudar dominio
            self.click(by.ID, 'rdDominio')

            # Insere as informações de domain no campo dominio
            self.digitar_texto(by.ID, 'LoginModel_Dominio', dic_login['dominio'])

            # Clica no botão entrar
            self.click(by.ID, 'btnEfetuarLogin')


            # Seleciona a unidade que sera acessada pelo sistema
            self.selecionar_item_da_lista(by.ID, 'LoginModel_Hierarquia', select_type.seleciona_por_texto, dic_login['unidade'])

            # Clica no botão avançar
            self.click(by.ID, 'btnConcluirAutenticacao')
        except Exception as error:
            mensagem = str(self.verifica_elemento(by.ID, 'validationSummary').text)
            self.registrar_evidencia('artefact/images/falha_login.png', 
                                     'artefact/documents/fluxo_parcele_facil.json', 
                                      mensagem)
            raise('Erro ao realizar a rotina de login. \n Detalhes do erro: {}'.format(error))


    def efetua_logoff(self):

        try:
            # Finaliza Atendimento
            self.click(by.ID, 'icl_FinalizarCliente')

            # Clica no botão Sim do pop-up
            for elemento in self.driver.find_elements(by.TAG_NAME, 'button'):
                try:
                    if(str(elemento.text) == "Sim"):
                        elemento.click()
                        break
                except:
                    pass

            # Clica no botão logoff
            self.click(by.ID, 'logoff')

            # Clica no botão sim do pop-up
            self.click(by.XPATH, "//input[@value='Sim']")
    
        except Exception as error:
            raise('Erro ao realizar a rotina de logoff. \n Detalhes do erro: {}'.format(error))