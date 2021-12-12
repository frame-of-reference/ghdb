#!/usr/bin/python
# -*- coding: utf-8 -*-
from typing import Optional

from pydantic import BaseModel


# Shared properties
class GhdbQueriesBase(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None


# Properties to receive on GhdbQueries creation
class GhdbQueriesCreate(GhdbQueriesBase):
    title: str


# Properties to receive on GhdbQueries update
class GhdbQueriesUpdate(GhdbQueriesBase):
    pass


# Properties shared by models stored in DB
class GhdbQueriesInDBBase(GhdbQueriesBase):
    id: int
    title: str

    class Config:
        orm_mode = True


# Properties to return to client
class GhdbQueries(GhdbQueriesInDBBase):
    pass


# Properties stored in DB
class GhdbQueriesInDB(GhdbQueriesInDBBase):
    pass