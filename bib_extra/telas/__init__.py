from PySimpleGUI import PySimpleGUI as sg

font_Avi_Info = ('Arial Black Normal', 12)
font_info_fixa = ('Arial Black Normal', 16)
font_nome = ('Arial Negrito', 16)
font_geral = ('Arial Negrito', 14)
font_status = ('Arial Negrito', 12)


def tela_totem(users,filtro_pergunta,filtro_aviso,agenda_ge,agenda_au,cipa):
    """
    -> Monta ajusta layouts secundários e ajusta para a tela do totem

    :param users: recebe lista com o layout pre pronto
    :param filtro_perguntas: recebe lista com o layout pre pronto
    :param filtro_aviso: recebe lista com o layout pre pronto
    :param agenda_ge: recebe lista com o layout pre pronto
    :param agenda_au: recebe lista com o layout pre pronto
    :param cipa: recebe lista com o layout pre pronto
    :return: Layout completo da janela principal
    """
    #tema da janela
    sg.theme('DarkBlue9')

    #ajusta layout das agenda do auditório
    evento_audi = [
        [sg.Frame('',element_justification='c',vertical_alignment='c',expand_x=True,expand_y=True,
        layout=(
            [sg.Text('Eventos Auditório:',justification='c',font=font_geral,size=(18,1))],
            [sg.Frame('',layout=agenda_au,element_justification='c',
            key='-evento_au-',vertical_alignment='c',expand_x=True)]
        ))]
    ]

    #ajusta layout da agenda geral 
    evento_geral = [
        [sg.Frame('',element_justification='c',vertical_alignment='c',expand_x=True,expand_y=True,
        layout=(
            [sg.Text('Eventos Gerais:',justification='c',font=font_geral,size=(18,1))],
            [sg.Frame('',layout=agenda_ge, element_justification='c',
                    key='-evento_ge-',vertical_alignment='c',expand_x=True)]))]
    ]

    #faz a leitura da quantidade de usuários para ajustar o layout
    if len(users) == 1:
        box = [
            [sg.Column(layout=users[0],element_justification='c')]
        ]

    elif len(users) == 2:
        box = [
            [sg.Column(layout=users[0],element_justification='c'),
            sg.Column(layout=users[1],element_justification='c')]
            ]
    
    #ajusta layout de perguntas frequentes
    info_fixa =[
        [sg.Frame('',layout=filtro_pergunta,element_justification='c',key='-fixo-',
        expand_x=True, expand_y=True)]
    ]

    #ajusta layout de avisos
    info_variavel = [
        [sg.Frame('',layout=filtro_aviso,element_justification='c',key='-Variavel-',
        expand_x=True, expand_y=True)]
    ]
    
    #ajusta layout equipe CIPA suportando no máximo 6 pessoas como padrão
    eq_cipa =[
        [sg.Column(layout=cipa[0],element_justification='c'),
        sg.Column(layout=cipa[1],element_justification='c'),
        sg.Column(layout=cipa[2],element_justification='c')],

        [sg.Column(layout=cipa[3],element_justification='c'),
        sg.Column(layout=cipa[4],element_justification='c'),
        sg.Column(layout=cipa[5],element_justification='c'),
        ]
    ]

    #layout geral do totem
    layout = [

        #Primeira parte do layout ajusta e posiciona  os layouts de eventos
        [sg.Frame('',element_justification='c',expand_x=True, layout=(
            [sg.Text('Agenda Senac:',font=font_nome,justification='c')],
            [sg.HSeparator()],
            [sg.Column(layout=evento_audi,element_justification='c',expand_x=True,expand_y=True),
            sg.Column(layout=evento_geral,element_justification='c',expand_x=True,expand_y=True)]
        ))],

        #Segunda parte do layout ajusta e posiciona o layout da ti e perguntas frequentes
        [sg.Frame('',element_justification='c',expand_x=True,layout=(
            [sg.Text('Equipe TI:', justification='c',font=font_nome)],

            [sg.HSeparator()],
            [sg.Column(layout=box,element_justification='c',expand_x=True,
            vertical_alignment='c')],

            [sg.Column(layout = info_fixa,element_justification='c',expand_x=True)],
        ))],

        #Terceira parte do layout ajusta e encaixa o quadro de avisos
        [sg.Frame('',element_justification='c',expand_x=True,layout=(
            [sg.Text('Avisos:',font=font_nome,justification='c')],
            [sg.HSeparator()],
            [sg.Column(layout=info_variavel,element_justification='c',expand_x=True,
            key='-avisos-',visible=True)],
        ))],

        #quarta parte do layout ajusta e encaixa a comissão da CIPA
        [sg.Frame('',element_justification='c',expand_x=True,layout=(
            [sg.Text('Comissão CIPA:',font=font_nome,justification='c')],
            [sg.HSeparator()],
            [sg.Column(layout=eq_cipa,element_justification='c',expand_x=True)],
        ))]
    ]
    
    #retorna janela com todos os parâmetros necessários  
    return sg.Window('', finalize=True, size=(1000,1000), layout = layout,
    margins=(0,0),resizable=True,element_justification='c',keep_on_top=True,
    use_custom_titlebar=True,titlebar_background_color='#263859',titlebar_icon=(''),
    location=tuple(sg.user_settings_get_entry('-last position-', (None, None))))

