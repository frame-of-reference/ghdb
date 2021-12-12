#!/usr/bin/python
# -*- coding: utf-8 -*-
from pydantic import BaseModel


# Shared properties
class GhdbAuthorBase(BaseModel):
    name: str

# Properties to receive on GhdbAuthor creation
class GhdbAuthorCreate(GhdbAuthorBase):
    id: int
    name: str


# Properties to receive on GhdbAuthor update
class GhdbAuthorUpdate(GhdbAuthorBase):
    pass


# Properties shared by models stored in DB
class GhdbAuthorInDBBase(GhdbAuthorBase):
    id: int
    name: str

    class Config:
        orm_mode = True


# Properties to return to client
class GhdbAuthor(GhdbAuthorInDBBase):
    id: str
    name: str


# Properties stored in DB
class GhdbAuthorInDB(GhdbAuthorInDBBase):
    pass
