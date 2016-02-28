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

    def login(self, username, password):
        return self.app.post('/login',
                             data={"username": username, "password": password},
                             follow_redirects=True)

    def logout(self):
        return self.app.get('/logout', follow_redirects=True)

    def test_empty_db(self):
        rcvd = self.app.get('/')
        self.assertIn("No entries.", rcvd.data.decode('utf-8'))

    def test_logs_in(self):
        rcvd = self.login('admin', 'default_password')
        self.assertIn('Successfully logged in.', rcvd.data.decode('utf-8'))

    def test_logs_out(self):

        rcvd = self.logout()
        self.assertIn('Logged out', rcvd.data.decode('utf-8'))

    def test_does_not_log_in_with_wrong_username(self):

        rcvd = self.login('invaliduser', 'default_password')
        self.assertIn('Invalid username', rcvd.data.decode('utf-8'))

    def test_does_not_log_in_with_incorrect_password(self):

        rcvd = self.login('admin', 'invalid_password')
        self.assertIn('Invalid password', rcvd.data.decode('utf-8'))

if __name__ == '__main__':
    unittest.main()
