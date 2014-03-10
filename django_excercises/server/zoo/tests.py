from django.test import TestCase
import json

# Create your tests here.
class ZooTest(TestCase):

    def test_store(self):
        resp = self.client.post(
            "/zoo",
            '{"nome":"Zebra"}',
            content_type='application/json'
            )
        self.assertEqual(resp.status_code, 200)


    def test_fetch(self):
        resp = self.client.post(
            "/zoo",
            '{"nome":"Zebra"}',
            content_type='application/json'
            )
        self.assertEqual(resp.status_code, 200)

        resp = self.client.get('/zoo')
        self.assertEqual(resp.status_code,200)
        content = json.loads(resp.content)
        self.assertEqual(content[0]['nome'], 'Zebra')

        
