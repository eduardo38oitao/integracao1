# Import do framework Flask
# Render_template para ler/renderizar o html
# Request para pegar os dados do formulário

from flask import Flask, render_template, request
# biblioteca para conectar ao banco de dados MySQL
import mysql.connector

app = Flask(__name__)

# Cria conexão com o banco de dados
bd_config = {
    'host': '127.0.0.1',
    'user': 'root',
    'password': 'escola',
    'database': 'cadastro1'
}

# Criação de rota para o arquivo HTML principal

@app.route('/')

def indexRota():
    return render_template('index.html')

@app.route('/cadastrar', methods=('POST'))

def criarCadastro():

    try: 
        # recebe os dados do formulário
        cpf = request.form['cpf']
        primeiro_nome = request.form['primeiro_nome']
        sobrenome = request.form['sobrenome']
        idade = request.form['idade']

        # Conecta ao banco de dados
        # #Biblioteca mysql.connector conecta o python com o mysql
        conexao = mysql.connector.connect(**bd_config)

        #levar instrução SQL do python para o banco de dados
        curso = conexao.cursor()
        
        query = "INSERT INTO cliente1 (cpf, primeiro_nome, sobrenome, idade) VALUES (%s, %s, %s, %s)"
        curso.execute(query,(cpf,primeiro_nome,sobrenome,idade))

        #salvar as alterações
        curso.commit()
        #fechar cursor
        curso.close()
        #fechar a conexão com o banco de dados
        conexao.close()

        # Decorador tem @
    except mysql.connector.Error as err:
        return f"Erro ao gravar no banco: {err}"