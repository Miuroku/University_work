from django.test import TestCase
from django.urls import reverse # for accessin urls by their names.
from first_app.models import Product, Category

class CartAddViewTest(TestCase):

    @classmethod
    def setUpTestData(self):        
        Product.objects.create(title='test_title', pk=1, category=Category.objects.create(title='test_cat_title'))

    def test_view_url_exists_atdesired_location(self):
        resp = self.client.post(f'/cart/add/{1}/')
        self.assertEquals(resp.status_code, 302)