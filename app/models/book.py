from sqlalchemy import Column, Integer, String, Date
from sqlalchemy.sql import func
from ..core.database import Base
from datetime import datetime

class Book(Base):
    __tablename__ = "books"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(255), nullable=False, index=True)
    author = Column(String(255), nullable=False, index=True)
    published_date = Column(Date, nullable=False)
    summary = Column(String, nullable=True)
    genre = Column(String(100), nullable=False)

    def __repr__(self):
        return f"<Book(id={self.id}, title='{self.title}', author='{self.author}')>"
    
    @classmethod
    def from_dict(cls, data: dict):
        """Create a Book instance from a dictionary"""
        # Convert string date to datetime.date if needed
        if isinstance(data.get('published_date'), str):
            data['published_date'] = datetime.strptime(
                data['published_date'], 
                '%Y-%m-%d'
            ).date()
        return cls(**data)