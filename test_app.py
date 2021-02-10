
from app import app 
import unittest, json

class AppTestCase(unittest.TestCase):
    def test_status(self):
        response = app.test_client(self).get('/')
        self.assertEqual(response.status_code,200)
    
    def test_response(self):
        response = app.test_client(self).get('/')
        data = json.loads(response.get_data(as_text=True))

        self.assertEqual(data['mean'],1721.13)
        self.assertEqual(data['sum'],213420)

if __name__ == '__main__':
    unittest.main()