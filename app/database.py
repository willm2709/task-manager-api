from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase

# String de conexão com banco SQLite
DATABASE_URL = "sqlite:///./tasks.db"

# Cria engine (conexão com o banco)
engine = create_engine(
    DATABASE_URL,
    connect_args={"check_same_thread": False}  # necessário para SQLite
)

# Cria fábrica de sessões
SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

# Classe base para nossos modelos
class Base(DeclarativeBase):
    pass

# Dependência para abrir e fechar sessão automaticamente
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
