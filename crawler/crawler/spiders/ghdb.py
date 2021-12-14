#!/usr/bin/python
# -*- coding: utf-8 -*-
import ast
import datetime

from scrapy.http.response.text import TextResponse
import scrapy
import numpy as np

from crawler.utils.generators import GoogleHackingQueries
from crawler.crud import ghdb_categories


class GhdbSpider(scrapy.Spider):
    """
    https://www.exploit-db.com/google-hacking-database
    """
    name = 'ghdb'
    allowed_domains = ['www.exploit-db.com']

    query = GoogleHackingQueries()
    start_urls = [query.__str__()]

    date_fmt = '%Y-%m-%d'

    def parse(self, response, **kwargs):
        for url in self.start_urls:
            yield scrapy.Request(url=url, headers=self.query.headers, callback=self.parse_results_count)

    def parse_results_count(self, response: TextResponse):
        total_results = response.json().get('recordsTotal', 1)

        yield scrapy.Request(url=self.query.get_url(results_count=total_results),
                             headers=self.query.headers, callback=self.parse_ghdb_results)

    def parse_ghdb_results(self, response: TextResponse):
        resp = response.json()
        results = resp.get('data', [])

        all_categories = []
        all_results = []

        for result in results:
            ghdb_result = {
                "id": result.get('id'),
                "date": str(datetime.datetime.strptime(result.get('date'), self.date_fmt)),
                "url_title": result.get('url_title'),
                "cat_id": result.get('cat_id')[0],
                "author_id": result.get('author_id')[0],
                "author_name": result.get('author_id')[1],
            }

            category = result.get('category')

            category_result = {
                "id": category.get('cat_id'),
                "title": category.get('cat_title'),
                "description": category.get('cat_description'),
                "last_update": str(
                    datetime.datetime.strptime(category.get('last_update', '1999-01-01'), self.date_fmt)),
                "records_count": category.get('records_count'),
            }

            all_results.append(ghdb_result)
            all_categories.append(category_result)

        categories = list(np.unique(np.array(all_categories).astype(str)))
        all_categories = []
        for category in categories:
            print("CATEGORY: ", category, self.start_urls)
            all_categories.append(ast.literal_eval(category))

        print(all_categories)
        print('all_categories length: ', len(all_categories))
