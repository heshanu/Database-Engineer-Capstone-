from django.test import TestCase

# Create your tests here.
#add the following method in Menu class

#TestCase class
class MenuItemTest(TestCase):
    def test_get_item(self):
        item = MenuItem.objects.create(title="IceCream", price=80, inventory=100)
        self.assertEqual(item, "IceCream : 80")

def __str__(self):
        return f'{self.title} : {str(self.price)}'