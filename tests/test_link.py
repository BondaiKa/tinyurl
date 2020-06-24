import os
import unittest

import pytest

from app import app, redis
from app.compression import CompressionLink

comp = CompressionLink()


class APITestCase(unittest.TestCase):
    def setUp(self):
        self.app = app
        self.redis = redis
        self.client = self.app.test_client()

        self.long_link = 'https://yandex.ru/'
        self.comp = CompressionLink()

    def test_create_short_link_success(self):
        response = self.client.post('/', data=dict(
            full_link=self.long_link
        ), follow_redirects=True)
        assert response.status_code == 200

    def test_create_short_link_fail(self):
        response = self.client.post('/', data=dict(
            full_link='broke_link'
        ), follow_redirects=True)
        assert response.status_code == 400

    def test_redirect_by_link_success(self):
        full_link = self.long_link
        redis.incr('linked_id')
        counter = int(redis.get('linked_id'))
        short_link = comp.compress_url(counter)
        redis.set(short_link, full_link, nx=True)
        short_link = 'http://0.0.0.0:5000/' + short_link

        response = self.client.get(short_link)
        assert response.status_code == 308

    def test_redirect_by_link_failed(self):
        short_link = 'http://0.0.0.0:5000/' + 'not_exist_page/'
        response = self.client.get(short_link)
        assert response.status_code == 404
