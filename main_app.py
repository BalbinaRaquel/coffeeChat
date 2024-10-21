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
    # 1.3 Ao clicar no botão -> remover título - remover botão 'Iniciar chat'
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
    titulo = ft.Text('Coffee & Chat')
    pagina.add(titulo)

    # Criar botão iniciar
    botao_iniciar = ft.ElevatedButton('Iniciar Chat')
    pagina.add(botao_iniciar)



# Executar a função main com o flet
ft.app(main, view=ft.W)


