import unittest

from test.rely import db
from test.rely.utils.db_utils import setup_database


class TestRelyApis(unittest.TestCase):
    def setUp(self) -> None:
        setup_database()
        print("initialising db setup successful")

    def tearDown(self) -> None:
        db.session.close()
