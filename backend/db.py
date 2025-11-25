from sqlmodel import SQLModel, create_engine
from backend.models import Medication

# SQLite database file
sqlite_file_name = "meds.db"
sqlite_url = f"sqlite:///{sqlite_file_name}"

create_engine = create_engine(sqlite_url, echo=True)

def create_db_and_tables():
  SQLModel.metadata.create_all(create_engine)
