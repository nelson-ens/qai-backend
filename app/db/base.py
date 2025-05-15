from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

# Import all models here for Alembic to detect them
from app.db.base_class import Base  # noqa
from app.models.user_role import UserRole  # noqa
from app.models.user import User  # noqa 