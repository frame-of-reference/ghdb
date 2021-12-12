#!/usr/bin/python
# -*- coding: utf-8 -*-
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from crawler.db.base_class import Base
from crawler.models.ghdb_authors_queries import Ghdb_Authors_Queries

class Ghdb_Authors(Base):  # noqa
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    results = relationship("Ghdb_Queries",
                           secondary=Ghdb_Authors_Queries)