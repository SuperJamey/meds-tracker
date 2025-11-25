from sqlmodel import Session
from backend.db import engine
from backend.models import Medication

def seed_data():
    meds = [
        Medication(name="Medication A", strength="10 mg", schedule="Morning, Evening", notes="Sample note"),
        Medication(name="Medication B", strength="5 mg", schedule="As needed", notes="PRN for headaches"),
        Medication(name="Medication C", strength="20 mg", schedule="Bedtime", notes="Helps with sleep"),
    ]
    with Session(engine) as session:
        for med in meds:
            session.add(med)
        session.commit()
        print("Seeded database with sample medications.")

if __name__ == "__main__":
    seed_data()
