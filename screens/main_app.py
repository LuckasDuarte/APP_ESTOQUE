import tkinter as tk
from tkinter import messagebox
from tkinter import *
from PIL import Image, ImageTk
import sqlite3
import time

# Função para atualizar a hora
def update_time(time_label):
    current_time = time.strftime('%d/%m/%Y %H:%M:%S')  # Formato de data e hora
    time_label.config(text=current_time)
    time_label.after(1000, update_time, time_label)  # Atualiza a cada 1000ms (1 segundo)

def open_main_app(): #INSERIR COMO ARGUMENTO DA FUNÇÃO: username, para exibir o nome de maneira dinâmica
    main_app = tk.Tk()
    main_app.title("SISTEMA WMS")
    icon = tk.PhotoImage(file='assets/parcela.png')
    main_app.iconphoto(True, icon)
    main_app.state("zoomed")
    main_app.resizable(False, False)

    # ----------- Header --------------
    header_frame = Frame(main_app, bg="#444444", height=70)
    header_frame.pack_propagate(False)
    header_frame.pack(fill="x", side="top")

    # Logo à esquerda
    logo_path = "assets/logo_home.png"
    original_logo = Image.open(logo_path)
    resized_logo = original_logo.resize((200, 150), Image.LANCZOS)  # Usando LANCZOS
    logo_wms = ImageTk.PhotoImage(resized_logo)

    logo_label = Label(header_frame, image=logo_wms, bg="#444444", width=50)
    logo_label.pack(side="left", padx=10)
    
    # Armazenar a imagem para evitar coleta de lixo
    main_app.logo_wms = logo_wms

    # Título (Saudação) e nome do usuário ao lado do logo
    username = "LUCAS.D"
    title_label = Label(header_frame, text=f"BEM-VINDO: {username}", font=("Arial", 12), fg="white", bg="#444444", anchor="w")
    title_label.pack(pady=27, side="left")  # Ajusta a posição para estar ao lado do logo

    # Data e Hora (Centralizado)
    time_label = Label(header_frame, font=("Arial", 12), fg="white", bg="#444444", anchor="w")
    time_label.place(relx=0.5, anchor="center", y=40, x=540)  # Centraliza o tempo horizontalmente
    update_time(time_label)

    # Função para confirmar a saída
    def confirmar_saida():
        resposta = messagebox.askyesno("Confirmação", "Tem certeza que deseja sair?")
        if resposta:
            main_app.destroy()

    # Botão de sair (extrema direita)
    btn_sair = Button(header_frame, text="Sair", command=confirmar_saida, bg="#ff4d4d", fg="white", relief="flat", cursor="hand2")
    btn_sair.place(x=1310, y=27)

    # ----------- Frame Lateral --------------
    side_menu_frame = Frame(main_app, bg="#333333", width=80, height=800)  # Frame lateral
    side_menu_frame.pack(side="left", fill="y")

    # ---- Botão Estoque  ----
    caixa_image_path = "assets/caixa.png"
    original_caixa_image = Image.open(caixa_image_path)
    resized_caixa_image = original_caixa_image.resize((50, 50), Image.LANCZOS)
    caixa_photo = ImageTk.PhotoImage(resized_caixa_image)

    btn_estoque = Button(side_menu_frame, image=caixa_photo, bg="#333333", relief="flat", cursor="hand2")
    btn_estoque.image = caixa_photo  # Armazenar a imagem para evitar coleta de lixo
    btn_estoque.pack(pady=10, padx=10)

    # ---- Botão Movimentações  ----
    carrinho_image_path = "assets/carrinho.png"
    original_carrinho_image = Image.open(carrinho_image_path)
    resized_carrinho_image = original_carrinho_image.resize((50, 50), Image.LANCZOS)
    carrinho_photo = ImageTk.PhotoImage(resized_carrinho_image)

    btn_movimentar = Button(side_menu_frame, image=carrinho_photo, bg="#333333", relief="flat", cursor="hand2")
    btn_movimentar.image = carrinho_photo
    btn_movimentar.pack(pady=10)

    # ---- Botão Cadastros  ----
    produto_image_path = "assets/produto.png"
    original_produto_image = Image.open(produto_image_path)
    resized_produto_image = original_produto_image.resize((50, 50), Image.LANCZOS)
    produto_photo = ImageTk.PhotoImage(resized_produto_image)

    btn_produtos = Button(side_menu_frame, image=produto_photo, bg="#333333", relief="flat", cursor="hand2")
    btn_produtos.image = produto_photo
    btn_produtos.pack(pady=10)

    # ---- Botão Relatório  ----
    relatorio_image_path = "assets/relatorio.png"
    original_relatorio_image = Image.open(relatorio_image_path)
    resized_relatorio_image = original_relatorio_image.resize((50, 50), Image.LANCZOS)
    relatorio_photo = ImageTk.PhotoImage(resized_relatorio_image)

    btn_relatorios = Button(side_menu_frame, image=relatorio_photo, bg="#333333", relief="flat", cursor="hand2")
    btn_relatorios.image = relatorio_photo
    btn_relatorios.pack(pady=10)

    # ---- Botão Dashboard  ----
    dashboard_image_path = "assets/grafico.png"
    original_dashboard_image = Image.open(dashboard_image_path)
    resized_dashboard_image = original_dashboard_image.resize((50, 50), Image.LANCZOS)
    dashboard_photo = ImageTk.PhotoImage(resized_dashboard_image)

    btn_dashboard = Button(side_menu_frame, image=dashboard_photo, bg="#333333", relief="flat", cursor="hand2")
    btn_dashboard.image = dashboard_photo
    btn_dashboard.pack(pady=10)

    # ---- Frame para os Botões Usuário e Servidor ----
    bottom_buttons_frame = Frame(side_menu_frame, bg="#333333")
    bottom_buttons_frame.pack(side="bottom", pady=20)  # Posicionar mais para baixo

    # ---- Botão Usuário  ----
    usuario_image_path = "assets/usuario.png"
    original_usuario_image = Image.open(usuario_image_path)
    resized_usuario_image = original_usuario_image.resize((50, 50), Image.LANCZOS)
    usuario_photo = ImageTk.PhotoImage(resized_usuario_image)

    btn_usuario = Button(bottom_buttons_frame, image=usuario_photo, bg="#333333", relief="flat", cursor="hand2")
    btn_usuario.image = usuario_photo  # Armazenar a imagem para evitar coleta de lixo
    btn_usuario.pack(pady=10)

    # ---- Botão Servidor  ----
    servidor_image_path = "assets/servidor.png"
    original_servidor_image = Image.open(servidor_image_path)
    resized_servidor_image = original_servidor_image.resize((50, 50), Image.LANCZOS)
    servidor_photo = ImageTk.PhotoImage(resized_servidor_image)

    btn_servidor = Button(bottom_buttons_frame, image=servidor_photo, bg="#333333", relief="flat", cursor="hand2")
    btn_servidor.image = servidor_photo  # Armazenar a imagem para evitar coleta de lixo
    btn_servidor.pack(pady=10)


    # ---- FRAME APLICAÇÃO PARTE INFERIOR ---- #
    Frame_App = Frame(main_app, bg="#fff", width=1200, height=800)
    Frame_App.pack_propagate(False)  # Impede que o frame redimensione automaticamente
    Frame_App.pack(fill="both", expand=True)  # Ajusta o frame ao tamanho da janela

    # # Exemplo de frase de boas-vindas e dados adicionais
    welcome_label = Label(Frame_App, text="Bem-vindo ao Sistema WMS", font=("Arial", 16), bg="#fff")
    welcome_label.place(x=10, y=10)
   
    # -------------------------------------

    main_app.mainloop()

open_main_app()