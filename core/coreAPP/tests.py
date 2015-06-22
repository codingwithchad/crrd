
from django.test import TestCase

from .models import UseCat, ReuseItem, Business, RepCat, RepairItem, RepBusiness
# Create your tests here.

class urlTests(TestCase):
    def test_useCat(self):
        response = self.client.get("http://52.26.111.76:8000/crrd/usecat/")
        self.assertEqual(response.status_code, 200)
   
    def test_useItems(self):
        response = self.client.get("http://52.26.111.76:8000/crrd/7/useitems/")
        self.assertEqual(response.status_code, 200)

    def test_business(self):
        response = self.client.get("http://52.26.111.76:8000/crrd/27/business/")
        self.assertEqual(response.status_code, 200)

    def test_busdetail(self):
        response = self.client.get("http://52.26.111.76:8000/crrd/3/busdetail/")
        self.assertEqual(response.status_code, 200)

    def test_repCat(self):
        response = self.client.get("http://52.26.111.76:8000/crrd/repcat/repair/")
        self.assertEqual(response.status_code, 200)

    def test_repItems(self):
        response = self.client.get("http://52.26.111.76:8000/crrd/4/repitems/")
        self.assertEqual(response.status_code, 200)

    def test_repBusiness(self):
        response = self.client.get("http://52.26.111.76:8000/crrd/6/repbusiness/")
        self.assertEqual(response.status_code, 200)

    def test_repBusDet(self):
        response = self.client.get("http://52.26.111.76:8000/crrd/1/repbusdetail/")
        self.assertEqual(response.status_code, 200)
    def test_badUrl(self):
        response = self.client.get("http://52.26.111.76:8000/crrd/1/badUrl/")
        self.assertEqual(response.status_code, 404)