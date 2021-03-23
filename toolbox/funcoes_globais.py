# Coleção de imports
from toolbox.collection import *

# Definição de class
class funcoes_globais():
    def __init__(self, driver):
        self.driver = driver

# Catálogo de funções
    def remove_acentos(self, palavra):
        # Remove os acentos da String que for passada por parâmetro
        return unidecode(palavra)
    # Fim da função remove_acentos

    def gera_log(self, caminho_do_log, nome_do_arquivo, valor_a_inserir = ''):
        # Gera o log com base nos parâmetros passados
        if(valor_a_inserir != ''):    
            # Cria o diretorio 
            if(self.cria_diretorio(caminho_do_log.strip()) == False):
                return False
            # Abre o arquivo passado, se ele não existir tenta criar um
            try:
                try:
                    insere = open(caminho_do_log + '/' + nome_do_arquivo, 'a')
                    # Insere valor no arquivo
                    insere.writelines( valor_a_inserir.strip() + '\n')
                finally:
                    insere.close()
            except Exception:
                return False
            return True
        else:
            return False
    # Fim da função gera_log

    def verifica_diretorio_existe(self, caminho_do_diretorio=""):
        # Verifica se o diretório passado existe
        if(r"{}".format(caminho_do_diretorio.strip()) != ""):
            if(os.path.isdir(caminho_do_diretorio.strip()) == True):
                return True
        return False
    # Fim da função verifica_diretorio_existe

    def verifica_arquivo_existe(self, caminho_arquivo=""):
        # Verifica se o arquivo existe no camino passado nos parâmetros 
            if(r"{}".format(caminho_arquivo.strip()) != ""):
                if(os.path.isfile(caminho_arquivo.strip()) == True):
                    return True
            return False
    # Fim da função verifica_arquivo_existe

    def listar_arquivos_diretorio(self, caminho_diretorio, optional_extencao_arquivo = ''):
        # Lista o arquivo do diretório passado no parâmetro
        arquivos = []
        if(self.verifica_diretorio_existe(caminho_diretorio)== True):

            # Retorna todos os arquivos que existirem no diretório e nos subdiretórios do mesmo
            if(optional_extencao_arquivo == ""):
                for p, _, files in os.walk(os.path.abspath(caminho_diretorio)):
                    for file in files:
                        arquivos.append(os.path.join(p, file))

            # Retorna apenas os arquivos que contém a mesma extensão passada por parâmetro
            else:
                for p, _, files in os.walk(os.path.abspath(caminho_diretorio)):
                    for file in files:
                        extensaoDoArquivo = file[file.index("."):len(str(file))]
                        if(optional_extencao_arquivo in str(file) and len(optional_extencao_arquivo) == len(str(extensaoDoArquivo)) ):
                            arquivos.append(os.path.join(p, file))
        else:
            return "Diretório Inválido"
        return arquivos
    # Fim da função listar_arquivos_diretorio

    def cria_diretorio(self, caminho_diretorio = ""):
        # Cria um diretório no caminho passado no parâmetro
        if(caminho_diretorio.strip() != ""):
            if(self.verifica_diretorio_existe(caminho_diretorio.strip()) != True):

                # Tenta criar um diretório
                try:
                    os.mkdir(caminho_diretorio.strip());

                # Caso não consiga retorna uma mensagem de erro
                except:
                    raise Exception ("Processo de criação do diretorio " + caminho_diretorio.strip() + " falhou.")

                # Verifica se o diretório foi criado
                if (self.verifica_diretorio_existe(caminho_diretorio.strip()) == True):
                    return True
            else:
                return True
        else:
            raise Exception("Caminho para criar o diretorio raiz, não foi informado!")
        return False
    # Fim da função cria_diretorio

    def exclui_diretorio(self, caminho_diretorio=""):
        # Exclui o diretório informado
        # Verifica se o caminho foi passado e exclui o mesmo
        if(caminho_diretorio.strip() != ""):
            if (self.verifica_diretorio_existe(caminho_diretorio.strip()) == True):
                try:
                    shutil.rmtree(caminho_diretorio.strip(), ignore_errors=True)
                except:
                    raise Exception ("Processo de exclusão do diretorio " + caminho_diretorio.strip() + " falhou.")
                if (self.verifica_diretorio_existe(caminho_diretorio.strip())):
                    return False
                else:
                    return True
        else:
            raise Exception ("Caminho para excluir o diretorio raiz, não foi informado!")
        return False
    # Fim da função exclui_diretorio

    def exclui_arquivo(self, caminho_diretorio, nome_arquivo):
        # Exclui o arquivo do caminho passado no parâmetro
        # Verifica se o caminho existe
        try:
            if (caminho_diretorio.strip() == ""):
                return False
            if (nome_arquivo.strip() == ""):
                return False
            if (self.verifica_diretorio_existe(caminho_diretorio) == False):
                return False
            if (self.verifica_arquivo_contem_diretorio(caminho_diretorio, nome_arquivo) == False):
                return False
            os.remove(caminho_diretorio.upper() +'/'+ nome_arquivo.upper())
            return True
        except:
            return False
    # Fim da função exclui_arquivo

    def verifica_arquivo_contem_diretorio(self, caminho_diretorio, nome_arquivo):
        # Verifica se o arquivo existe no diretório

        if(self.verifica_diretorio_existe(caminho_diretorio)== False):
            return False

        if(nome_arquivo == ""):
            return False

        for p, _, files in os.walk(os.path.abspath(caminho_diretorio)):
            for file in files:
                if(str(file).upper() == nome_arquivo.upper()):
                    return True

        return False
    # Fim da função verifica_arquivo_contem_diretorio

    def retorna_data_hora_sem_caracter(self):
        # Retorna a data e a hora atual sem caracteres
        data_atual = datetime.datetime.now()
        return(str(data_atual)[:str(data_atual).index(".")].replace("-", "").replace(":", "").replace(" ", ""))
    # Fim da função retorna_data_hora_sem_caracter

    def retorna_mes_por_escrito(self, mes_informado):
        # Retorna o mês que foi informado 
        if (mes_informado == 1):
            mes_por_escrito = "JANEIRO"
        elif (mes_informado == 2):
            mes_por_escrito = "FEVEREIRO"
        elif (mes_informado == 3):
            mes_por_escrito = "MARÇO"
        elif (mes_informado == 4):
            mes_por_escrito = "ABRIL"
        elif (mes_informado == 5):
            mes_por_escrito = "MAIO"
        elif (mes_informado == 6):
            mes_por_escrito = "JUNHO"
        elif (mes_informado == 7):
            mes_por_escrito = "JULHO"
        elif (mes_informado == 8):
            mes_por_escrito = "AGOSTO"
        elif (mes_informado == 9):
            mes_por_escrito = "SETEMBRO"
        elif (mes_informado == 10):
            mes_por_escrito = "OUTUBRO"
        elif (mes_informado == 11):
            mes_por_escrito = "NOVEMBRO"
        elif (mes_informado == 12):
            mes_por_escrito = "DEZEMBRO"
        else:
            return "Mês informado inválido"
        return mes_por_escrito
    # Fim da função retorna_mes_por_escrito

    def retorna_indice_mes(self, mes_informado):
        # Retorna o índice do mês informado
        if (mes_informado.upper() == 'JANEIRO'):
            idx_mes_selecionado = 1
        elif (mes_informado.upper() == 'FEVEREIRO'):
            idx_mes_selecionado = 2
        elif (mes_informado.upper() == 'MARÇO'):
            idx_mes_selecionado = 3
        elif (mes_informado.upper() == 'ABRIL'):
            idx_mes_selecionado = 4
        elif (mes_informado.upper() == 'MAIO'):
            idx_mes_selecionado = 5
        elif (mes_informado.upper() == 'JUNHO'):
            idx_mes_selecionado = 6
        elif (mes_informado.upper() == 'JULHO'):
            idx_mes_selecionado = 7
        elif (mes_informado.upper() == 'AGOSTO'):
            idx_mes_selecionado = 8
        elif (mes_informado.upper() == 'SETEMBRO'):
            idx_mes_selecionado = 9
        elif (mes_informado.upper() == 'OUTUBRO'):
            idx_mes_selecionado = 10
        elif (mes_informado.upper() == 'NOVEMBRO'):
            idx_mes_selecionado = 11
        elif (mes_informado.upper() == 'DEZEMBRO'):
            idx_mes_selecionado = 12
        else:
            return 'Mês informado inválido'
        return idx_mes_selecionado
    # Fim da função retorna_indice_mes

    def gerador_de_cpf(self):
        # Gera um CPF aleatório e válido
        n1 = random.randrange(10)
        n2 = random.randrange(10)
        n3 = random.randrange(10)
        n4 = random.randrange(10)
        n5 = random.randrange(10)
        n6 = random.randrange(10)
        n7 = random.randrange(10)
        n8 = random.randrange(10)
        n9 = random.randrange(10)

        a1 = n9 * 2
        a2 = n8 * 3
        a3 = n7 * 4
        a4 = n6 * 5
        a5 = n5 * 6
        a6 = n4 * 7
        a7 = n3 * 8
        a8 = n2 * 9
        a9 = n1 * 10

        d1 = a1 + a2 + a3 + a4 + a5 + a6 + a7 + a8 + a9
        d1 = 11 - round(d1 % 11)

        # Caso d1 seja maior que 10 ele é elevado a 0, para que não ocorra um erro
        if d1 >= 10:
            d1 = 0

        a1 = d1 * 2
        a2 = n9 * 3
        a3 = n8 * 4
        a4 = n7 * 5
        a5 = n6 * 6
        a6 = n5 * 7
        a7 = n4 * 8
        a8 = n3 * 9
        a9 = n2 * 10
        a10 = n1 * 11

        d2 = a1 + a2 + a3 + a4 + a5 + a6 + a7 + a8 + a9 + a10
        d2 = 11 - round(d2 % 11)

        if d2 >= 10:
            d2 = 0

        return "{}{}{}{}{}{}{}{}{}{}{}".format(n1, n2, n3,  n4, n5, n6,  n7, n8, n9,  d1, d2)
    # Fim da função gerador_de_cpf

    def remove_caracteres_especiais(self, string):
        # Remove os caracteres especiais de uma String
        return re.sub('[A-Za-z0-9 ÇçÁÀÃÂáàãâÉÈÊéèêÍÌÎíìîÓÒÕÔóòõôÚÙÛúùû]+', '', string)
    # Fim da função remove_caracteres_especiais

    def pega_extensao_arquivo(self, file_name):
        # Retorna a extensão do arquivo passado ou None se ele não tiver extensão 
        file_name = file_name[::-1]

        # Verifica se existe . no nome do arquivo
        if '.' in file_name[0:6]:
            try:
                # Tenta capturar a extensão do arquivo
                file_name = file_name[0:6][::-1]
                file_name = file_name.split('.')
                index = len(file_name)

                # Retorna a extensão do arquivo
                if file_name[index-1] == '':
                    return None
                return str(file_name[index-1])
            except:
                return None
        else:
            return None
    # Fim da função do pega_extensao_arquivo

    def registrar_evidencia(self,
                            optional_path_screenshot = '{}/artefact/images/evidence_image.png'.format(os.getcwd()),
                            optional_path_file = '{}/artefact/documents/evidence_text.json'.format(os.getcwd()),
                            optional_text_file = None):
        # Registra a evidencia com um arquivo de texto e um registro de imagem
        # *passar o caminho completo nos "opcional_path"

        # Verifica se o arquivo possui extensão
        if self.pega_extensao_arquivo(optional_path_file) == None:
            raise Exception('O arquivo que você informou, não contém uma extensão válida: {}'.format(optional_path_file))
        if self.pega_extensao_arquivo(optional_path_screenshot) == None:
            raise Exception('O arquivo que você informou, não contém uma extensão válida: {}'.format(optional_path_screenshot))

        # Cria o arquivo
        try:
            arq = open(optional_path_file, 'a')
            arq.write("{}\n".format(optional_text_file))
            arq.close()
        except:
            raise Exception('Não foi possível criar o arquivo: {}'.format(optional_path_file))

        # Realizando o print da tela
        try:
            self.driver.get_screenshot_as_file(optional_path_screenshot)
        except:
            raise Exception('Não foi possível criar o arquivo: {}'.format(optional_path_file))
    # Fim da função registrar_evidencia