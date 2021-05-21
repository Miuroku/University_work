from django.test import TestCase
from django.urls import reverse # for accessin urls by their names.


class CouponApplyViewTest(TestCase):

    def test_view_url_exists_atdesired_location(self):
        resp = self.client.post('/coupons/apply/')
        self.assertEquals(resp.status_code, 302)

    def test_view_url_accessible_by_name(self):
        resp = self.client.post(reverse('coupons:coupon_apply'))
        self.assertEqual(resp.status_code, 302)
