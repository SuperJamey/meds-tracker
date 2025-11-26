from sqlmodel import SQLModel, Field
from typing import Optional

class Medication(SQLModel, table=True):
  id: Optional[int] = Field(default=None, primary_key=True)
  name: str
  strength: Optional[str] = None
  schedule: Optional[str] = None
  notes: Optional[str] = None
  