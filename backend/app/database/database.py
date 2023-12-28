from sqlmodel import create_engine,SQLModel
from app.core.settings import settings

engine = create_engine(settings.SQLALCHEMY_DATABASE_URI)



def create_db_and_tables():
    SQLModel.metadata.create_all(engine)