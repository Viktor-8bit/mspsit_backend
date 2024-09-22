
from typing import List
from typing import Optional
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship
from sqlalchemy import Integer, String, ForeignKey, create_engine, DateTime


import Base



class Comment(Base):
    __tablename__ = "comments"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
   
    comment_text: Mapped[str] = mapped_column(String(255))
    log_id: Mapped[int] = mapped_column(ForeignKey("logs.id"))

    def __repr__(self) -> str:
        return f"Comment(id={self.id!r}, comment_text={self.comment_text!r})"
