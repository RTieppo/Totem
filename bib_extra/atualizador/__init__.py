from time import sleep
from bib_extra import buscador_img

def atualiza_info(progress,window):
        '''
        -> Faz a atualização das informações da tela de progresso.

        :param progress: Recebe valor int da porcentagem
        :param window: Recebe as informações da janela para atualização
        :return: Sem retorno.
        '''

        window['-progress-'].update(progress)
        window['-info_user-'].update(f'{progress}%',None,'yellow')
        window.refresh()
        sleep(0.5)

def atualiza_totem_status(window,dados,nomes):
        '''
        -> Faz a atualização das informações da janela principal do totem.
        conforme quantidade de usuários, programa suporta até 4 usuários
        até o momento foi adequando para até duas pessoas.

        :param window: Recebe as informações da janela para atualização
        :param dados: Recebe lista de dados dos usuários para a atualização das informações na tela
        :param nomes: Recebe lista de nomes para atualização na tela
        :return: Sem retorno
        '''

        if len(dados) == 1:
                user = dados[0]
                nome = str(nomes[0][0]).split('.')

                if user[2] == 'Ferias':
                        window['-nome_user0-'].update(nome[0].capitalize())
                        window['-status_g_user0-'].update(visible=False)
                        ajusta_img = buscador_img.ajusta_img_padrão(img_p=r'img_base\Ferias.png',local=f'{user[0]}')
                        window['-img_user0-'].update(ajusta_img)
                        window['-humor_user0-'].update('Férias')
                
                else:
                        #verifica se user 0 está já começou a trabalhar
                        if user[1] == 'Entrada':

                                #verifica se user 0 está no horário de intervalo
                                if user[2] == 'Intervalo':
                                        #atualiza nome user 0
                                        window['-nome_user0-'].update(nome[0].capitalize())
                                        
                                        #ajusta img padrão para atualizar no totem
                                        ajusta_img = buscador_img.ajusta_img_padrão(img_p=r'img_base\intervalo.png',
                                        local=f'{user[0]}')
                                        #atualiza img
                                        window['-img_user0-'].update(ajusta_img)
                                        #apaga o humor
                                        window['-humor_user0-'].update('')

                                        #atualiza status geral
                                        window['-status_user0-'].update(user[2])
                                        window['-un_user0-'].update(user[3])
                                        window['-local_user0-'].update(user[4])
                                        window.refresh()


                                else:   
                                        #atualiza nome user 0
                                        window['-nome_user0-'].update(nome[0].capitalize())

                                        #ajusta img do user de acordo com o humor
                                        ajuste_img = buscador_img.ajusta_img(matricula=str(user[0]),
                                        ark=(f'{user[5]}.png'),local=str(user[0]))
                                        #Atualiza img e humor 
                                        window['-img_user0-'].update(ajuste_img)
                                        window['-humor_user0-'].update(user[5])

                                        #atualiza status geral
                                        window['-status_user0-'].update(user[2])
                                        window['-un_user0-'].update(user[3])
                                        window['-local_user0-'].update(user[4])

                                        #deixa status geral visível caso user 0 tenha saído ou retornado de saída
                                        window['-status_g_user0-'].update(visible=True)
                                        window.refresh()
                                        
                        else:   
                                #atualiza nome user 0
                                window['-nome_user0-'].update(nome[0].capitalize())

                                #ajusta img padrão para atualizar no totem
                                ajusta_img = buscador_img.ajusta_img_padrão(img_p=r'img_base\descanso.png',
                                local=f'{user[0]}')

                                #atualiza status geral
                                window['-img_user0-'].update(ajusta_img)
                                window['-humor_user0-'].update('Descansando')

                                #oculta status geral caso user não esteja 
                                window['-status_g_user0-'].update(visible=False)


        elif len(dados) == 2:

                #realiza a divisão das info recebidas através das lista
                user_0 = dados[0]
                nome_0 = str(nomes[0][0]).split('.')
                user_1 = dados[1]
                nome_1 = str(nomes[1][0]).split('.')

                #verifica se user 0 está de ferias
                if user_0[2] == 'Ferias':

                        window['-nome_user0-'].update(nome_0[0].capitalize())
                        window['-status_g_user0-'].update(visible=False)
                        ajusta_img = buscador_img.ajusta_img_padrão(img_p=r'img_base\Ferias.png',local=f'{user_0[0]}')
                        window['-img_user0-'].update(ajusta_img)
                        window['-humor_user0-'].update('Férias')

                else:   
                        #verifica se user 0 está já começou a trabalhar
                        if user_0[1] == 'Entrada':

                                #verifica se user 0 está no horário de intervalo
                                if user_0[2] == 'Intervalo':
                                        #atualiza nome user 0
                                        window['-nome_user0-'].update(nome_0[0].capitalize())
                                        
                                        #ajusta img padrão para atualizar no totem
                                        ajusta_img = buscador_img.ajusta_img_padrão(img_p=r'img_base\intervalo.png',
                                        local=f'{user_0[0]}')
                                        #atualiza img
                                        window['-img_user0-'].update(ajusta_img)
                                        #apaga o humor
                                        window['-humor_user0-'].update('')

                                        #atualiza status geral
                                        window['-status_user0-'].update(user_0[2])
                                        window['-un_user0-'].update(user_0[3])
                                        window['-local_user0-'].update(user_0[4])
                                        window.refresh()


                                else:   
                                        #atualiza nome user 0
                                        window['-nome_user0-'].update(nome_0[0].capitalize())

                                        #ajusta img do user de acordo com o humor
                                        ajuste_img = buscador_img.ajusta_img(matricula=str(user_0[0]),
                                        ark=(f'{user_0[5]}.png'),local=str(user_0[0]))
                                        #Atualiza img e humor 
                                        window['-img_user0-'].update(ajuste_img)
                                        window['-humor_user0-'].update(user_0[5])

                                        #atualiza status geral
                                        window['-status_user0-'].update(user_0[2])
                                        window['-un_user0-'].update(user_0[3])
                                        window['-local_user0-'].update(user_0[4])

                                        #deixa status geral visível caso user 0 tenha saído ou retornado de saída
                                        window['-status_g_user0-'].update(visible=True)
                                        window.refresh()
                                        
                        else:   
                                #atualiza nome user 0
                                window['-nome_user0-'].update(nome_0[0].capitalize())

                                #ajusta img padrão para atualizar no totem
                                ajusta_img = buscador_img.ajusta_img_padrão(img_p=r'img_base\descanso.png',
                                local=f'{user_0[0]}')

                                #atualiza status geral
                                window['-img_user0-'].update(ajusta_img)
                                window['-humor_user0-'].update('Descansando')

                                #oculta status geral caso user não esteja 
                                window['-status_g_user0-'].update(visible=False)

                # verifica se user 1 está de ferias.
                if user_1[2] == 'Ferias':
                        #atualiza nome user 1
                        window['-nome_user1-'].update(nome_1[0].capitalize())
                        #esconde layout de status geral 
                        window['-status_g_user1-'].update(visible=False)

                        #ajusta img padrão para atualizar o totem
                        ajusta_img = buscador_img.ajusta_img_padrão(img_p=r'img_base\Ferias.png',local=f'{user_1[0]}')
                        window['-img_user1-'].update(ajusta_img)
                        #atualiza humor com status
                        window['-humor_user1-'].update('Férias')

                else:
                        #verifica se user 1 está já começou a trabalhar
                        if user_1[1] == 'Entrada':

                                #verifica se user 1 está no horário de intervalo
                                if user_1[2] == 'Intervalo':
                                        #atualiza nome user 1
                                        window['-nome_user1-'].update(nome_1[0].capitalize())
                                        
                                        #ajusta img padrão para atualizar no totem
                                        ajusta_img = buscador_img.ajusta_img_padrão(img_p=r'img_base\intervalo.png',
                                        local=f'{user_1[0]}')

                                        #atualiza img
                                        window['-img_user1-'].update(ajusta_img)
                                        #apaga humor
                                        window['-humor_user1-'].update('')

                                        #atualiza status geral
                                        window['-status_user1-'].update(user_1[2])
                                        window['-un_user1-'].update(user_1[3])
                                        window['-local_user1-'].update(user_1[4])
                                        window.refresh()

                                else:   
                                        #atualiza nome user 1
                                        window['-nome_user1-'].update(nome_1[0].capitalize())

                                        #ajusta img do user de acordo com o humor
                                        ajuste_img = buscador_img.ajusta_img(matricula=str(user_1[0]),
                                        ark=(f'{user_1[5]}.png'),local=str(user_1[0]))
                                        #Atualiza img e humor 
                                        window['-img_user1-'].update(ajuste_img)
                                        window['-humor_user1-'].update(user_1[5])

                                        #atualiza status geral
                                        window['-status_user1-'].update(user_1[2])
                                        window['-un_user1-'].update(user_1[3])
                                        window['-local_user1-'].update(user_1[4])

                                        #deixa status geral visível caso user 0 tenha saído ou retornado de saída
                                        window['-status_g_user1-'].update(visible=True)
                                        window.refresh()
                        
                        else:
                                #atualiza nome user 1
                                window['-nome_user1-'].update(nome_1[0].capitalize())
                                #ajusta img padrão para atualizar o totem
                                ajusta_img = buscador_img.ajusta_img_padrão(img_p=r'img_base\descanso.png',
                                local=f'{user_1[0]}')
                                
                                #atualiza status geral
                                window['-img_user1-'].update(ajusta_img)
                                window['-humor_user1-'].update('Descansando')

                                #oculta status geral caso user não esteja
                                window['-status_g_user1-'].update(visible=False)
