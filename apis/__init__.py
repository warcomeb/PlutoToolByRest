from flask_restx import Api

from .categories import api as categories
from .subcategories import api as subcategories
from .payees import api as payees
from .payeestype import api as payeestype


api = Api(
    title='PlutoTool by Rest',
    version='1.0',
    description='...',
    # All API metadatas
)

api.add_namespace(categories, path='/categories')
api.add_namespace(subcategories, path='/subcategories')
api.add_namespace(payees, path='/payees')
api.add_namespace(payeestype, path='/payeestype')