def tela_popup_erro(texto):
    """
    -> Monta o

    :param texto: Recebe informação do erro ocorrido
    :return: Janela de erro com a informação do erro
    """

    #tema da janela
    sg.theme('DarkRed2')

    #layout principal da tela de erro
    layout = [
        [sg.Text(f'{texto}\nContate o Administrador!',font=font_geral)],
        [sg.Button('OK',font=font_geral,size=(5,1))]
    ]

    #retorna tela montada para exibição
    return sg.Window('ERRO!', finalize=True, size=(550,110), layout = layout,
    margins=(0,0), element_justification='c', icon= (r'icon\Control_Panel.ico'),
    text_justification='c',keep_on_top=True,
    location=tuple(sg.user_settings_get_entry('-last position-', (None, None))))

def tela_inicia_app():
    """
    -> Cria tela de loading
    :return: tela de loading e seus paramentos de atualização
    """

    sg.theme('DarkBlue9')

    layout =  [
        [sg.Text('Iniciando aplicação...',font=font_geral)],

        [sg.ProgressBar(100,orientation='h',size=(50,2),border_width=4,
        key='-progress-')],
        
        [sg.Text('',key='-info_user-',font=font_geral)]
    ]

    return sg.Window('Iniciando', finalize=True, size=(500,110), layout = layout,
    margins=(0,0), element_justification='c', icon= (r'icon\Control_Panel.ico'),
    text_justification='c',
    location=tuple(sg.user_settings_get_entry('-last position-', (None, None))))

def cria_layout_infos(informativos):
    """
    -> Cria pre layout das perguntas frequentes com base na lista recebida do banco de dados.
    :param informativos: Recebe lista de perguntas retiradas do banco de dados
    :return: lista de pre layout com parâmetros base e suas chaves 
    """
    #tema do layout
    sg.theme('DarkBlue9')

    #lista para adicionar linha a linha
    layout = list()

    #percorre lista de perguntas uma a uma
    for informativo in informativos:
        
        ajusta = [sg.Text(f'{informativo[1]}',font=font_info_fixa,justification='c'),
        sg.Text(f'{informativo[2]}',font=font_info_fixa,justification='c',
        key=(f'-{informativo[0]}-'))]

        layout.append(ajusta)

    #retorna lista completa com o pre layout
    return layout

def cria_layout_avisos(avisos):
    """
    -> Cria pre layout dos avisos com base na lista recebida do banco de dados.
    :param avisos: Recebe lista de dados retirada do banco de dados
    :return: lista com o pre layout e seus parâmetros e chaves
    """

    #tema do layout
    sg.theme('DarkBlue9')

    #lista para adicionar linha a linha
    layout = list()

    #percorre lista de avisos uma a uma
    for aviso in avisos:
        
        ajusta = [sg.Text(f'{aviso[1]}',font=font_Avi_Info,justification='c')]

        layout.append(ajusta)
    
    #retorna lista completa com o pre layout
    return layout

