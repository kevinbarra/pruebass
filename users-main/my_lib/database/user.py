from datetime import datetime as dt
from sqlalchemy import Column, Integer, VARCHAR, TIMESTAMP, Boolean, ForeignKey
from .base import Base

class User(Base):
    '''
    User model
    '''
    __tablename__ = 'users'

    id = Column(Integer(), primary_key=True, autoincrement=True)
    id_role = Column(Integer(), ForeignKey('roles.id'), nullable=False)
    name = Column(VARCHAR(50), nullable=False)
    lastname = Column(VARCHAR(50), nullable=False)
    email = Column(VARCHAR(100), nullable=False, unique=True)
    password = Column(VARCHAR(128), nullable=False)
    created_at = Column(TIMESTAMP(), nullable=False, default=dt.now())
    updated_at = Column(TIMESTAMP(), nullable=False, default=dt.now())
    is_banned = Column(Boolean(), nullable=False, default=False)

    def serialize(self):
        """
        Serialize the data

        Returns:
            dict: The serialized data
        """

        return {
            "id": self.id,
            "id_role": self.id_role,
            "name": self.name,
            "lastname": self.lastname,
            "email": self.email,
            "is_banned": self.is_banned
        }