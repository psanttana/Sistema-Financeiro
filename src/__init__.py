from flask import Flask
from .extensions import db
from .config import config

def create_app(config_name='development'):
    """Factory function para criar a aplicação Flask."""
    app = Flask(__name__, template_folder='templates', static_folder='static')
    
    # Carregar configurações
    app.config.from_object(config[config_name])
    
    # Inicializar extensões
    db.init_app(app)
    
    # Registrar blueprints
    from .routes import auth_bp, dashboard_bp, categories_bp, transactions_bp
    app.register_blueprint(auth_bp)
    app.register_blueprint(dashboard_bp)
    app.register_blueprint(categories_bp)
    app.register_blueprint(transactions_bp)
    
    # Criar tabelas
    with app.app_context():
        db.create_all()
    
    return app
