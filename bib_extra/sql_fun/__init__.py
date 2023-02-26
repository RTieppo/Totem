import mysql.connector
from mysql.connector import Error


class BancoDeDados:

    def __init__(self,host,user, database, password):
        '''
        -> Inicia a class para conexão ao banco de dados e suas consultas.

        :param host: Recebe o ip do banco de dados
        :param user: Recebe o usuário que vai ser usado para acesso
        :param database: Recebe a info de qual banco de dados vai ser usado
        :param password: Recebe a senha do usuário que vai acessar o banco de dados
        :return: Sem retorno
        '''
        self.host = host
        self.user = user
        self.database = database
        self.password = password
    
    def conectar(self):
        '''
        -> Faz a conexão ao banco de dados com os paramentos de inicialização através do self
        :return: True, erro de conexão ou erro de conexão não especificado
        '''

        #variável global para acessar e conectar ao banco de dados 
        global conectar

        try:

            #realiza conexão ao bando de dados com os parâmetros iniciados pelo self
            conectar = mysql.connector.connect(host = self.host ,user = self.user,
            database = self.database, password = self.password)

            #valida se consegui conexão
            if conectar.is_connected():
                return True
        
        #caso não tenha conectado ou outro erro não previsto aconteça retorna um erro genérico
        #a partir desse ponto.
            else:
                return 'Erro de conexão'
        
        except Error:
            return 'Erro ao conectar no servidor'
    
    def desconecta(self):
        '''
        -> Realiza a desconexão do banco de dados.

        :return: True ou Erro ao desconectar do servidor
        '''

        try:

            #valida se ainda tem conexão
            if conectar.is_connected():

                #realiza desconexão do banco de dados
                conectar.close()
                return True
            
            else:
                return True
        
        except Error:
            return 'Erro ao desconectar do servidor'

    def reconecta(self):
        '''
        -> Realiza a reconexão ao banco de dados.
        
        :return: True ou Erro ao reconectar no servidor
        '''

        try:

            #verifica se existe conexão com o banco de dados
            if conectar.is_connected():
                return True
            
            #caso não esteja conectado ao banco de dados realiza a conexão
            else:
                conectar.connect()
                
                #valida se realmente a conexão foi realizada
                if conectar.is_connected():
                    return True
                
                else:
                    return 'Erro ao reconectar no servidor'
                
        except Error:
            return 'Erro ao reconectar no servidor'

    def consulta_status_geral(self):
        '''
        -> Realiza a consulta a tabela de status_atendimento do banco de dados.

        :return: Uma lista com os status dos usuários cadastrados no banco de dados,
        caso ocorra algum erro o mesmo é informado
        '''
        try:

            #Verifica se está conectado ao banco de dados
            if conectar.is_connected():

                #comando para a consulta
                consulta = ('select * from status_atendimento;')
                #cria comando de execução
                cursor = conectar.cursor()
                #executa consulta
                cursor.execute(consulta)
                #grava informações obtida das consulta
                linhas = cursor.fetchall()

                #retorna lista com as informações
                return linhas
            
            else:
                return 'Erro de conexão'

        except Error:
            return 'Erro ao buscar informações'

    def consulta_nome(self):
        '''
        -> Realiza consulta dos nomes dos usuários cadastrados no banco de dados.

        :return: lista com os nomes dos usuários ou possível erro
        '''
        try:

            #Valida se está conectado ao banco de dados
            if conectar.is_connected():

                #comando para a consulta
                consulta = ('select id from login;')
                #cria comando de consulta
                cursor = conectar.cursor()
                #executa comando de consulta
                cursor.execute(consulta)
                #grava informações obtida das consultas
                linhas = cursor.fetchall()

                #retorna lista de nomes
                return linhas
            
            else:
                return 'Erro de conexão'

        except Error:
            return 'Erro na consulta nome'
    
    def coleta_link(self):
        '''
        -> Realiza coleta e consulta aos links para download de images.

        :return: Lista de links das imagens ou possível erro durante a consulta
        '''

        try:
            #Verifica conexão
            if conectar.is_connected():
                #comando para a consulta
                info = ('select * from emoji;')
                #cria comando de consulta
                cursor = conectar.cursor()
                #executa a consulta
                cursor.execute(info)
                #grava informações obtidas da consulta
                linhas = cursor.fetchall()
                
                #retorna lista com os links
                return linhas
            
            else:
                return 'Erro de conexão'
                        
        except Error:
            return 'Erro ao coletar links'
    
    def coleta_info(self):
        '''
        -> Realiza coleta de perguntas frequentes.

        :return: lista com as perguntas ou possível erro na consulta
        '''

        try:

            #Verifica conexão
            if conectar.is_connected():
                #comando para a consulta
                consulta = ('select * from perguntas_f;')
                #cria comando de consulta
                cursor = conectar.cursor()
                #executa a consulta
                cursor.execute(consulta)
                #grava as informações da consulta
                linha = cursor.fetchall()

                #retorna lista com as informações
                return linha
            
            else:
                return 'Erro de conexão'

        except Error:
            return 'Erro ao coletar info'
    
    def coleta_avisos(self):
        '''
        -> Realiza a coleta de avisos.

        :return: lista com os avisos cadastrados no banco de dados
        '''

        try:
            #Verifica a conexão
            if conectar.is_connected():

                #comando para a consulta
                consulta = ('select * from avisos;')
                #cria comando de consulta
                cursor = conectar.cursor()
                #executa consulta
                cursor.execute(consulta)
                #grava informações obtidas da consulta
                linha = cursor.fetchall()

                #retorna lista com as informações
                return linha
            
            else:
                return 'Erro de conexão'

        except Error:
            return 'Erro ao coletar aviso'
            
    def coleta_evento_au(self):
        '''
        -> Realiza a coleta das informações de eventos do auditório.

        :return: Lista com os eventos cadastrados ou possível erro na consulta
        '''
        try:

            #Verifica conexão
            if conectar.is_connected():

                #comando para a consulta
                consulta = (f'select * from eventos_au;')
                #cria comando de consulta
                cursor = conectar.cursor()
                #executa consulta
                cursor.execute(consulta)
                #grava informações obtidas durante a consulta
                linhas = cursor.fetchall()

                #retorna informações obtidas durante a consulta
                return linhas
            
            else:
                return 'Erro de conexão'


        except Error:
            return 'Erro ao buscar os eventos_au'
    
    def coleta_evento_ge(self):
        '''
        -> Realiza a consulta dos eventos gerais da unidade 

        :return: lista com os eventos gerais ou possível erro durante a consulta
        '''
        try:

            #Verifica conexão
            if conectar.is_connected():

                #comando para a consulta
                consulta = ('select * from eventos_ge;')
                #cria comando de consulta
                cursor = conectar.cursor()
                #executa consulta
                cursor.execute(consulta)
                #grava informações obtidas da consulta
                linhas = cursor.fetchall()

                #retorna lista de eventos do banco de dados
                return linhas
            
            else:
                return 'Erro de conexão'


        except Error:
            return 'Erro ao buscar os eventos_ge'
    
    def coleta_equipe_cipa(self):
        """
        -> Realiza a consulta da equipe da CIPA

        :return: Lista com os membros da CIPA ou possível erro durante consulta
        """
        try:
            #Verifica conexão
            if conectar.is_connected():

                #comando de consulta
                consulta = ('select * from equipe_cipa;')
                #cria comando de consulta
                cursor = conectar.cursor()
                #executa consulta
                cursor.execute(consulta)
                #grava informações obtidas da consulta
                linhas = cursor.fetchall()

                #retorna lista com as informações coletadas
                return linhas

            else:
                return 'Erro de conexão'

        except Error:
            return 'Erro ao buscar equipe CIPA'