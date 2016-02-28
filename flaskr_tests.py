import os
import unittest
import tempfile

import flaskr


class FlaskrTestCase(unittest.TestCase):

    def setUp(self):
        self.db_fd, flaskr.app.config['DATABASE'] = tempfile.mkstemp()
        flaskr.app.config['TESTING'] = True
        self.app = flaskr.app.test_client()
        flaskr.init_db()

    def tearDown(self):
        os.close(self.db_fd)
        os.unlink(flaskr.app.config['DATABASE'])

    def test_empty_db(self):
        rcvd = self.app.get('/')
        self.assertIn("No entries.", rcvd.data.decode('utf-8'))

if __name__ == '__main__':
    unittest.main()
