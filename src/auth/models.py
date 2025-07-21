from datetime import datetime
from sqlmodel import SQLModel, Field, Column
import sqlalchemy.dialects.postgresql as pg

import uuid


class User(SQLModel, table=True):

    __tablename__ = "user_accounts"

    uid: uuid.UUID = Field(
        sa_column=Column(
            uuid.uuid4,
            primary_key=True,
            unique=True,
            nullable=False,
            default=uuid.uuid4,
            info={"description": "Unique identifier for the use account"}
        )
    )

    username: str
    first_name: str = Field(nullable=True)
    last_name: str = Field(nullable=True)
    is_verified: bool = False
    email: str
    password_hash: str
    
    created_at: datetime = Field(
        sa_column=Column(
            pg.TIMESTAMP, default=datetime.now()
        )
    )

    def __repr__(self):
        return f"User <{self.username}>"



