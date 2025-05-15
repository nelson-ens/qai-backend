# QAI Backend

This is the backend API for the QAI Dashboard application, built with FastAPI and PostgreSQL.

## Prerequisites

- Python 3.8+
- Docker and Docker Compose
- PostgreSQL (via Docker)

## Setup Instructions

1. Clone the repository:
```bash
git clone <repository-url>
cd qai-backend-py
```

2. Create and activate a virtual environment:
```bash
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install --upgrade pip
pip install -r requirements.txt
```

4. Create a `.env` file in the root directory with the following content:
```env
DATABASE_URL=postgresql://postgres:postgres@localhost:5432/qai_db
SECRET_KEY=your-secret-key-here
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
BACKEND_CORS_ORIGINS=["http://localhost:3000"]
LOG_LEVEL=INFO
```

5. Start the PostgreSQL database using Docker:
```bash
docker compose up -d
```

6. Initialize the database:
```bash
alembic upgrade head
```

7. Seed the database with initial data:
```bash
python -m app.db.init_db
```

This will create the following test users:
- Email: admin@qai.com, Password: admin123
- Email: user@qai.com, Password: user123
- Email: test@qai.com, Password: test123

8. Run the development server:
```bash
uvicorn app.main:app --reload
```

The API will be available at `http://localhost:8000`

## API Documentation

- Swagger UI: `http://localhost:8000/docs`
- ReDoc: `http://localhost:8000/redoc`

## Project Structure

```
qai-backend-py/
├── alembic/              # Database migrations
├── app/
│   ├── api/             # API endpoints
│   ├── core/            # Core functionality
│   ├── crud/            # Database operations
│   ├── db/              # Database configuration
│   │   ├── seeds.py     # Database seed data
│   │   └── init_db.py   # Database initialization script
│   ├── models/          # SQLAlchemy models
│   └── schemas/         # Pydantic schemas
├── tests/               # Test files
├── .env                 # Environment variables
├── docker-compose.yml   # Docker configuration
├── requirements.txt     # Python dependencies
└── README.md           # This file
```

## Development

1. Create a new migration:
```bash
alembic revision --autogenerate -m "description"
```

2. Apply migrations:
```bash
alembic upgrade head
```

3. Run tests:
```bash
pytest
```

## Database Seeding

To seed the database with initial data:

1. Make sure your database is running and migrations are applied:
```bash
docker compose up -d
alembic upgrade head
```

2. Run the seed script:
```bash
python3 -m app.db.init_db
```

## Remove docker volume to reset database

```bash
docker compose down -v
```

To modify the seed data, edit the `app/db/seeds.py` file.

## Production Deployment

1. Update the `.env` file with production values
2. Set up proper CORS origins in `app/main.py`
3. Use a production-grade ASGI server like Gunicorn:
```bash
gunicorn app.main:app -w 4 -k uvicorn.workers.UvicornWorker
```

## License

MIT 