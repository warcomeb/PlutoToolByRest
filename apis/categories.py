from flask import jsonify, request#, g, url_for, current_app
from flask_restx import Namespace, Resource, fields

from . import db

api = Namespace('categories', description='Categories related operations')

@api.route('/list')
class CategoriesList(Resource):
    @api.doc('list_categories')
    #@api.description('List of all categories present in the database')
    #@api.marshal_list_with(cat)
    def get(self):
        conn = db.get_db_connection()
        categories = conn.execute('SELECT * FROM category').fetchall()
        conn.close()
        payload = []
        content = {}
        for result in categories:
            content = {'id': result[0], 'name': result[1], 'desciption': result[2]}
            payload.append(content)
            content = {}
        return jsonify(payload)

@api.route('/', methods=["POST", "GET"])
class Category(Resource):
    #@api.marshal_with(cat)
    @api.doc('get_category')
    @api.response(200, 'Category found')
    @api.response(404, 'Category not found')
    @api.param('id', 'The category identifier')
    @api.param('name', 'The category name')
    def get(self):
        query_parameters = request.args
        id_category = query_parameters.get('id')
        name_category = query_parameters.get('name')
        
        query = "SELECT * FROM category WHERE"
        to_filter = []
        
        if id_category:
            query += ' Id=? AND'
            to_filter.append(id_category)
        if name_category:
            query += ' Name=? AND'
            to_filter.append(name_category)

        if not (id_category or name_category):
            api.abort(404)

        query = query[:-4] + ';'
        print(query)
        conn = db.get_db_connection()
        res = conn.execute(query,to_filter).fetchall()
        if len(res) == 1:
            category = {
                        "id" : res[0][0],
                        "name": res[0][1],
                        "description": res[0][2]
                      }
            return jsonify(category)
        elif len(res) == 0:
            print('No elements...')
            api.abort(404)
        else:
            print('To many elements...')
            api.abort(404)
        
    @api.doc('post_category')
    @api.response(200, 'New category added')
    @api.response(400, 'The add request is not well formed.')
    #@api.description("Add new category")
    def post(self):
        if (request.is_json):
            data = request.get_json()
            name = data.get('name','')
            description = data.get('description','')
            if ((name != None) & (description != None) & (name != "") & (description != "")):
                conn = db.get_db_connection()
                res = conn.execute("INSERT INTO category (Id, Name, Description) VALUES (NULL, ?, ?);",
                                (name,description)
                                ).lastrowid
                conn.commit()
                conn.close()
                category_return = {
                                    "id" : res,
                                    "name": name,
                                    "description": description
                                  }
                #print(res)
                #data.to_json().append("id",res)
                return jsonify(category_return)
            else:
                api.abort(400)
        else:
            api.abort(400)
