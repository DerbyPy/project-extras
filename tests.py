import flask_webtest
from app import app


class TestViews:
    @classmethod
    def setup_class(cls):
        cls.client = flask_webtest.TestApp(app)

    def test_default(self):
        resp = self.client.get('/')
        assert resp.body == b'Hello World!'

    def test_url_name(self):
        resp = self.client.get('/DerbyPy')
        assert resp.body == b'Hello DerbyPy!'
