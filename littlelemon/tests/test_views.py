from django.test import TestCase
from restaurant.models import Menu


#TestCase class
class MenuViewTest(TestCase):
    def setup(self):
        item = Menu.objects.create(title="IceCream", price=80, inventory=100)
        self.assertEqual(item, "IceCream : 80")

    def test_getall(self):
        item = Menu.objects.all()
        self.assertEqual(item, "IceCream : 80")
