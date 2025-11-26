from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

# Inicializamos o objeto db aqui para ser usado pelas classes
db = SQLAlchemy()

# --- Definição das Tabelas (Classes) ---

class Ong(db.Model):
    __tablename__ = 'ongs'
    id = db.Column(db.Integer, primary_key=True)
    nome_fantasia = db.Column(db.String(100), nullable=False)
    cnpj = db.Column(db.String(14), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    senha_hash = db.Column(db.String(128))
    
    # Relacionamento com Animal
    animais = db.relationship('Animal', backref='ong_proprietaria', lazy=True)

class Usuario(db.Model):
    __tablename__ = 'usuarios'
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    senha_hash = db.Column(db.String(128))

class Animal(db.Model):
    __tablename__ = 'animais'
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(50), nullable=False)
    especie = db.Column(db.String(20), nullable=False)
    ong_id = db.Column(db.Integer, db.ForeignKey('ongs.id'), nullable=False)

class PedidoAdocao(db.Model):
    __tablename__ = 'pedidos_adocao'
    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.DateTime, default=datetime.utcnow)
    usuario_id = db.Column(db.Integer, db.ForeignKey('usuarios.id'), nullable=False)
    animal_id = db.Column(db.Integer, db.ForeignKey('animais.id'), nullable=False)