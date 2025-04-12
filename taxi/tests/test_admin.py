from django.test import TestCase
from django.contrib.admin.sites import site
from taxi.models import Driver, Car, Manufacturer
from taxi.admin import DriverAdmin, CarAdmin


class AdminTests(TestCase):
    def test_driver_admin_registered(self):
        self.assertIn(Driver, site._registry)
        self.assertIsInstance(site._registry[Driver], DriverAdmin)

    def test_car_admin_registered(self):
        self.assertIn(Car, site._registry)
        self.assertIsInstance(site._registry[Car], CarAdmin)

    def test_manufacturer_admin_registered(self):
        self.assertIn(Manufacturer, site._registry)
