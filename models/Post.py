from sqlalchemy import Integer,String,TIMESTAMP
from sqlalchemy.orm import Mapped,mapped_column
from app import db

class Post(db.Model):
    id : Mapped[int] = mapped_column(Integer,primary_key=True)
    title : Mapped[String] = mapped_column(String(100), nullable=True)
    description : Mapped[String] = mapped_column(String(100))
    created_at : Mapped[TIMESTAMP] = mapped_column(TIMESTAMP)
    updated_at : Mapped[TIMESTAMP] = mapped_column(TIMESTAMP)

    def __repr__(self):
        return f"<Post {self.title}>"