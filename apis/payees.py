from flask import jsonify, request#, g, url_for, current_app
from flask_restx import Namespace, Resource, fields

from . import db

api = Namespace('payees', description='Payees related operations')

@api.route('/', methods=["POST", "GET"])
class Payee(Resource):
    #@api.marshal_with(cat)
    @api.doc('get_subcategory')
    @api.response(200, 'Payee found')
    @api.response(404, 'Payee not found')
    @api.param('id', 'The payee identifier')
    @api.param('name', 'The payee name')
    @api.param('typeId', 'The payee type identifier')
    def get(self):
        query_parameters = request.args
        id_payee = query_parameters.get('id')
        id_payeetype = query_parameters.get('typeId')
        name_payee = query_parameters.get('name')
        
        query = 'SELECT p.Id, p.Name, t.Id, t.Name FROM payee p '
        query += 'INNER JOIN payeetype t ON t.Id = p.PayeeTypeId'
        to_filter = []

        if (id_payee or id_payeetype or name_payee):
            query += ' WHERE'
        
        if id_payee:
            query += ' p.Id=? AND'
            to_filter.append(id_payee)
        if id_payeetype:
            query += ' p.PayeeTypeId=? AND'
            to_filter.append(id_payeetype)
        if name_payee:
            query += ' p.Name=? AND'
            to_filter.append(name_payee)

        if (id_payee or id_payeetype or name_payee):
            query = query[:-4] + ';'
        print(query)
        
        conn = db.get_db_connection()
        res = conn.execute(query,to_filter).fetchall()
        conn.close()
      
        if len(res) == 1:
            payee = {
                        "id" : res[0][0],
                        "name": res[0][1],
                        "typeId": res[0][2],
                        "typeName" : res[0][3]
                      }
            return jsonify(payee)
        elif len(res) > 1:
            payload = []
            content = {}
            
            for result in res:
                content = {'id': result[0], 'name': result[1], 'typeId': result[2],  'typeName': result[3]}
                payload.append(content)
                content = {}

            return jsonify(payload)
        else:
            print('No element...')
            api.abort(404)

    @api.doc('post_payee')
    @api.response(200, 'New payee added')
    @api.response(400, 'The add request is not well formed.')
    @api.response(404, 'The payee type is not found.')
    def post(self):
        if (request.is_json):
            api.abort(400)
        else:
            api.abort(400)

