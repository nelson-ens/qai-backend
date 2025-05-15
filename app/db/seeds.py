from sqlalchemy.orm import Session
from app.crud import crud_user
from app.schemas.user import UserCreate
from app.core.security import get_password_hash

def seed_users(db: Session) -> None:
    """Seed the users table with initial data."""
    
    # List of users to create
    users = [
        {
            "email": "admin@qai.com",
            "password": "admin123",  # This will be hashed
            "is_active": True
        },
        {
            "email": "user@qai.com",
            "password": "user123",  # This will be hashed
            "is_active": True
        },
        {
            "email": "test@qai.com",
            "password": "test123",  # This will be hashed
            "is_active": True
        }
    ]
    
    # Create each user
    for user_data in users:
        # Check if user already exists
        existing_user = crud_user.get_user_by_email(db, email=user_data["email"])
        if not existing_user:
            user_in = UserCreate(
                email=user_data["email"],
                password=user_data["password"]
            )
            crud_user.create_user(db, user=user_in)
            print(f"Created user: {user_data['email']}")
        else:
            print(f"User already exists: {user_data['email']}")

def init_db(db: Session) -> None:
    """Initialize the database with seed data."""
    print("Creating initial data...")
    seed_users(db)
    print("Initial data created.") 