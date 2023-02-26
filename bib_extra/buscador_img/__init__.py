from os import path
import urllib.request
import urllib.error
import cv2

def baixa_img(dados):
    '''
    -> Faz download das imagens dos usuários uma a uma.

    :param dados: Recebe uma lista de links para realizar o download das img
    :return: True ou possível erro no download
    '''

    try:
        #caminho geral padrão
        caminho_geral = (r'C:\Users\Public\AppExpo')
        #lista de nomes para salvar as img
        #lista de nomes montada conforme sequencia de links já cadastrados no banco de dados
        nome_save = ('feliz.png','cansado.png','concentrado.png','pensativo.png','serio.png')

        #contadores de download e usuários que serão baixados
        conta= download = 0

        #faz a leitura de user a partir da lista recebida
        n_user = len(dados)

        while True:

            #verifica a quantidade de img baixadas, sempre serão 5 img de padrão
            #caso tenha 5 img baixadas add 1 ao numeres de user baixados
            #zerando o contador de img baixadas
            if conta == 5:
                download += 1
                conta = 0
            
            #verifica se já foi feito todos os download de img de usuários.
            elif download == n_user:
                return True

            #faz o download das img de usuários um a um
            else:
                
                #verifica se link existe ou foi cadastrado caso não esteja cadastrado
                #adiciona como 1 user já baixado e zera contador de img a serem baixadas
                if dados[download][conta+1] == None:
                    download +=1
                    conta = 0

                    #inicia o download das img 
                else:
                    #Realiza a unificação do do caminho para salvar
                    #unindo o caminho geral com a matricula do usuário e nome de salvamento
                    unifica = path.join(caminho_geral,str(dados[download][0]),nome_save[conta])
                    #cria um arquivo para baixar a img ou abre um existente para editar.
                    img_d = open(f"{unifica}",'wb')
                    #Abre a img pelo link e começa o download da mesma
                    img_d.write(urllib.request.urlopen(dados[download][conta+1]).read())
                    img_d.close()
                    #add como 1 img de 5 já baixada
                    conta += 1

    except urllib.error:
        return 'Erro ao baixar img'

def ajusta_img(matricula,ark,local):
    '''
    -> Faz ajuste de img de usuário para a exibição no totem
    :param matricula: Recebe matricula user 
    :param ark: Recebe caminho de img original
    :param local: recebe a matricula que é o nome da pasta de save do ark a ser ajustado
    :return: link de img ajustada ou erro no ajuste
    '''
    try:
        #Caminho geral de arquivos
        caminho_geral = (r'C:\Users\Public\AppExpo')

        #unifica caminho geral com matricula que é a pasta e o ark que é o link da img
        unifica_caminho = path.join(caminho_geral,matricula,ark)

        #abre e faz a leitura da img
        imagem = cv2.imread(unifica_caminho)

        #realiza reajuste da img de a cordo já com o valor pre definido
        imagem = cv2.resize(imagem,dsize=(100,100))

        #cria caminho e nome de arquivo para salvar ajuste
        temp = path.join(caminho_geral,local,'temp.png')

        #grava nova img
        cv2.imwrite(temp,imagem)

        #retorna link para apresentar img no totem
        return temp

    except Exception:
        return 'Erro na conversão de img'

def ajusta_img_padrão(img_p,local):
    '''
    -> Faz ajuste de img padrão para a exibição no totem
    :param img_p: Recebe link de img padrão já definida
    :param local: Recebe matricula do user para gravação na pasta do mesmo
    :return: link de img ajustada ou erro no ajuste
    '''
    
    try:
        #caminho geral predefinido
        caminho_geral = (r'C:\Users\Public\AppExpo')

        #abre img ignorando um dos canais de cores para manter a transparência 
        imagem = cv2.imread(img_p,-1)

        #reajusta a img para tamanho ja predefinido mantendo a transparência 
        imagem = cv2.resize(imagem,dsize=(100,100),interpolation = cv2.INTER_CUBIC)

        #cria caminho e nome para salvar a img base
        temp = path.join(caminho_geral,local,'base.png')

        #grava img base
        cv2.imwrite(temp,imagem,)

        #retorna link da img base para exibição no totem
        return temp

    except Exception:
        return 'Erro na conversão img base'

def ajusta_img_cipa(img):
    '''
    ->  Faz ajuste de img padrão da CIPA para a exibição no totem

    :param img: Recebe link de img padrão para ajuste
    :return: link de img ajustada ou erro durante o ajuste
    '''

    try:
        #caminho geral
        caminho_geral = (r'C:\Users\Public\AppExpo\cipa')

        #abre img para ajuste
        imagem = cv2.imread(img)

        #ajusta img para o tamanho já definido
        imagem = cv2.resize(imagem,dsize=(100,100))

        #cria caminho e nome de salvamento da nova img ajustada
        caminho = path.join(caminho_geral,f'{img}')

        #grava img ajustada
        cv2.imwrite(caminho,imagem)

        #retorna caminho para exibição no totem
        return caminho

    except Exception:
        return 'Erro na conversão img base'