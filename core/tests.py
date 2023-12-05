from datetime import datetime

from django.test import TestCase
from core.models import Product, Author, Landmark, Quote, Booking


class ProductTest(TestCase):
    def test_model_generate_field(self):
        data = {'info': {'version': 35}}
        p = Product.objects.create(slug='first-product', data=data)
        self.assertEquals(p.version, '35')


class QuoteTest(TestCase):
    def test_model_generate_field(self):
        p = Quote.objects.create(
            author='aliRahmani',
            text='anyway, some english word in this world,'
                 ' And you find here english ENGLISH English ENglish words for test')
        self.assertEquals(p.search, "'anyway':1 'english':3,12,13,14,15 'find':10 'test':18 'word':4,16 'world':7")


class AuthorTest(TestCase):
    def test_model_generate_field(self):
        p = Author.objects.create(first_name='Lodging', last_name='Wittgenstein')
        self.assertEquals(p.full_name, "Lodging Wittgenstein")


class LandmarkTest(TestCase):
    def test_model_generate_field(self):
        p = Landmark.objects.create(name='blue', reviews=[4, 4, 5, 1, 2])
        self.assertEquals(p.count, 5)


class BookingTest(TestCase):
    def test_model_generate_field(self):
        from datetime import timedelta
        now_date = datetime.now().date()
        p = Booking.objects.create(start=now_date, end=now_date + timedelta(days=1))
        self.assertEquals(p.span.__str__(), '[2023-12-05, 2023-12-06)')
