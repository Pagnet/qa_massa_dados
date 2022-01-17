import json
from os import abort
from types import MethodType
from flask_restplus import Resource
from flask import request
from src.server.instance import server

from src.db.customer_repository import CustomerRepository
from src.models.customer_model import customer

app, api = server.app, server.api
ns = api.namespace('QA Automation', path='/api/v1/customer')


@ns.route('/')
class RouteCustomerPost(Resource):
    @api.expect(customer, valitade=True)
    def post(Self):
        try:
            payload = api.payload
            repo = CustomerRepository()
            query = repo.save(payload)
            return {"msg": "Sucesso!", "obj": payload}
        except Exception as e:
            return {"msg": "Falha ao adicionar item!", "insert": payload}

@ns.route('/<role>')
class RouteCustomerGetEmail(Resource):
    def get(self, role):
        try:
            repo = CustomerRepository()
            query = repo.selectByRole(role)
            return {"msg": "Sucesso!", "obj":query[0][0]}
        except Exception as e:
            return {"msg": "Falha ao realizar a consulta!", "error": '''"'''+ e +'''"'''}
