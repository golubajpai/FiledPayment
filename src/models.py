from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import relationship
db = SQLAlchemy()





class Card_details(db.Model):
    __tablename__ = 'credit_card_details'

    id = db.Column(db.Integer, primary_key=True)
    credit_card_number = db.Column(db.String())
    card_holder=db.Column(db.String())
    expiration_date=db.Column(db.Date())
    security_code=db.Column(db.String())
    amount =db.Column(db.Float())
    Payment_status = db.relationship("Payment", backref="credit_card_details")

    

    def __init__(self,credit_card_number, card_holder, expiration_date ,amount, security_code ):
        self.credit_card_number=credit_card_number
        self.card_holder= card_holder
        self.expiration_date= expiration_date
        self.security_code = security_code
        self.amount = amount
     

    def __repr__(self):
        return "< {} {} >".format(self.card_holder,self.id)




class Payment(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    card_id=db.Column(db.Integer,db.ForeignKey('credit_card_details.id'))
    gateway_used = db.Column(db.String())