from django.test import TestCase
from mydealsapp.models import product

# Create your tests here.

class MyTest(TestCase):
	def test_record(self):
		try:
			obj = product(name = "VICKY",
				description = "I WANT A ONEPLUS",
				costperitem = 12,
				stockquantity = 25)
			obj.save()
			self.assertEquals(obj.stockquantity,12,"quantity mismatch")
			self.assertEquals(obj.costperitem,25,"cost mismatch")
			self.assertEquals(obj.volume,300,"volume mismatch")
		except Exception as e:
			print('unable to insert the record')


	
	