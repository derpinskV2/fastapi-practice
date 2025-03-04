from pydantic import EmailStr
from sqlmodel import Field, Session, SQLModel, create_engine, select


class User(SQLModel, table=True):
    id: int = Field(primary_key=True)
    email: EmailStr = Field(nullable=False, index=True)
