import tkinter as tk
from tkinter import messagebox
import threading
from flask import Flask, jsonify, request
import sqlite3

# Inicializando o aplicativo Flask
app = Flask(__name__)

# Função para criar a interface desktop
def criar_interface():
    root = tk.Tk()
    root.title("Sistema de Controle de Estoque")

    def iniciar_servidor():
        # Inicia o servidor Flask em uma thread separada
        server_thread = threading.Thread(target=rodar_servidor)
        server_thread.daemon = True
        server_thread.start()
        messagebox.showinfo("Servidor", "Servidor iniciado no endereço http://localhost:5000")

    # Botão para iniciar o servidor
    iniciar_btn = tk.Button(root, text="Iniciar Servidor", command=iniciar_servidor)
    iniciar_btn.pack(pady=20)

    root.mainloop()

# Função para rodar o servidor Flask
def rodar_servidor():
    app.run(host="0.0.0.0", port=5000)

# Funções Flask para interagir com o banco de dados
@app.route("/produtos", methods=["GET"])
def listar_produtos():
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM ESTOQUE")
    produtos = cursor.fetchall()
    conn.close()
    return jsonify(produtos)

@app.route("/movimentar", methods=["POST"])
def movimentar_produto():
    dados = request.json
    produto_id = dados["id"]
    quantidade = dados["quantidade"]
    
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()
    cursor.execute("UPDATE ESTOQUE SET quantidade = quantidade + ? WHERE id = ?", (quantidade, produto_id))
    conn.commit()
    conn.close()
    return jsonify({"status": "movimentação realizada"}), 200

@app.route("/")
def index():
    return '''
    <h1>Sistema de Controle de Estoque - Coletor</h1>
    <form action="/movimentar" method="POST">
        <label>ID do Produto:</label><br>
        <input type="text" name="id"><br>
        <label>Quantidade:</label><br>
        <input type="text" name="quantidade"><br>
        <input type="submit" value="Enviar">
    </form>
    '''


# Cria a interface do sistema desktop
if __name__ == "__main__":
    criar_interface()
