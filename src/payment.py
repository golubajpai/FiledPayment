from .models import Payment
from .models import db


class CheapPaymentGateway:
	def __init__(self,card_object):
		self.card_object=card_object
		self.model=Payment

	def process(self):
		obj=self.model(**{'gateway_used':self.__class__.__name__,'card_id':self.card_object.id})
		db.session.add(obj)
		db.session.commit()
		print(obj.__dict__)
		return True




class ExpensivePaymentGateway(CheapPaymentGateway):
	pass

class PremiumPaymentGateway(CheapPaymentGateway):
	def process(self):
		i=0
		while i<3:
			try:
				print('abc')
				super(PremiumPaymentGateway,self).process()
				i=i+3
			except Exception as e :
				print(e)
				i=i+1

class Base_payment_gateway:
	def __init__(self,card_object):
		self.card_object=card_object

	def make_payment(self):
		if self.card_object.amount<=20:
			gateway_object=CheapPaymentGateway(self.card_object)
			gateway_object.process()
			return True

		if self.card_object.amount>20 and self.card_object.amount<500:
			gateway_object=ExpensivePaymentGateway(self.card_object)
			gateway_object.process()

		if self.card_object.amount>500:
			gateway_object=PremiumPaymentGateway(self.card_object)
			gateway_object.process()
