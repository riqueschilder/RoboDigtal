# importando as bibliotecas necessárias
from flask import Flask, jsonify, request, send_file
import sqlite3

# criando a aplicação Flask
app = Flask(__name__)

# definindo a rota principal que retorna o arquivo 'index.html'
@app.route('/')
def index():
    return send_file('front\index.html')

# definindo a rota para consultar a posição atual do robô
@app.route('/robot_position', methods=['GET'])
def get_robot_position():
    # conectando-se ao banco de dados SQLite
    conn = sqlite3.connect('position.db')
    cursor = conn.cursor()
    # selecionando a posição atual do robô a partir do banco de dados
    cursor.execute('SELECT * FROM position')
    position = cursor.fetchone()
    # fechando a conexão com o banco de dados
    conn.close()
    # retornando a posição atual do robô em formato JSON
    return jsonify({'x': position[0], 'y': position[1], 'z': position[2]})

# definindo as rotas para mover o robô para frente, trás, direita, esquerda, para cima e para baixo
@app.route('/move_forward', methods=['POST'])
def move_forward():
    # conectando-se ao banco de dados SQLite
    conn = sqlite3.connect('position.db')
    cursor = conn.cursor()
    # atualizando a posição x do robô para frente
    cursor.execute("UPDATE position SET x = x + 1 WHERE id = 1")
    # salvando as alterações no banco de dados
    conn.commit()
    # fechando a conexão com o banco de dados
    conn.close()
    # retornando um JSON indicando que a operação foi bem sucedida
    return jsonify({'success': True})

@app.route('/move_backward', methods=['POST'])
def move_backward():
    # conectando-se ao banco de dados SQLite
    conn = sqlite3.connect('position.db')
    cursor = conn.cursor()
    # atualizando a posição x do robô para trás
    cursor.execute("UPDATE position SET x = x - 1 WHERE id = 1")
    # salvando as alterações no banco de dados
    conn.commit()
    # fechando a conexão com o banco de dados
    conn.close()
    # retornando um JSON indicando que a operação foi bem sucedida
    return jsonify({'success': True})

@app.route('/move_right', methods=['POST'])
def move_right():
    # conectando-se ao banco de dados SQLite
    conn = sqlite3.connect('position.db')
    cursor = conn.cursor()
    # atualizando a posição y do robô para a direita
    cursor.execute("UPDATE position SET y = y + 1 WHERE id = 1")
    # salvando as alterações no banco de dados
    conn.commit()
    # fechando a conexão com o banco de dados
    conn.close()
    # retornando um JSON indicando que a operação foi bem sucedida
    return jsonify({'success': True})

# Define rota /move_left para mover o robô para a esquerda
@app.route('/move_left', methods=['POST'])
def move_left():
    # Estabelece conexão com o banco de dados SQLite
    conn = sqlite3.connect('position.db')
    cursor = conn.cursor()
    
    # Executa uma query SQL para atualizar a posição do robô
    cursor.execute("UPDATE position SET y = y - 1 WHERE id = 1")
    
    # Salva as alterações no banco de dados
    conn.commit()
    
    # Fecha a conexão com o banco de dados
    conn.close()
    
    # Retorna uma resposta JSON indicando que a operação foi concluída com sucesso
    return jsonify({'success': True})


# Define rota /move_up para mover o robô para cima
@app.route('/move_up', methods=['POST'])
def move_up():
    # Estabelece conexão com o banco de dados SQLite
    conn = sqlite3.connect('position.db')
    cursor = conn.cursor()
    
    # Executa uma query SQL para atualizar a posição do robô
    cursor.execute("UPDATE position SET z = z + 1 WHERE id = 1")
    
    # Salva as alterações no banco de dados
    conn.commit()
    
    # Fecha a conexão com o banco de dados
    conn.close()
    
    # Retorna uma resposta JSON indicando que a operação foi concluída com sucesso
    return jsonify({'success': True})


# Define rota /move_down para mover o robô para baixo
@app.route('/move_down', methods=['POST'])
def move_down():
    # Estabelece conexão com o banco de dados SQLite
    conn = sqlite3.connect('position.db')
    cursor = conn.cursor()
    
    # Executa uma query SQL para atualizar a posição do robô
    cursor.execute("UPDATE position SET z = z - 1 WHERE id = 1")
    
    # Salva as alterações no banco de dados
    conn.commit()
    
    # Fecha a conexão com o banco de dados
    conn.close()
    
    # Retorna uma resposta JSON indicando que a operação foi concluída com sucesso
    return jsonify({'success': True})


# Inicia o aplicativo Flask
if __name__ == '__main__':
    app.run(debug=True)