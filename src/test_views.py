import pytest
import requests
import json
from flask import  request
import os
import unittest
from flask import Flask
from flask_testing import LiveServerTestCase
from config import DevConfig
from flask_testing import TestCase
from models import db
import sys
from utils import connection_check



class MyTest(unittest.TestCase):
    url=os.environ.get("base_url")+"payment/"
    data={"credit_card_number":"5553042241984105","card_holder":"sdhlj;klj;lkj;lkj;lkjlkf","expiration_date":"2022-12-06","security_code":"121","amount":"1.2"}

    


    def run(self, result=None):
        """ Stop after first error """

        if not result.errors:
            super(MyTest, self).run(result)






    def test_withallvalue(self):
        response=requests.post(url=self.url,data=json.dumps(self.data))
        print(response.text)
        assert  response.status_code==200
        assert response.json()["payment_status"]["gateway_used"]=="CheapPaymentGateway"


    def test_wrong_credit_card(self):
    	self.data['credit_card_number']="123123123"
    	response=requests.post(url=self.url,data=json.dumps(self.data))
    	assert response.status_code==400


    def test_invalid_expiration_date(self):
    	self.data['expiration_date']="2000-12-06"
    	response=requests.post(url=self.url,data=json.dumps(self.data))
    	self.data['expiration_date']="2022-12-06"
    	print(response.status_code)
    	print(response.text)
    	assert response.status_code==400


    def test_security_code(self):
    	self.data['security_code']=12312312
    	response=requests.post(url=self.url,data=json.dumps(self.data))
    	self.data['security_code']="123"
    	print(response.text)
    	assert  response.status_code==400



    def test_invalid_ammount(self):
    	self.data['amount']=0
    	response=requests.post(url=self.url,data=json.dumps(self.data))
    	self.data['amount']="1.2"
    	print(response.text)
    	assert  response.status_code==400

    @connection_check
    def test_blank_json(self):
    	data={}
    	response=requests.post(url=self.url,data=json.dumps(data))
    	
    	print(response.text)
    	assert  response.status_code==400









if __name__=="__main__":
	unittest.main()