import tkinter as tk
from tkinter import messagebox
from tkinter import *
from PIL import Image, ImageTk
import sqlite3
import time

from screens.main_app import open_main_app

# --- ESTOQUE APP ---
# VERSÃO - ALPHA 0.0.1

banco = "database/database.db"
icone = "assets/parcela.png"

# Função para verificar login
def check_login(username, password):

    try:
        # Conectando ao banco de dados SQLite
        conn = sqlite3.connect(banco)
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
    except:
        messagebox.showerror("Erro","Erro durante o login, verifique os dados!")

# Função chamada ao clicar no botão de login
def login():
    global username
    username = entry_user.get()
    password = entry_pass.get()

    # Verifica se o usuário e senha estão corretos
    if check_login(username, password):
        Login.destroy()  # Fecha a janela de login
        open_main_app(username)  # Abre a tela principal
    else:
        messagebox.showerror("Erro", "Usuário ou senha incorretos!")

# Função para mostrar ou ocultar a senha
def toggle_password():
    if chk_state.get():
        entry_pass.config(show="")  # Mostra a senha
    else:
        entry_pass.config(show="*")  # Oculta a senha



# LOGUIN PAGE
def LoginPage():
    global Login, entry_user, entry_pass, chk_state, user_logado
    Login = tk.Tk()
    Login.title("WMS")
    icon = tk.PhotoImage(file=icone)
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