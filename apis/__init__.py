from flask_restx import Api

from .categories import api as categories


api = Api(
    title='PlutoTool by Rest',
    version='1.0',
    description='...',
    # All API metadatas
)

api.add_namespace(categories, path='/categories')

