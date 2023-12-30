# Define a base model with created_at and updated_at fields
from datetime import datetime

from sqlmodel import Field,SQLModel


class BaseModel(SQLModel):
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)