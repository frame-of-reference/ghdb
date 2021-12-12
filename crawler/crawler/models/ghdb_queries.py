#!/usr/bin/python
# -*- coding: utf-8 -*-
from sqlalchemy import Column, ForeignKey, Integer, String, Date
from sqlalchemy.orm import relationship

from crawler.db.base_class import Base


class Ghdb_Queries(Base):  # noqa
    id = Column(Integer, primary_key=True, index=True)
    date = Column(Date)
    title = Column(String, index=True)
    category_id = Column(Integer, ForeignKey('ghdb_categories.id'))
    category = relationship('Ghdb_Categories')
