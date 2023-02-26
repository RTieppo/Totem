from os import makedirs, listdir,path,error

def cria_pasta_geral():
    '''
    -> Verifica se pasta principal existe se não faz a criação da mesma
    :return: True ou possível erro na criação da pasta
    '''

    try:
        #caminho padrão para a criação e validação da pasta
        valida_pasta = listdir(r'C:\Users\Public')

        #verifica se pasta ja existe
        if 'AppExpo' in valida_pasta:
            return True
        
        #caso não exista cria faz a criação da pasta
        else:
            makedirs(r'C:\Users\Public\AppExpo')
            return True
    
    except error:
        return 'Erro na criação da pasta'

def cria_pastas_user(dados):
    '''
    -> Faz a criação da/s pastas de users conforme lista recebida

    :param dados: Recebe lista de usuários coletados do banco de dados
    :return: True ou possível erro na criação das pastas
    '''

    try:
        #faz a leitura de individual de cada user disponível
        for dado in dados:
            #caminho geral para validação de user
            valida_pasta = listdir(r'C:\Users\Public\AppExpo')

            #caso pasta de user não exista na pasta geral faz a criação 
            if not str(dado[0]) in valida_pasta:
                caminho = path.join(r'C:\Users\Public\AppExpo',str(dado[0]))
                makedirs(caminho)
            
        return True
    
    except error:
        return 'Erro ao criar pasta user'