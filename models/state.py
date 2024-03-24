#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from models.city import City
from models import storage

class State(BaseModel, Base):
    """ State class """
    __tablename__ = "states"
    name = Column(String(128), nullable=False)

    cities = relationship("City", backref="state",
            cascade="all, delete, delete-orphan")

    @property
    def cities():
        list_cities = []
        cities = models.storage.all(City).values()
        for city in cities:
            if city.state_id == self.id:
                list_cities.append(city)
        return list_cities
