from sqlalchemy.orm import Session
from app.crud import crud_user
from app.schemas.user import UserCreate
from app.core.security import get_password_hash
from app.models import UserRole

def seed_roles(db: Session) -> None:
    """Seed the user_roles table with initial data."""
    
    roles = [
        {
            "name": "SUPER_ADMIN",
            "description": "Super Administrator with full system access"
        },
        {
            "name": "ADMIN",
            "description": "Administrator with system management access"
        },
        {
            "name": "APP_USER",
            "description": "Application user with limited access"
        }
    ]
    
    for role_data in roles:
        existing_role = db.query(UserRole).filter(UserRole.name == role_data["name"]).first()
        if not existing_role:
            role = UserRole(**role_data)
            db.add(role)
            print(f"Created role: {role_data['name']}")
        else:
            print(f"Role already exists: {role_data['name']}")
    
    db.commit()

def seed_users(db: Session) -> None:
    """Seed the users table with initial data."""
    
    # Get role IDs
    super_admin_role = db.query(UserRole).filter(UserRole.name == "SUPER_ADMIN").first()
    admin_role = db.query(UserRole).filter(UserRole.name == "ADMIN").first()
    app_user_role = db.query(UserRole).filter(UserRole.name == "APP_USER").first()
    
    # List of users to create
    users = [
        {
            "email": "superadmin@qai.com",
            "password": "superadmin123",
            "first_name": "Super",
            "last_name": "Admin",
            "role_id": super_admin_role.id,
            "is_active": True
        },
        {
            "email": "admin@qai.com",
            "password": "admin123",
            "first_name": "Admin",
            "last_name": "User",
            "role_id": admin_role.id,
            "is_active": True
        },
        {
            "email": "appuser@qai.com",
            "password": "appuser123",
            "first_name": "App",
            "last_name": "User",
            "role_id": app_user_role.id,
            "is_active": True
        }
    ]
    
    # Create each user
    for user_data in users:
        # Check if user already exists
        existing_user = crud_user.get_user_by_email(db, email=user_data["email"])
        if not existing_user:
            user_in = UserCreate(**user_data)
            crud_user.create_user(db, user=user_in)
            print(f"Created user: {user_data['email']}")
        else:
            print(f"User already exists: {user_data['email']}")

def init_db(db: Session) -> None:
    """Initialize the database with seed data."""
    print("Creating initial data...")
    seed_roles(db)
    seed_users(db)
    print("Initial data created.") 