"""
Utilies for handling json
"""

from flask import jsonify

def json_error(error):
    """Input: string
    Output: dictionary"""
    return jsonify(error=error)
