import unittest

from app import app


class AppTestCase(unittest.TestCase):
    def setUp(self):
        self.ctx = app.app_context()
        self.ctx.push()
        self.client = app.test_client()

    def tearDown(self):
        self.ctx.pop()

    def test_login(self):
        response = self.client.get('/login/')
        self.assertEqual(response.status_code, 200)

    def test_index(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_register(self):
        response = self.client.get('/register/')
        self.assertEqual(response.status_code, 200)

    def test_logged_in(self):
        response = self.client.get('/logged_in/')
        self.assertEqual(response.status_code, 200)
        
    def test_about(self):
        response = self.client.get('/about/')
        self.assertEqual(response.status_code, 200)

    def test_logout(self):
        response = self.client.get('/logout/')
        self.assertEqual(response.status_code, 200)

    

    
    



if __name__ == "__main__":
    unittest.main()
