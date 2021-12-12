#!/usr/bin/python
# -*- coding: utf-8 -*-
from sqlalchemy import Column, Integer, String, Date

from crawler.db.base_class import Base


class Ghdb_Categories(Base):  # noqa
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    description = Column(String)
    last_update = Column(Date)
    results_count = Column(Integer)
