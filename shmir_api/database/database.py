"""
Module for communication with database
"""

import psycopg2
from flask import g
try:
    from settings import DB_NAME, DB_USER, DB_PASS, DB_HOST, DB_PORT
except ImportError:
    print('Create settings.py')

def get_db():
    """
    Global connector variable
    """
    db = getattr(g, '_database', None)
    if db is None:
        db = psycopg2.connect(database=DB_NAME, user=DB_USER,
                              password=DB_PASS, host=DB_HOST, port=DB_PORT)
    return db


def disconnect():
    """
    Global disconnector
    """
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()


def execute_with_one_response(query, var=None):
    """
    Executes query and returns only first response
    """
    with get_db().cursor() as cur:
        cur.execute(query, var)
        data = cur.fetchone()
    return data


def execute_with_response(query, var=None):
    """
    Executes query and returns all responses
    """
    with get_db().cursor() as cur:
        cur.execute(query, var)
        data = cur.fetchall()
        cur.close()
    return data

def get_multirow_by_query(query, var=None):
    """
    Returns serialized data from database
    """
    data = execute_with_response(query, var)
    backbones = []
    for row in data:
        backbones.append(serialize(*row))
    return backbones


def add(name, flanks3_s, flanks3_a, flanks5_s, flanks5_a, loop_s, loop_a,
        miRNA_s, mirRNA_a, miRNA_length, miRNA_min, miRNA_max, miRNA_end_5,
        miRNA_end_3, structure, homogeneity, miRBase_link):
    """
    Function which adds another flank to database without closing server
    """

    query = ("INSERT INTO backbone VALUES(DEFAULT, %s, %s, %s, %s, %s, %s, %s,"
             " %s, %s, %d, %d, %d, %s, %d, %s);")

    var = (name, flanks3_s, flanks3_a, flanks5_s, flanks5_a, loop_s, loop_a,
           miRNA_s, mirRNA_a, miRNA_length, miRNA_min, miRNA_max, miRNA_end_5,
           miRNA_end_3, structure, homogeneity, miRBase_link)

    execute(query, var)


def get_by_name(name):
    """
    Function which gets one serialized Backbone by name
    """
    query = ("SELECT name, flanks3_s, flanks3_a, flanks5_s, flanks5_a, loop_s,"
             " loop_a, miRNA_s, miRNA_a, miRNA_length, miRNA_min, miRNA_max, "
             "miRNA_end_5, miRNA_end_3, structure, homogeneity, miRBase_link "
             "FROM backbone WHERE LOWER(name) = LOWER(%s);")

    data = execute_with_one_response(query, (name,))

    return serialize(*data) if data else {}


def get_all():
    """
    Function which gets all serialized Backbones in database
    """
    query = ("SELECT name, flanks3_s, flanks3_a, flanks5_s, flanks5_a, loop_s,"
             " loop_a, miRNA_s, miRNA_a, miRNA_length, miRNA_min, miRNA_max, "
             "miRNA_end_5, miRNA_end_3, structure, homogeneity, miRBase_link "
             "FROM backbone;")

    return get_multirow_by_query(query)


def get_by_miRNA_s(letters):
    """
    Function which gets serialized Backbones by first two letters of miRNA_s
    """
    query = ("SELECT name, flanks3_s, flanks3_a, flanks5_s, flanks5_a, loop_s,"
             " loop_a, miRNA_s, miRNA_a, miRNA_length, miRNA_min, miRNA_max, "
             "miRNA_end_5, miRNA_end_3, structure, homogeneity, miRBase_link "
             "FROM backbone WHERE miRNA_s LIKE %s;")

    return get_multirow_by_query(query, (letters.upper() + "%",))


def serialize(name, flanks3_s, flanks3_a, flanks5_s, flanks5_a, loop_s,
              loop_a, miRNA_s, miRNA_a, miRNA_length, miRNA_min, miRNA_max,
              miRNA_end_5, miRNA_end_3, structure, homogeneity, miRBase_link):
    """
    Function which serialize data from database to dictionary
    """
    return {
        'name': name,
        'flanks3_s': flanks3_s,
        'flanks3_a': flanks3_a,
        'flanks5_s': flanks5_s,
        'flanks5_a': flanks5_a,
        'loop_s': loop_s,
        'loop_a': loop_a,
        'miRNA_s': miRNA_s,
        'miRNA_a': miRNA_a,
        'miRNA_length': miRNA_length,
        'miRNA_min': miRNA_min,
        'miRNA_max': miRNA_max,
        'miRNA_end_5': miRNA_end_5,
        'miRNA_end_3': miRNA_end_3,
        'structure': structure,
        'homogeneity': homogeneity,
        'miRBase_link': miRBase_link
    }
