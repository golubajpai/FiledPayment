from .models import Card_details,Payment

from marshmallow import post_load
from flask_marshmallow import Marshmallow
from datetime import date
from .credit_card_validation import cards
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
ma=Marshmallow()
from marshmallow import Schema, fields, validate, ValidationError,Schema, fields, post_load,validates




class Payment_sera(SQLAlchemyAutoSchema):
	class Meta:
		model=Payment
	


class Card_details_sera(Schema):
	credit_card_number = fields.Integer(required=True)
	card_holder = fields.Str(required=True,validate=validate.Length(min=1))
	security_code= fields.Str(required=True,validate=validate.Length(min=3,max=3))
	expiration_date = fields.Date(required=True)
	amount= fields.Float(required=True,validate=validate.Range(min=1))


	def dump(self,*args,**kwargs):
		data=super(Card_details_sera,self).dump(*args,**kwargs)
		sera_obj=Payment_sera()
		data['payment_status']=sera_obj.dump(args[0].Payment_status[0])
		return data

	@post_load
	def make_card_object(self, data, **kwargs):
		return Card_details(**data)


	@validates('expiration_date')
	def validate_expiration_date(self,value):
		"""'value' is the datetime parsed from time_created by marshmallow"""
		now = date.today()
		if value < now:
			raise ValidationError("field must be a future date")


	@validates('credit_card_number')
	def validate_credit_card(self,value):
		"""validating card by patterns """
		valid_by_pattern,valid_by_algo=False,False
		for card in cards:
			for pattern in card['patterns']:
				#import pdb;pdb.set_trace()
				if (str(pattern)== str(value)[:len(str(pattern))]):
					print(pattern)
					print(card)
					valid_by_pattern=True


		""" validate card number using the mod 10 algorithm """

		checksum, factor = 0, 1
		for c in reversed(str(value)):
			for c in str(factor * int(c)):
				checksum += int(c)
			factor = 3 -factor
		if checksum % 10== 0:

			valid_by_algo=True

		if valid_by_algo==False or  valid_by_pattern==False:
			raise  ValidationError("invalid credit card number")
		






