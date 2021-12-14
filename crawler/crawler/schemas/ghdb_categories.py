#!/usr/bin/python
# -*- coding: utf-8 -*-
import datetime

from pydantic import BaseModel


# Shared properties
class GhdbCategoriesBase(BaseModel):
    title: str
    description: str
    last_update: datetime.datetime
    results_count: int


# Properties to receive on GhdbCategories creation
class GhdbCategoriesCreate(GhdbCategoriesBase):
    id: int
    title: str
    description: str
    last_update: datetime.datetime
    results_count: int


# Properties to receive on GhdbCategories update
class GhdbCategoriesUpdate(GhdbCategoriesBase):
    last_update: datetime.datetime
    results_count: int


# Properties shared by models stored in DB
class GhdbCategoriesInDBBase(GhdbCategoriesBase):
    id: int
    title: str
    description: str
    last_update: datetime.datetime
    results_count: int

    class Config:
        orm_mode = True


# Properties to return to client
class GhdbCategories(GhdbCategoriesInDBBase):
    pass


# Properties stored in DB
class GhdbCategoriesInDB(GhdbCategoriesInDBBase):
    pass
