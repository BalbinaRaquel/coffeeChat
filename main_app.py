# Projeto de Chat 

# Estrutura do Projeto

# Tela Inicial
# Step 01: Criar tela inicial com o seguintes recursos:
    # 1.1 : Título 'Coffee & Chat';
    # 1.2 Botão iniciar Chat - quando clicar no botão --> abrir popup/modal/alerta

        # Tela de Alerta/PopUp
        # 1.2.1 Título do popup/alerta: 'Bem-vindo!'
        # 1.2.2 Caixa de texto: 'Escreva seu nome no chat'
        # 1.2.3 Botão: 'Entrar no chat'
    # 1.3 Ao clicar no botão -> remover título - remover botão 'Iniciar chat' e fechar popup
        # 1.3.1 Carregar chat;
        # 1.3.2 Carregar campo de enviar mensagem: 'Digite sua mensagem'
        # 1.3.3 Carregar o botão 'enviar' mensagem

# Tela de Chat
# step 02: Ao clicar no botão 'enviar' da mensagem, a mensagem é enviada
    # 2.1 enviar mensagem
    # 2.2 limpar a caixa de mensagem
    # 2.3 Mensagem enviada --> Tela de conversa

# Tela de Chat
# Step 03: 


# main code: Ctrl+F5 Chat
# Criar função principal para rodar o main (aplicativo)

import flet as ft

def main(pagina):
    # steps do projeto

    
    
    imagem_pg = ft.Image(src=f'icon1.png', width=250, height=250, fit=ft.ImageFit.CONTAIN,)
    pagina.add(imagem_pg)
    # Criar Título  
    titulo = ft.Text('Bem-vindos ao Coffee & Chat!')
    pagina.add(titulo)

    def enviar_mensagem(evento):
        nome_usuario = caixa_nome.value
        texto_campo_mensagem = campo_enviar_mensagem.value
        
        texto = ft.Text(f'{nome_usuario}: {campo_enviar_mensagem.value}')
        chat.controls.append(texto)

        # Limpar caixa de enviar mensagem
        campo_enviar_mensagem.value = ''
        pagina.update()


    campo_enviar_mensagem = ft.TextField(label='Digite a sua mensagem...', on_submit=enviar_mensagem)
    botao_enviar = ft.ElevatedButton('Enviar', on_click=enviar_mensagem)
    
    

    linha_mensagem = ft.Row([campo_enviar_mensagem, botao_enviar])

    chat = ft.Column()


    # criar função entrar no chat com o click do botão do popup
    # Ao clicar no botão -> remover título - remover botão 'Iniciar chat' e fechar popup
    def entrar_chat(evento):

        # fechar popup
        popup.open = False
        # remover título
        pagina.remove(titulo)
        # Remover botão iniciar chat
        pagina.remove(botao_iniciar)
        
        # Carregar o chat
        pagina.add(chat)
        
        # carregar o campo de enviar mensagem e carregar botão enviar
        pagina.add(linha_mensagem)
        pagina.update()
        


    # criar popup que abre ao criar no botão iniciar
    titulo_popup = ft.Text('Vamos iniciar o Coffeebreak?')
    caixa_nome = ft.TextField(label='Digite o seu nome', on_submit=entrar_chat)
    botao_popup = ft.ElevatedButton('Entrar no Chat', on_click=entrar_chat)
    
    popup = ft.AlertDialog(title=titulo_popup, content=caixa_nome, actions=[botao_popup])



    # Criar botão iniciar
    def abrir_popup(evento):
        # ação que executa ao clicar no botão
        pagina.dialog = popup
        popup.open= True
        pagina.update()
    
    botao_iniciar = ft.ElevatedButton('Iniciar Chat', on_click=abrir_popup)
    pagina.add(botao_iniciar)



# Executar a função main com o flet
ft.app(target=main, view=ft.AppView.WEB_BROWSER, port=8000)


