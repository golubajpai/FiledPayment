from flask.views import MethodView
from .models import Card_details
from flask import request,session,abort,jsonify,make_response
from flask_restplus import Resource
from sqlalchemy import engine
from sqlalchemy.orm import scoped_session, sessionmaker
from .serailizer import Card_details_sera,Payment_sera
from  marshmallow.exceptions import ValidationError
from json.decoder import JSONDecodeError
from .models import db
from .payment import Base_payment_gateway






class ProcessPayment(Resource):
	serailizer=Card_details_sera()

	def post(self):
		try:
			data=request.get_json(force=True)
			obj=self.serailizer.load(data)
			db.session.add(obj)
			db.session.commit()
			base_obj=Base_payment_gateway(obj)
			base_obj.make_payment()
			return make_response(jsonify(self.serailizer.dump(obj)),200)

		except ValidationError as e:
			return make_response(jsonify({'error':e.messages}),400)
		except Exception as e:
			print(e)

			return make_response(jsonify({"error":"internal server error"}),500)