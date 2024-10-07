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

def open_main_app():
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

    # ----------- Frame Lateral --------------
    side_menu_frame = Frame(main_app, bg="#333333", width=64, height=800)  # Frame lateral
    side_menu_frame.pack(side="left", fill="y")

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

    # ---- FRAME APLICAÇÃO PARTE INFERIOR ---- #
    Frame_App = Frame(main_app, bg="#fff", width=1200, height=800)
    Frame_App.pack_propagate(False)  # Impede que o frame redimensione automaticamente
    Frame_App.pack(fill="both", expand=True)  # Ajusta o frame ao tamanho da janela

    # # Exemplo de frase de boas-vindas e dados adicionais
    welcome_label = Label(Frame_App, text="Bem-vindo ao Sistema WMS", font=("Arial", 16), bg="#fff")
    welcome_label.place(x=10, y=10)
   
    # -------------------------------------

    main_app.mainloop()