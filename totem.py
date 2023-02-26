from PySimpleGUI import PySimpleGUI as sg
from configparser import ConfigParser
from time import sleep

from bib_extra import telas as t    
from bib_extra import sql_fun as sql
from bib_extra import criador_pasta as pasta
from bib_extra import buscador_img as img
from bib_extra import atualizador as atual


def start():

    try:
        #variável global para acesso ao banco de dados
        global conex_sql

        #Abre arquivo de config inicial para acessar o banco de dados
        config_init = ConfigParser()
        config_init.read('banco.ini')
        def_banco = dict(config_init['default'])

        #inicia class do banco de dados
        conex_sql = sql.BancoDeDados(host=def_banco['host'], user=def_banco['user'],
        database=def_banco['database'], password=def_banco['password'])
        #Conecta ao banco de dados e recebe o retorno do mesmo
        conecta_BDD = conex_sql.conectar()

        porcentagem = 0

        if conecta_BDD == True:
            #Se conectado ao banco de dados inicia a coleta de dados
            #e abre tela de inicialização
            janela_progress = t.tela_inicia_app()
            atual.atualiza_info(progress=porcentagem,window=janela_progress)

            #realiza a verificação das pasta de ark geral do app
            #caso não exista é criada uma
            verifica_pasta_geral = pasta.cria_pasta_geral()
            
            if verifica_pasta_geral == True:
                porcentagem += 2.5
                atual.atualiza_info(progress=porcentagem,window=janela_progress)
            
            else:
                janela_progress.close()
                return verifica_pasta_geral
            
            #consulta links de emoji para criação de pasta e download
            consulta_links = conex_sql.coleta_link()
            
            #Realiza a criação das pastas
            if not 'Erro' in consulta_links:

                #cria a pasta conforme a quantidade de user cadastrados
                criar_pastas = pasta.cria_pastas_user(consulta_links)

                if criar_pastas == True:
                    porcentagem += 2.5
                    atual.atualiza_info(progress=porcentagem,window=janela_progress)

                    #realiza a atualização das imagens conforme o user
                    baixa_imgs = img.baixa_img(dados=consulta_links)

                    if baixa_imgs == True:
                        porcentagem += 50
                        atual.atualiza_info(progress=porcentagem,window=janela_progress)
                    
                    else:
                        janela_progress.close()
                        return baixa_imgs
                
                else:
                    janela_progress.close()
                    return criar_pastas
            
            else:
                janela_progress.close()
                return consulta_links
                
            porcentagem = 100
            atual.atualiza_info(progress=porcentagem,window=janela_progress)

            #loop para manter e atualizar a tela de inicialização ativa
            while True:

                events,values = janela_progress.read(timeout=1000)

                if events == sg.WIN_CLOSED:
                    break

                #assim que evento de timeout for gerado todas as etapas foram concluídas
                #então fecha a janela e inicia a abertura da tela principal.
                elif events == sg.TIMEOUT_EVENT:
                    sg.user_settings_set_entry('-last position-', janela_progress.current_location())
                    janela_progress['-info_user-'].update('Acessando...',None,'green')
                    janela_progress.refresh()
                    sleep(1)
                    janela_progress.close()
                    return True
        
        else:
            return conecta_BDD
    
    except Exception as erro:
        janela_progress.close()
        return erro

