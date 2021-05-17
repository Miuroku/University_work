from django.test import TestCase

from first_app.models import Product, Category

class GetAboutUsViewTest(TestCase):

    def test_view_url_exists_atdesired_location(self):
        resp = self.client.get('/about_us/')
        self.assertEquals(resp.status_code, 200)

class GetSpecificProductViewTest(TestCase):

    @classmethod
    def setUpTestData(self):
        # create 4 products.
        number_of_products = 3        
        for product_num in range(number_of_products):
            Product.objects.create(title=f'my_product-{product_num}', category=Category.objects.create(title=f'Category-{product_num}'))
    
    def test_view_url_exists_atdesired_location(self):
        resp = self.client.get(f'/products/{Product.objects.get(pk=1)}/')
        self.assertEquals(resp.status_code, 200)