#!/usr/bin/python
# -*- coding: utf-8 -*-
from sqlalchemy import Column, ForeignKey, Table

from crawler.db.base_class import Base

Ghdb_Authors_Queries = Table('ghdb_authors_queries', Base,
    Column('ghdb_author_id', ForeignKey('ghdb_authors.id')),  # noqa
    Column('ghdb_queries_id', ForeignKey('ghdb_queries.id'))
)
