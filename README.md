# FastAPI Task Management Service

A scalable, production-ready FastAPI service with a well-organized folder structure for building REST APIs.

## Project Structure

```
Task-Management-Services/
├── app/
│   ├── api/              # API routes
│   │   ├── v1/          # API version 1
│   │   │   ├── users.py
│   │   │   ├── tasks.py
│   │   │   └── __init__.py
│   │   ├── v2/          # API version 2 (for future use)
│   │   └── __init__.py
│   ├── core/            # Core application configuration
│   │   ├── config.py    # Settings and configuration
│   │   ├── database.py  # Database connection and session
│   │   └── __init__.py
│   ├── models/          # SQLAlchemy models
│   │   ├── models.py    # Database models
│   │   └── __init__.py
│   ├── schemas/         # Pydantic schemas
│   │   ├── schemas.py   # Request/response schemas
│   │   └── __init__.py
│   ├── utils/           # Utility functions
│   │   ├── helpers.py   # Helper functions and logging
│   │   └── __init__.py
│   ├── middleware/      # Custom middleware
│   │   └── __init__.py
│   ├── db/              # Database utilities and migrations
│   │   └── __init__.py
│   ├── tests/           # Test files
│   │   ├── test_main.py
│   │   └── __init__.py
│   └── __init__.py
├── main.py              # Application entry point
├── requirements.txt     # Python dependencies
├── .env.example         # Environment variables template
└── README.md           # This file
```

## Setup Instructions

### 1. Create Virtual Environment
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Configure Environment Variables
```bash
cp .env.example .env
```

Edit `.env` and update the configuration values:
- `DATABASE_URL`: PostgreSQL connection string
- `SECRET_KEY`: Change to a secure random key
- `ALLOWED_ORIGINS`: Update CORS origins

### 4. Database Setup
```bash
# Create database tables
python -c "from app.core.database import Base, engine; Base.metadata.create_all(bind=engine)"
```

### 5. Run the Application
```bash
python main.py
```

Or use uvicorn directly:
```bash
uvicorn main:app --reload
```

The API will be available at `http://localhost:8000`

## API Documentation

- **Swagger UI**: http://localhost:8000/docs
- **ReDoc**: http://localhost:8000/redoc
- **OpenAPI JSON**: http://localhost:8000/openapi.json

## Endpoints

### Users
- `POST /api/v1/users/` - Create a new user
- `GET /api/v1/users/{user_id}` - Get user by ID
- `GET /api/v1/users/` - List users (with pagination)

### Tasks
- `POST /api/v1/tasks/` - Create a new task
- `GET /api/v1/tasks/{task_id}` - Get task by ID
- `GET /api/v1/tasks/` - List tasks (with pagination)
- `PUT /api/v1/tasks/{task_id}` - Update task
- `DELETE /api/v1/tasks/{task_id}` - Delete task

## Health Check
- `GET /health` - Service health status
- `GET /` - Root endpoint with service info

## Running Tests
```bash
pytest app/tests/ -v
```

## Configuration Management

The application uses `pydantic-settings` for configuration management. All settings are defined in `app/core/config.py`:

- **App Settings**: Application name and version
- **Server Settings**: Host and port
- **Database Settings**: Connection URL and echo mode
- **JWT Settings**: Secret key and token expiration
- **CORS Settings**: Allowed origins for cross-origin requests

## Scalability Features

1. **Versioned API Routes**: `/api/v1/` and `/api/v2/` for API versioning
2. **Modular Structure**: Separate concerns (models, schemas, routes, utils)
3. **Database Session Management**: Proper session handling with dependency injection
4. **Error Handling**: HTTPException with proper status codes
5. **Middleware Support**: CORS and TrustedHost middleware enabled
6. **Pydantic Validation**: Strong data validation with schemas
7. **Logging**: Built-in logging utilities for debugging

## Development

### Database Migrations
For production, use Alembic for database migrations:
```bash
alembic init migrations
alembic revision --autogenerate -m "Initial migration"
alembic upgrade head
```

### Adding New Endpoints
1. Create a new router in `app/api/v1/new_resource.py`
2. Define models in `app/models/models.py`
3. Define schemas in `app/schemas/schemas.py`
4. Include the router in `app/api/v1/__init__.py`

## Testing

Test files should be placed in `app/tests/` directory. Use pytest with asyncio support for async tests.

## Production Deployment

For production:
1. Set `DEBUG=False` in `.env`
2. Use a production database (PostgreSQL recommended)
3. Set a strong `SECRET_KEY`
4. Deploy with Gunicorn or similar ASGI server:
```bash
gunicorn -w 4 -k uvicorn.workers.UvicornWorker main:app
```

5. Use environment-specific configuration files
6. Implement proper logging and monitoring
7. Use HTTPS in production

## License

MIT License
