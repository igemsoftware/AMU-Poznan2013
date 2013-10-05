"""
Handlers to communicate with database
"""

from . import database
from decorators import require_json
from flask.json import dumps

@require_json(require_data=False)
def get_all(**kwargs):
    """
    Gets all data from database
    """
    return dumps(database.get_all())


@require_json(required_data_words=1)
def get_by_name(data=None, **kwargs):
    """
    Searching by name in a case-insensitive way
    """
    return dumps(database.get_by_name(data))


@require_json(required_data_characters=2)
def get_by_miRNA_s(data=None, **kwargs):
    """
    Searching by first two nucleotides of endogenous miRNA
    """
    return dumps(database.get_by_miRNA_s(data))


get_all.methods = ['POST']
get_by_name.methods = ['POST']
get_by_miRNA_s.methods = ['POST']
