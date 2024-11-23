from sqlalchemy import Integer, String, TIMESTAMP
from sqlalchemy.orm import Mapped, mapped_column
from datetime import datetime
from app import db 

class User(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[String] = mapped_column(String(100))
    email: Mapped[String] = mapped_column(String(100), unique=True)
    password: Mapped[String] = mapped_column(String(100))
    created_at: Mapped[TIMESTAMP] = mapped_column(TIMESTAMP, default=datetime.now)
    updated_at: Mapped[TIMESTAMP] = mapped_column(TIMESTAMP, default=datetime.now,onupdate=datetime.now)

    def __repr__(self):
        return f"<User {self.name}>"
