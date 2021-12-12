#!/usr/bin/python
# -*- coding: utf-8 -*-
from typing import Optional, Dict, Any

from pydantic import BaseSettings, PostgresDsn, validator


class MetaSettings(BaseSettings):
    SCRAPY_SETTINGS_MODULE: str
    SCRAPY_PROXIES_PATH: Optional[str] = '../proxies.txt'

    SQLALCHEMY_DATABASE_URI: Optional[PostgresDsn] = None

    @validator("SQLALCHEMY_DATABASE_URI", pre=True)
    def assemble_db_connection(cls, v: Optional[str], values: Dict[str, Any]) -> Any:
        if isinstance(v, str):
            return v
        return PostgresDsn.build(
            scheme="postgresql",
            user=values.get("POSTGRES_USER"),
            password=values.get("POSTGRES_PASSWORD"),
            host=values.get("POSTGRES_SERVER"),
            path=f"/{values.get('POSTGRES_DB') or ''}",
        )

    class Config:
        case_sensitive = True
        env_file = '../../.env'
        env_file_encoding = 'utf-8'


config = MetaSettings()
