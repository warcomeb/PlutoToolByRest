from flask import jsonify, request#, g, url_for, current_app
from flask_restx import Namespace, Resource, fields

from . import db

api = Namespace('subcategories', description='Sub-Categories related operations')

@api.route('/', methods=["POST", "GET"])
class SubCategory(Resource):
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

        #if not (id_scategory or name_scategory or id_category):
        #    api.abort(404)

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
    def post(self):
        if (request.is_json):
            data = request.get_json()
            name = data.get('name','')
            description = data.get('description','')
            categoryId = data.get('categoryId','')
        else:
            api.abort(400)

