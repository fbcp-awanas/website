from django.test import TestCase
from .models import Family, Child
from .models import Clubber, Visitor


# Create your tests here.
class FamilyTestCase(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.doe = Family.objects.create(
            slug='Doe',
            ICEContactName='Geoff Doe',
            ICEContactPhone='214-555-1212',
            address='1234 Nota Street',
            city='Plano',
            state='TX',
            zip='75080'
        )
        cls.smith = Family.objects.create(
            slug='Smith',
            ICEContactName='Bob Smythe',
            ICEContactNumber='469-555-1212',
            address='2345 Nota Street',
            city='Plano',
            state='TX',
            zip='75080'
        )


class ChildTestCase(TestCase):
    pass
    # def setUp(self):
    #     Child.objects.create()
