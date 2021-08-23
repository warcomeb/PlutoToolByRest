from flask import Flask
#from flask_restx import Resource, Api
from apis import api

app = Flask(__name__)
api.init_app(app)

#@api.route('/hello')
#class HelloWorld(Resource):
#    def get(self):
#        return {'hello': 'world'}

#@api.route('/payee')
#class Payee(Resource):
#    def get(self):
#        query_parameters = request.args
#        id = query_parameters.get('id')
#        return{'id':id}


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)