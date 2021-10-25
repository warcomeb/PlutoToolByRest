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
        
        query = 'SELECT p.Id, p.Name, p.City, t.Id, t.Name FROM payee p '
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

        payload = []
        content = {}
        if len(res) == 1:
            content = {
                        "id" : res[0][0],
                        "name": res[0][1],
                        "city": res[0][2],
                        "typeId": res[0][3],
                        "typeName" : res[0][4]
                      }
            payload.append(content)
            return jsonify(payload)
        elif len(res) > 1:

            
            for result in res:
                content = {'id': result[0],
                           'name': result[1],
                           'city': result[2],
                           'typeId': result[3],
                           'typeName': result[4]}
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
        if request.is_json:
            data = request.get_json()
            name = data.get('name', '')
            type_id = data.get('typeId', '')
            email = data.get('email', '')
            phone = data.get('phone', '')
            address = data.get('address', '')
            city = data.get('city', '')
            district = data.get('district', '')
            zip_code = data.get('zipCode', '')
            country = data.get('country', '')
            VATID = data.get('VATID', '')
            NIN = data.get('NIN', '')
            note = data.get('note', '')

            if (type_id != None) and (type_id != ""):
                conn = db.get_db_connection()
                type_id_row = conn.execute('SELECT * FROM payeetype WHERE Id=?', [type_id]).fetchall()
                conn.close()
                if len(type_id_row) != 1:
                    api.abort(404)

            if (name != None) and (name != ""):
                query_string = "INSERT INTO payee (Id, Name, PayeeTypeId, Email, Phone, Address, City, District, ZipCode, Country, VATID, NIN, Active, Note) VALUES (NULL,?,"

                # Add payeetypeid
                query_string += type_id + ","

                if (email != None) & (email != ""):
                    query_string += email + ","
                else:
                    query_string += "NULL,"

                if (phone != None) & (phone != ""):
                    query_string += phone + ","
                else:
                    query_string += "NULL,"

                if (address != None) & (address != ""):
                    query_string += address + ","
                else:
                    query_string += "NULL,"

                if (city != None) & (city != ""):
                    query_string += city + ","
                else:
                    query_string += "NULL,"
    
                if (district != None) & (district != ""):
                    query_string += district + ","
                else:
                    query_string += "NULL,"

                if (zip_code != None) & (zip_code != ""):
                    query_string += zip_code + ","
                else:
                    query_string += "NULL,"

                if (country != None) & (country != ""):
                    query_string += country + ","
                else:
                    query_string += "NULL,"

                if (VATID != None) & (VATID != ""):
                    query_string += VATID + ","
                else:
                    query_string += "NULL,"

                if (NIN != None) & (NIN != ""):
                    query_string += NIN + ","
                else:
                    query_string += "NULL,"

                # The new payees is active!
                query_string += "1,"

                if (note != None) & (note != ""):
                    query_string += note
                else:
                    query_string += "NULL"

                query_string += ")"

                conn = db.get_db_connection()
                res = conn.execute(query_string, (name)).lastrowid

                conn.commit()
                conn.close()
                payee_return = {
                                "id": res,
                                "name": name,
                                "typeId": type_id
                               }
                #print(res)
                return jsonify(payee_return)
            else:
                api.abort(400)
        else:
            api.abort(400)

