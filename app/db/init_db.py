import sys
import os

# Add the project root directory to the Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from app.db.session import SessionLocal
from app.db.seeds import init_db

def main() -> None:
    db = SessionLocal()
    try:
        init_db(db)
    finally:
        db.close()

if __name__ == "__main__":
    print("Creating initial data...")
    main()
    print("Initial data created.") 