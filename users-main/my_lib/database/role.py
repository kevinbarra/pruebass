from sqlalchemy import Column, Integer, VARCHAR
from .base import Base

class Role(Base):
    '''
    Role model
    '''
    __tablename__ = 'roles'
    id = Column(Integer(), primary_key=True, autoincrement=True)
    nombre = Column(VARCHAR(50), nullable=False)

    def serialize(self):
        """
        Serialize the data

        Returns:
            dict: The serialized data
        """

        return {
            "id": self.id,
            "nombre": self.nombre,
        }