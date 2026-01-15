from sqlalchemy import Column, Integer, String

from project.database import Base


class User(Base):
    __tablename__ = "users"

    id = Column[int](Integer, primary_key=True, autoincrement=True)
    username = Column[str](String(128), unique=True, nullable=False)
    email = Column[str](String(128), unique=True, nullable=False)

    # This enforces that we provide the username and email when creating a new user.
    # Otherwise, we could create an empty user, that would be invalid when we try to save it to the database.
    def __init__(self, username: str, email: str, *args, **kwargs):
        self.username = username
        self.email = email
