"""
General functions
"""
from my_lib.database import DatabaseInterface
from .general import crud_template, validate

database = DatabaseInterface()

URI = '/api/v1/'

__all__ = ['database', 'URI', 'crud_template', 'validate']