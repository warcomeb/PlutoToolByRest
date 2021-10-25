from flask import jsonify, request#, g, url_for, current_app
from flask_restx import Namespace, Resource, fields

from . import db

api = Namespace('payeestype', description='Payees Type related operations')

@api.route('/', methods=["POST", "GET"])
class Payee(Resource):
    #@api.marshal_with(cat)
    @api.doc('get_payeetype')
    @api.response(200, 'Payee Type found')
    @api.response(404, 'Payee Type not found')
    @api.param('id', 'The payee type identifier')
    @api.param('name', 'The payee type name')
    def get(self):
        query_parameters = request.args
        id_payee = query_parameters.get('id')
        name_payee = query_parameters.get('name')
        
        query = 'SELECT p.Id, p.Name FROM payeetype p '
        to_filter = []

        if (id_payee or name_payee):
            query += ' WHERE'
        
        if id_payee:
            query += ' p.Id=? AND'
            to_filter.append(id_payee)
        if name_payee:
            query += ' p.Name=*?* AND'
            to_filter.append(name_payee)

        if id_payee or name_payee:
            query = query[:-4] + ';'
        print(query)
        
        conn = db.get_db_connection()
        res = conn.execute(query,to_filter).fetchall()
        conn.close()

        payload = []
        content = {}
        if len(res) == 1:
            content = {
                        "id" : res[0][0],
                        "name": res[0][1]
                      }
            payload.append(content)
            return jsonify(payload)
        elif len(res) > 1:
            for result in res:
                content = {'id': result[0],
                           'name': result[1]}
                payload.append(content)
                content = {}

            return jsonify(payload)
        else:
            print('No element...')
            api.abort(404)

    @api.doc('post_payeetype')
    @api.response(200, 'New payee type added')
    @api.response(400, 'The add request is not well formed.')
    @api.response(404, 'The payee type is not found.')
    def post(self):
        if request.is_json:
            api.abort(400)
        else:
            api.abort(400)

