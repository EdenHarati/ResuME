from django.test import TestCase
from myapp.models import MyModel

class MyModelTest(TestCase):
    def test_create_object(self):
        new_object = MyModel(field1="value1", field2="value2")
        new_object.save()
        self.assertEqual(MyModel.objects.count(), 1)
