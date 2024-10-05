import tkinter as tk
from tkinter import messagebox
from tkinter import *
from PIL import Image, ImageTk
import sqlite3
import time

# --- ESTOQUE APP ---
# VERSÃO - ALPHA 0.0.1




# Função para atualizar a hora
def update_time(time_label):
    current_time = time.strftime('%d/%m/%Y %H:%M:%S')  # Formato de data e hora
    time_label.config(text=current_time)
    time_label.after(1000, update_time, time_label)  # Atualiza a cada 1000ms (1 segundo)

# Função para verificar login
def check_login(username, password):
    # Conectando ao banco de dados SQLite
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()

    # Consulta para verificar se o usuário e a senha são válidos
    cursor.execute('''
        SELECT * FROM USERS WHERE user=? AND senha=?
    ''', (username, password))

    # Verificar se existe um resultado
    user = cursor.fetchone()
    
    conn.close()

    if user:
        return True
    else:
        return False

# Função chamada ao clicar no botão de login
def login():
    global username
    username = entry_user.get()
    password = entry_pass.get()

    # Verifica se o usuário e senha estão corretos
    if check_login(username, password):
        Login.destroy()  # Fecha a janela de login
        open_main_app()  # Abre a tela principal
    else:
        messagebox.showerror("Erro", "Usuário ou senha incorretos!")

# Função para mostrar ou ocultar a senha
def toggle_password():
    if chk_state.get():
        entry_pass.config(show="")  # Mostra a senha
    else:
        entry_pass.config(show="*")  # Oculta a senha



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

    # Botão de sair (extrema direita)
    btn_sair = Button(header_frame, text="Sair", command=main_app.destroy, bg="#ff4d4d", fg="white", relief="flat", cursor="hand2")
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


# LOGUIN PAGE
def LoginPage():
    global Login, entry_user, entry_pass, chk_state
    Login = tk.Tk()
    Login.title("WMS")
    icon = tk.PhotoImage(file='assets/parcela.png')
    Login.iconphoto(True, icon)
    Login.resizable(False, False)
    Login.state("zoomed")

    # ----------- Imagem Lateral --------------
    image = PhotoImage(file='assets/fundo_login.png')  # Substitua pelo nome da sua imagem
    image_label = tk.Label(Login, image=image)
    image_label.image = image
    image_label.grid(column=0, row=0)

    Frame_login = Frame(Login, width=320, height=150)
    Frame_login.grid(column=1, row=0, padx=45, sticky="N", pady=130)

    # Logo Tag
    logo_path = "assets/logo.png"
    original_logo = Image.open(logo_path)
    resized_logo = original_logo.resize((250, 200), Image.ANTIALIAS)  # Redimensionar conforme necessário
    logo_task = ImageTk.PhotoImage(resized_logo)

    label_logo = Label(Frame_login, image=logo_task, text="")
    label_logo.grid(column=1, row=0)

    Frame_login_Itens = Frame(Login, width=250, height=200)
    Frame_login_Itens.grid(column=1, row=0, sticky="S", pady=220)

    lb_geral = Label(Frame_login_Itens, text="―――― BEM-VINDO ――――", font=("", 12))
    lb_geral.place(x=20, y=0)

    lb_login = Label(Frame_login_Itens, text="USUÁRIO")
    lb_login.place(x=20, y=40)

    # Criando a Entry com placeholder
    entry_user = tk.Entry(Frame_login_Itens, width=36, relief="groove")
    user_logado = entry_user.get()
    entry_user.place(x=20, y=60)

    lb_login_2 = Label(Frame_login_Itens, text="SENHA")
    lb_login_2.place(x=20, y=80)

    # Criando a Entry para senha
    entry_pass = tk.Entry(Frame_login_Itens, width=36, show="*", relief="groove")
    entry_pass.place(x=20, y=100)

    # Checkbutton para mostrar/ocultar senha
    chk_state = tk.BooleanVar(value=False)  # Estado inicial: desmarcado (senha oculta)
    chk_show_pass = tk.Checkbutton(Frame_login_Itens, text="Mostrar Senha", variable=chk_state, command=toggle_password)
    chk_show_pass.place(x=15, y=115)

    # Botão de login
    btn_login = Button(Frame_login_Itens, text="LOGIN", width=30, bg="#00bf63", fg="#000", relief="groove", cursor="hand2", command=login)
    btn_login.place(x=20, y=150)

    lb_credit = Label(Frame_login_Itens, text="Desenvolvido Por: Lucas Duarte")
    lb_credit.place(x=40, y=180)

    Login.mainloop()

# RODA A INTERFACE
if __name__ == "__main__":
    # LoginPage()
    open_main_app()
