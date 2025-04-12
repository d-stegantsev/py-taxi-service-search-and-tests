from django.test import TestCase
from taxi.models import Driver, Car, Manufacturer
from django.urls import reverse


class ModelTests(TestCase):
    def setUp(self):
        self.manufacturer = Manufacturer.objects.create(name="Toyota", country="Japan")
        self.driver = Driver.objects.create_user(
            username="driver1",
            password="pass",
            first_name="Test",
            last_name="Driver",
            license_number="ABC123",
        )
        self.car = Car.objects.create(model="Corolla", manufacturer=self.manufacturer)
        self.car.drivers.add(self.driver)

    def test_driver_str(self):
        self.assertEqual(str(self.driver), "driver1 (Test Driver)")

    def test_car_str(self):
        self.assertEqual(str(self.car), "Corolla")

    def test_manufacturer_str(self):
        self.assertEqual(str(self.manufacturer), "Toyota Japan")

    def test_get_absolute_url(self):
        url = self.driver.get_absolute_url()
        self.assertEqual(
            url, reverse("taxi:driver-detail", kwargs={"pk": self.driver.pk})
        )
