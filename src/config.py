import os
try:
    from dotenv import load_dotenv
    load_dotenv()
except:
    pass

class Config:
    """Configurações base da aplicação."""
    import os
    db_url = os.getenv('DATABASE_URL', '')
    if not db_url or 'mysql' in db_url:
        SQLALCHEMY_DATABASE_URI = 'sqlite:///sistema_financeiro.db'
    else:
        SQLALCHEMY_DATABASE_URI = db_url
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = os.getenv('SECRET_KEY', 'dev-key-change-in-production')

class DevelopmentConfig(Config):
    """Configurações para desenvolvimento."""
    DEBUG = True
    TESTING = False

class ProductionConfig(Config):
    """Configurações para produção."""
    DEBUG = False
    TESTING = False

class TestingConfig(Config):
    """Configurações para testes."""
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:'

config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    'testing': TestingConfig,
    'default': DevelopmentConfig
}
