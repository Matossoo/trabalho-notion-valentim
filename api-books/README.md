# api-books

API de livros com Flask + SQLAlchemy + PostgreSQL + Flask-Migrate.

## Passo a passo
1. Crie o banco `books` no PostgreSQL (porta 5432, usuário `postgres`).
2. `python -m venv venv` e ative (`venv\Scripts\activate` no Windows, `source venv/bin/activate` no Linux/Mac).
3. `pip install -r requirements.txt`
4. (Opcional) copie `.env.example` para `.env` e ajuste a senha.
5. Migrações:
   ```
   flask --app app db init
   flask --app app db migrate -m "criacao da tabela book"
   flask --app app db upgrade
   ```
6. `python app.py` -> http://localhost:8080/hello

## Endpoints
POST /books | GET /books | GET /books/<id> | PATCH /books/<id> | DELETE /books/<id>
