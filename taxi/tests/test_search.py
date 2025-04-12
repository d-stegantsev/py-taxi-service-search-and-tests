from django.test import TestCase
from taxi.forms import DriverSearchForm, CarSearchForm, ManufacturerSearchForm


class SearchFormsTest(TestCase):
    def test_driver_search_form_valid_data(self):
        form = DriverSearchForm(data={"username": "testdriver"})
        self.assertTrue(form.is_valid())
        self.assertEqual(form.cleaned_data["username"], "testdriver")

    def test_driver_search_form_empty_data(self):
        form = DriverSearchForm(data={})
        self.assertTrue(form.is_valid())
        self.assertEqual(form.cleaned_data["username"], "")

    def test_car_search_form_valid_data(self):
        form = CarSearchForm(data={"model": "Toyota"})
        self.assertTrue(form.is_valid())
        self.assertEqual(form.cleaned_data["model"], "Toyota")

    def test_car_search_form_empty_data(self):
        form = CarSearchForm(data={})
        self.assertTrue(form.is_valid())
        self.assertEqual(form.cleaned_data["model"], "")

    def test_manufacturer_search_form_valid_data(self):
        form = ManufacturerSearchForm(data={"name": "Ford"})
        self.assertTrue(form.is_valid())
        self.assertEqual(form.cleaned_data["name"], "Ford")

    def test_manufacturer_search_form_empty_data(self):
        form = ManufacturerSearchForm(data={})
        self.assertTrue(form.is_valid())
        self.assertEqual(form.cleaned_data["name"], "")

    def test_fields_present(self):
        self.assertIn("username", DriverSearchForm().fields)
        self.assertIn("model", CarSearchForm().fields)
        self.assertIn("name", ManufacturerSearchForm().fields)
