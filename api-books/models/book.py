from uuid import uuid4

from sqlalchemy import String, Text
from sqlalchemy.dialects.postgresql import UUID

from db import db


class Book(db.Model):
    __tablename__ = "book"

    id = db.Column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid4
    )

    title = db.Column(
        String(255),
        nullable=False
    )

    author = db.Column(
        String(255),
        nullable=False
    )

    description = db.Column(
        Text,
        nullable=False
    )

    is_favorite = db.Column(
        db.Boolean,
        nullable=False,
        default=False
    )

    is_reading = db.Column(
        db.Boolean,
        nullable=False,
        default=False
    )

    is_finished = db.Column(
        db.Boolean,
        nullable=False,
        default=False
    )

    def as_dict(self):
        return {
            "id": str(self.id),
            "title": self.title,
            "author": self.author,
            "description": self.description,
            "is_favorite": self.is_favorite,
            "is_reading": self.is_reading,
            "is_finished": self.is_finished
        }