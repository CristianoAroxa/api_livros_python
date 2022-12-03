""" Um API possui 4 etapas
    API é um lugar para disponibilizar recursos e/ou funcionalidades
    1. Objetivo - Criar um api que disponibiliza a consulta, criação, edição e exclusão de livros
    2. Url base - localhost
    3. Endpoints - 
        - localhost/livros(GET)
        - localhost/livros/id(GET)
        - localhost/livros/id(PUT)
        - localhost/livros/id(DELETE)
    4. Quais recursos livros
"""

from flask import Flask, jsonify, request

app = Flask(__name__)

livros = [
    {
        'id': 1,
        'título': 'O livro dos cinco anéis',
        'autor': 'Myamoto Musashi'
    },
    {
        'id': 2,
        'título': 'O caminho do Samurai',
        'autor': 'Inazo Nitobe'
    },
    {
        'id': 3,
        'título': '1984',
        'autor': 'George Orwell'
    },
]

# Consultar(todos)
@app.route('/livros', methods=['GET'])
def obter_livros():
    return jsonify(livros)

#consultar por id
@app.route('/livros/<int:id>',methods=['GET'])
def obter_livro_por_id(id):
    for livro in livros:
        if livro.get('id') == id:
            return jsonify(livro)

#editar
@app.route('/livros/<int:id>',methods=['PUT'])
def editar_livro_por_id(id):
    livro_alterado = request.get_json()
    for indice,livro in enumerate(livros):
        if livro.get('id') == id:
            livros[indice].update(livro_alterado)
            return jsonify(livros[indice])

#Criar
@app.route('/livros',methods=['POST'])
def incluir_novo_livro():
    novo_livro = request.get_json()
    livros.append(novo_livro)

    return jsonify(livros)


#excluir

@app.route('/livros/<int:id>',methods=['DELETE'])
def excluir_livro_por_id(id):
    for indice, livro in enumerate(livros):
        if livro.get('id') == id:
            del livros[indice]

    return jsonify(livros)


app.run(port=5000, host='localhost', debug=True)