def start_totem():
    try:

        #consultas ao banco para criação do layout
        consulta_status = conex_sql.consulta_status_geral()
        print(consulta_status)
        consulta_nomes = conex_sql.consulta_nome()
        coleta_pergunta = conex_sql.coleta_info()
        coleta_avisos = conex_sql.coleta_avisos()
        coleta_eventos_au = conex_sql.coleta_evento_au()
        coleta_eventos_ge = conex_sql.coleta_evento_ge()
        coleta_cipa = conex_sql.coleta_equipe_cipa()

        #variáveis a serem analisadas conforme seu retorno
        an_r_var = (consulta_status,consulta_nomes,coleta_pergunta,coleta_avisos,
        coleta_eventos_au,coleta_eventos_ge,coleta_cipa)

        #faz varreduras de erro nos retornos
        for variavel in an_r_var:
            if 'Erro' in str(variavel):
                return variavel

        #cria layout de usuários ativos do ti
        cria_user = t.cria_users(usuarios=consulta_status)

        #ajusta layout de perguntas frequentes do ti
        ajusta_perguntas = t.cria_layout_infos(informativos=coleta_pergunta)

        #ajusta layout de avisos do ti
        ajusta_avisos = t.cria_layout_avisos(avisos=coleta_avisos)

        #ajusta layout de eventos do auditório
        ajusta_eventos_au = t.cria_layout_eventos_au(coleta_eventos_au)

        #ajusta layout de eventos gerais
        ajusta_eventos_ge = t.cria_layout_eventos_ge(coleta_eventos_ge)

        #ajusta e cria layout equipe cipa
        ajusta_equipe_cipa = t.cria_equipe_cipa(coleta_cipa)
        
        #inicia tela com os paramentos de layout acima
        totem = t.tela_totem(users=cria_user,filtro_pergunta=ajusta_perguntas,
        filtro_aviso=ajusta_avisos,agenda_au=ajusta_eventos_au,agenda_ge=ajusta_eventos_ge,
        cipa=ajusta_equipe_cipa)

        #realiza primeira atualização da tela assim que abre totem
        atual.atualiza_totem_status(window=totem,dados=consulta_status,nomes=consulta_nomes)

        #deixa app em tela cheia
        totem.maximize()
        #desconecta do banco para validar novas entradas
        conex_sql.desconecta()

        #loop para manter a janela aberta
        while True:
            windows, events, values = sg.read_all_windows(timeout=10000)

            if windows == totem and events == sg.WIN_CLOSED:
                break

            #tela é atualizada conforme eventos de Timeout são gerados
            elif events == sg.TIMEOUT_EVENT:

                #ajuste de layout caso mudança
                ajuste_layout = False

                conecta_sql = conex_sql.reconecta()

                if conecta_sql == True:

                    #coleta novamente as informações para atualização
                    #reutilizando as mesma variáveis do inicio
                    consulta_status = conex_sql.consulta_status_geral()
                    consulta_nomes = conex_sql.consulta_nome()

                    #coleta novas info em novas variáveis preservando
                    #assim as variáveis antigas para comparação.
                    coleta_pergunta_n = conex_sql.coleta_info()
                    coleta_avisos_n = conex_sql.coleta_avisos()
                    coleta_eventos_au_n = conex_sql.coleta_evento_au()
                    coleta_eventos_ge_n = conex_sql.coleta_evento_ge()
                    coleta_cipa_n = conex_sql.coleta_equipe_cipa()

                    #faz a leitura de infos na pergunta e gera necessidade de refazer layout
                    #salva informações novas na variável antiga para nova comparação
                    if len(coleta_pergunta) > len(coleta_pergunta_n) or len(coleta_pergunta) < len(coleta_pergunta_n):
                        coleta_pergunta = coleta_pergunta_n
                        ajuste_layout = True
                    else:
                        #Realiza a mudança da resposta caso seja diferente da original
                        #salva informações novas na variável antiga para nova comparação
                        coleta_pergunta = coleta_pergunta_n
                        for atualiza in coleta_pergunta_n:
                            totem[f'-{atualiza[0]}-'].update(atualiza[2])

                    #faz a leitura de infos na pergunta e gera necessidade de refazer layout
                    if len(coleta_avisos) > len(coleta_avisos_n) or len(coleta_avisos) < len(coleta_avisos_n):
                        coleta_avisos = coleta_avisos_n
                        ajuste_layout = True
                    
                    elif coleta_avisos != coleta_avisos_n:
                        coleta_avisos = coleta_avisos_n
                        ajuste_layout = True
                    
                    #faz a leitura de infos dos eventos e gera necessidade de refazer layout
                    #salva informações novas na variável antiga para nova comparação
                    if len(coleta_eventos_au) > len(coleta_eventos_au_n) or len(coleta_eventos_au) < len(coleta_eventos_au_n):
                        coleta_eventos_au = coleta_eventos_au_n
                        ajuste_layout = True

                    else:
                        #Realiza a mudança da resposta caso seja diferente da original
                        #salva informações novas na variável antiga para nova comparação
                        coleta_eventos_au = coleta_eventos_au_n
                        for atualiza in coleta_eventos_au_n:
                            totem[f'-data{atualiza[0]}-'].update(atualiza[1])
                            totem[f'-auditorio{atualiza[0]}-'].update(atualiza[2])
                    
                    #faz a leitura de infos dos eventos e gera necessidade de refazer layout
                    #salva informações novas na variável antiga para nova comparação
                    if len(coleta_eventos_ge) > len(coleta_eventos_ge_n) or len(coleta_eventos_ge) < len(coleta_eventos_ge_n):
                        coleta_eventos_ge = coleta_eventos_ge_n
                        ajuste_layout = True

                    else:
                        #Realiza a mudança da resposta caso seja diferente da original
                        #salva informações novas na variável antiga para nova comparação
                        coleta_eventos_ge = coleta_eventos_ge_n
                        for atualiza in coleta_eventos_ge_n:
                            totem[f'-geral_d{atualiza[0]}-'].update(atualiza[1])
                            totem[f'-geral{atualiza[0]}-'].update(atualiza[2])


                    if ajuste_layout == True:

                        #Fecha janela antiga
                        totem.close()

                        #cria todos os layouts do zero com as novas informações
                        #assim garantindo que não haverá duplicatas de chave 
                        ajusta_perguntas = t.cria_layout_infos(informativos=coleta_pergunta_n)
                        ajusta_avisos = t.cria_layout_avisos(avisos=coleta_avisos_n)
                        cria_user = t.cria_users(usuarios=consulta_status)
                        ajusta_eventos_au = t.cria_layout_eventos_au(coleta_eventos_au_n)
                        ajusta_eventos_ge = t.cria_layout_eventos_ge(coleta_eventos_ge_n)
                        ajusta_equipe_cipa = t.cria_equipe_cipa(dados=coleta_cipa_n)

                        totem = t.tela_totem(users=cria_user,filtro_pergunta=ajusta_perguntas,
                        filtro_aviso=ajusta_avisos,agenda_au=ajusta_eventos_au,
                        agenda_ge=ajusta_eventos_ge,cipa=ajusta_equipe_cipa)

                        totem.maximize()
                    
                    #variáveis a serem analisadas conforme seu retorno
                    an_r_var = (consulta_status,consulta_nomes,coleta_pergunta_n,
                    coleta_avisos_n,coleta_cipa_n,coleta_eventos_au_n,
                    coleta_eventos_ge_n)

                    #faz nova varredura de erros no retorno
                    for variavel in an_r_var:
                        if 'Erro' in str(variavel):
                            totem.close()
                            return variavel

                    #realiza nova atualização conforme nova coleta de dados
                    atual.atualiza_totem_status(window=totem,dados=consulta_status,nomes=consulta_nomes)

                else:
                    return 'Erro ao acessar banco de dados'

                conex_sql.desconecta()
    
    except Exception:
        return 'Erro Fatal'

if __name__ == '__main__':
    inicia = start()

    if inicia == True:
        erro = start_totem()
        
        if 'Erro' in str(erro):
            janela_popup = t.tela_popup_erro(texto=erro)

            while True:
                events, values = janela_popup.read()
                
                if events == sg.WIN_CLOSED or 'OK':
                    break

    else:
        
        janela_popup = t.tela_popup_erro(texto=inicia)
        
        while True:
            events, values = janela_popup.read()
                
            if events == sg.WIN_CLOSED or 'OK':
                break