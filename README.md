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
docker-compose up -d
```

6. Initialize the database:
```bash
alembic upgrade head
```

7. Run the development server:
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

## Production Deployment

1. Update the `.env` file with production values
2. Set up proper CORS origins in `app/main.py`
3. Use a production-grade ASGI server like Gunicorn:
```bash
gunicorn app.main:app -w 4 -k uvicorn.workers.UvicornWorker
```

## License

MIT 