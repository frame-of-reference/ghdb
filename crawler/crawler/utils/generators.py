#!/usr/bin/python
# -*- coding: utf-8 -*-
from typing import Optional
from urllib.parse import urlencode


class GoogleHackingQueries(object):
    """Generate URLs for GHDB API

    Usage: GoogleHackingQueries().__str__() for live GHDB results count or GoogleHackingQueries(results_count=500).__str__()

    @:param results_count, optional - set number of results to return
    :return
    """
    url = 'https://www.exploit-db.com/google-hacking-database/?'

    headers = {
        "Accept": "application/json, text/javascript, */*; q=0.01",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "en-US,en;q=0.5",
        "Connection": "keep-alive",
        "Cookie": "XSRF-TOKEN=eyJpdiI6IkFcL2hFOGRIbzZ0V0tjNHBKanRPdHp3PT0iLCJ2YWx1ZSI6Inkzb0RMNGQ0bGtBMGtWcVlSK1JGa2JsZkx6Y1drTUtOcUt2OG9jM0wrNjdmaTBqMG40cnl5SkwyV2E4TVpONkMiLCJtYWMiOiIxY2JkMTY0ZmU4NDJjNGUzMGU4ZDZjM2Q4ZTQwZTI1MjBlZTk5MjIxOTdhYTY2YzQyOGI3ZDllNDJiOWJhNTIxIn0%3D; exploit_database_session=eyJpdiI6IjZ0b2hjaVA2XC9DRGdyUWZkT2dvQW53PT0iLCJ2YWx1ZSI6IlkxSlwvOE4rTlhGQ1JYc0F1aUVPcnRkTFN1eTZNVkd0ZUhPa2d0OFhtYlQ2NXpUczdVQmdlSGR0VlVzY0pZXC9zaSIsIm1hYyI6IjgzYWYyNmE0NzI0OWQyMjU1NTM4NjE5NjMyZTk0ZGYyZmQ3MTYzZGYwNmQ4YWNkYjBiOTFlMDZkZjZiZjQyMDkifQ%3D%3D; CookieConsent={stamp:%27-1%27%2Cnecessary:true%2Cpreferences:true%2Cstatistics:true%2Cmarketing:true%2Cver:1%2Cutc:1639249966374%2Cregion:%27CA%27}",
        "Host": "www.exploit-db.com",
        "Referer": "https://www.exploit-db.com/google-hacking-database",
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-origin",
        "TE": "trailers",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36",
        "X-Requested-With": "XMLHttpRequest",
    }

    query_params = {
        'draw': 1,
        'columns[0][data]': 'date',
        'columns[0][name]': 'date',
        'columns[0][searchable]': True,
        'columns[0][orderable]': True,
        'columns[0][search][regex]': False,
        'columns[1][data]': 'url_title',
        'columns[1][name]': 'url_title',
        'columns[1][searchable]': True,
        'columns[1][orderable]': False,
        'columns[1][search][regex]': False,
        'columns[2][data]': 'cat_id',
        'columns[2][name]': 'cat_id',
        'columns[2][searchable]': True,
        'columns[2][orderable]': False,
        'columns[2][search][regex]': False,
        'columns[3][data]': 'author_id',
        'columns[3][name]': 'author_id',
        'columns[3][searchable]': False,
        'columns[3][orderable]': False,
        'columns[3][search][regex]': False,
        'order[0][column]': 0,
        'order[0][dir]': 'desc',
        'start': 0,
        'length': 1,
        'search[regex]': False,
        '_': 1639249970926
    }

    def __str__(self):
        return self.url + urlencode(self.query_params)

    def get_url(self, results_count: Optional[int] = 1):
        params = self.query_params
        params['length'] = results_count
        return self.url + urlencode(params)

    def __repr__(self):
        return f'GoogleHackingQueries(results_count={self.query_params.get("length")})'
