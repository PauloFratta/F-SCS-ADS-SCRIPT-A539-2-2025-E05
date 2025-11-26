from flask import Flask
from model_db import db, Ong, Usuario, Animal, PedidoAdocao
import os

# Configuração mínima do App apenas para criar o banco
app = Flask(__name__)

# Define o caminho do arquivo SQLite
basedir = os.path.abspath(os.path.dirname(__file__))
path_banco = os.path.join(basedir, 'patacerta.db')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + path_banco
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Conecta o objeto db ao app configurado
db.init_app(app)

if __name__ == '__main__':
    # O comando with app.app_context() é obrigatório
    with app.app_context():
        print(f"Criando banco de dados em: {path_banco}")
        
        # O COMANDO MÁGICO: Cria todas as tabelas definidas nos models importados
        db.create_all()
        
        print("Sucesso! O arquivo 'patacerta.db' foi criado com as tabelas.")