def cria_users(usuarios):
    """
    -> Cria pre layout de usuários do TI com base nos dados coletados do banco

    :param usuarios: Recebe lista de usuários coletadas do banco de dados
    :return: pre layout com suas informações e chaves
    """

    #tema layout
    sg.theme('DarkBlue9')

    #lista para adicionar user linha a linha
    layout = list()

    #percorre lista de user uma a uma e usando como base sua posição para criação da chave
    # para a alteração das informações

    for n ,user in enumerate(usuarios):
        
        user_status =[
            [sg.Text('',key=(f'-status_user{n}-'),font=font_status)],
            [sg.Text('Unidade:',font=font_status),sg.Text('',key=(f'-un_user{n}-'),font=font_status)],
            [sg.Text('Local:',font=font_status),sg.Text('',key=(f'-local_user{n}-'),font=font_status)]
        ]
        caixa_user = [
            [sg.Frame('',layout=(
                [sg.Text('',font=font_nome,key=(f'-nome_user{n}-'))],
                [sg.Image('',key=(f'-img_user{n}-'))],
                [sg.Text('',font=font_status,key=(f'-humor_user{n}-'))],
                [sg.Frame('',element_justification='c',layout=user_status,
                visible=True,key=(f'-status_g_user{n}-'))]

                ),element_justification='c')],
        ]

        layout.append(caixa_user)
    
    #retorna lista completa com o pre layout
    return layout

def cria_layout_eventos_au(eventos):
    """
    -> Cria pre layout de eventos do auditório conforme lista recebida

    :param eventos: Recebe lista de eventos coletadas do banco de dados
    :return: pre layout com os parâmetros de exibição
    """

    #tema layout
    sg.theme('DarkBlue9')
    
    #lista para adicionar evento linha a linha
    layout = list()

    #valida se lista recebida está vazia
    if len(eventos) > 0:
        for evento in eventos:

            ajusta = [sg.Text(f'{evento[1]}',font=font_Avi_Info,text_color='yellow',size=(5,1),
            key=(f'-data{evento[0]}-')),
            sg.Text(f'{evento[2]}',font=font_Avi_Info,key=(f'-auditorio{evento[0]}-'),size=(25,1),
            justification='c')]

            layout.append(ajusta)
        
        return layout
    
    # se lista estiver vazia retorna layout base
    else:
        return [sg.Text('Em breve...',font=font_Avi_Info,size=(30,1),justification='c')],

def cria_layout_eventos_ge(eventos):
    """
    -> Cria pre layout de eventos gerais conforme lista recebida
    :param eventos: Recebe lista de eventos gerais coletadas do banco de dados
    :return: pre layout com os parâmetros de exibição
    """
    #tema layout
    sg.theme('DarkBlue9')
    
    #lista para adicionar evento linha a linha
    layout = list()

    #valida se lista recebida está vazia
    if len(eventos) > 0:
        for evento in eventos:

            ajusta = [sg.Text(f'{evento[1]}',font=font_Avi_Info,text_color='yellow',size=(5,1),
            key=(f'-geral_d{evento[0]}-')),
            sg.Text(f'{evento[2]}',font=font_Avi_Info,key=(f'-geral{evento[0]}-'),size=(25,1),
            justification='c')]

            layout.append(ajusta)
        
        return layout
    
    # se lista estiver vazia retorna layout base
    else:
        return [sg.Text('Em breve...',font=font_Avi_Info,size=(30,1),justification='c')],

def cria_equipe_cipa(dados):
    """
    -> Cria pre layout da comissão da cipa conforme lista recebida
    :param dados: Recebe lista de membros conforme dados extraídos do banco de dados
    :return: pre layout com os parâmetros de exibição
    """
    #tema layout
    sg.theme('DarkBlue9')
    
    #lista para adicionar evento linha a linha
    layout = list()

    #percorre membro a membro para montar o layout
    for dado in dados:
        box_equipe =[
            [sg.Frame('',element_justification='c',layout=(
                [sg.Text(dado[1],font=font_status,size=(15,1),justification='c')],
                [sg.Image(dado[2])],
                [sg.Text(dado[3],font=font_status)]
            ))],
        ]
        
        layout.append(box_equipe)
    
    #retorna pre layout com as informações
    return layout