from flask import jsonify, request#, g, url_for, current_app
from flask_restx import Namespace, Resource, fields

from . import db

api = Namespace('payees', description='Payees related operations')

@api.route('/', methods=["POST", "GET"])
class Payee(Resource):
    #@api.marshal_with(cat)
    @api.doc('get_subcategory')
    @api.response(200, 'Subcategory found')
    @api.response(404, 'Subcategory not found')
    @api.param('id', 'The subcategory identifier')
    @api.param('name', 'The subcategory name')
    @api.param('categoryId', 'The parent category identifier')
    def get(self):
        query_parameters = request.args
        id_scategory = query_parameters.get('id')
        id_category = query_parameters.get('categoryId')
        name_scategory = query_parameters.get('name')
        
        query = 'SELECT s.Id, s.Name, s.Description, c.Id, c.Name FROM subcategory s '
        query += 'INNER JOIN category c ON c.Id = s.CategoryId'
        to_filter = []

        if (id_scategory or name_scategory or id_category):
            query += ' WHERE'
        
        if id_scategory:
            query += ' s.Id=? AND'
            to_filter.append(id_scategory)
        if name_scategory:
            query += ' s.Name=? AND'
            to_filter.append(name_scategory)
        if id_category:
            query += ' s.CategoryId=? AND'
            to_filter.append(id_category)

        if (id_scategory or name_scategory or id_category):
            query = query[:-4] + ';'
        print(query)
        
        conn = db.get_db_connection()
        res = conn.execute(query,to_filter).fetchall()
        conn.close()
      
        if len(res) == 1:
            subcategory = {
                        "id" : res[0][0],
                        "name": res[0][1],
                        "description": res[0][2],
                        "categoryId" : res[0][3],
                        "categoryName" : res[0][4]
                      }
            return jsonify(subcategory)
        elif len(res) > 1:
            payload = []
            content = {}
            
            for result in res:
                content = {'id': result[0], 'name': result[1], 'description': result[2],  'categoryId': result[3], 'categoryName': result[4]}
                payload.append(content)
                content = {}

            return jsonify(payload)
        else:
            print('No element...')
            api.abort(404)

    @api.doc('post_subcategory')
    @api.response(200, 'New subcategory added')
    @api.response(400, 'The add request is not well formed.')
    @api.response(404, 'The parent category is not found.')
    def post(self):
        if (request.is_json):
            data = request.get_json()
            name = data.get('name','')
            description = data.get('description','')
            categoryId = data.get('categoryId','')

            if (categoryId != None) & (categoryId != ""):
                conn = db.get_db_connection()
                category = conn.execute('SELECT * FROM category WHERE Id=?',[categoryId]).fetchall()
                conn.close()
                if len(category) != 1:
                    api.abort(404)
            else:
                api.abort(400)

            if ((name != None) & (description != None) & (name != "") & (description != "")):
                conn = db.get_db_connection()
                res = conn.execute("INSERT INTO subcategory (Id, Name, Description, CategoryId) VALUES (NULL, ?, ?, ?);",
                                (name,description,categoryId)
                                ).lastrowid
                conn.commit()
                conn.close()
                subcategory_return = {
                                    "id" : res,
                                    "name": name,
                                    "description": description,
                                    "categoryId": categoryId
                                  }
                return jsonify(subcategory_return)
            else:
                api.abort(400)
        else:
            api.abort(400)

