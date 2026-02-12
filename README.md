# 🗂️ Task Manager API

API RESTful para gerenciamento de tarefas desenvolvida com FastAPI e SQLAlchemy, aplicando princípios de arquitetura em camadas e boas práticas de desenvolvimento backend.

> 🚧 Projeto em desenvolvimento contínuo.

---

## 🚀 Tecnologias utilizadas

- Python 3.12+
- FastAPI
- SQLAlchemy 2.0
- SQLite
- Uvicorn

---

## 🏗️ Estrutura do projeto

O projeto foi estruturado com separação de responsabilidades:

task-manager-api/
│
├── app/
│ ├── main.py # Inicialização da aplicação
│ ├── database.py # Configuração da conexão com o banco
│ ├── models.py # Modelos ORM (SQLAlchemy)
│ ├── schemas.py # Schemas de validação (Pydantic)
│ ├── crud.py # Operações de acesso ao banco
│ └── routers/
│ └── tasks.py # Definição de rotas da API
│
├── .gitignore
└── README.md


---

## 📌 Status atual

- [x] Configuração inicial do FastAPI
- [x] Configuração do banco de dados (SQLite)
- [x] Modelagem da entidade `Task` com SQLAlchemy
- [ ] Implementação completa do CRUD
- [ ] Validações avançadas
- [ ] Testes automatizados

---

## ▶️ Como executar o projeto

### 1️⃣ Clone o repositório

git clone https://github.com/seu-usuario/task-manager-api.git
cd task-manager-api

### 2️⃣ Crie e ative o ambiente virtual

Windows:

python -m venv venv
venv\Scripts\activate

Linux / Mac:

python3 -m venv venv
source venv/bin/activate

### 3️⃣ Instale as dependências

pip install -r requirements.txt

### 4️⃣ Execute a aplicação

uvicorn app.main:app --reload

Acesse no navegador:

http://127.0.0.1:8000/docs

---

## 🎯 Objetivo do projeto

Este projeto foi criado com o objetivo de:

Consolidar conhecimentos em construção de APIs REST

Praticar modelagem de banco de dados com ORM

Aplicar organização em camadas no backend

Evoluir gradualmente para padrões mais robustos (migrations, autenticação e testes)

👨‍💻 Autor
William Moreira
Desenvolvedor Back-end em formação
