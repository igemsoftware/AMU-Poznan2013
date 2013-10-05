"""
Module handling pri-miRNA objects
"""
import urllib2
import json

HOST = 'http://150.254.78.155:5000/'
URL_ALL = HOST + 'database/get_all'
URL_BY_NAME = HOST + 'database/get_by_name'
URL_BY_MIRNA_S = HOST + 'database/get_by_mirna_s'

HEADERS = {'content-type': 'application/json'}


class Backbone:
    """pri-miRNA class"""
    def __init__(self, name, flanks3_s, flanks3_a, flanks5_s, flanks5_a,
                 loop_s, loop_a, miRNA_s, miRNA_a, miRNA_length, miRNA_min,
                 miRNA_max, miRNA_end_5, miRNA_end_3, structure, homogeneity,
                 miRBase_link):
        self.name = name
        self.flanks3_s = flanks3_s
        self.flanks3_a = flanks3_a
        self.flanks5_s = flanks5_s
        self.flanks5_a = flanks5_a
        self.loop_s = loop_s
        self.loop_a = loop_a
        self.miRNA_s = miRNA_s
        self.miRNA_a = miRNA_a
        self.miRNA_length = miRNA_length
        self.miRNA_min = miRNA_min
        self.miRNA_max = miRNA_max
        self.miRNA_end_5 = miRNA_end_5
        self.miRNA_end_3 = miRNA_end_3
        self.structure = structure
        self.homogeneity = homogeneity
        self.miRBase_link = miRBase_link

    def serialize(self):
        """Makes dictionary of object variables"""
        return {
            'name': self.name,
            'flanks3_s': self.flanks3_s,
            'flanks3_a': self.flanks3_a,
            'flanks5_s': self.flanks5_s,
            'flanks5_a': self.flanks5_a,
            'loop_s': self.loop_s,
            'loop_a': self.loop_a,
            'miRNA_s': self.miRNA_s,
            'miRNA_a': self.miRNA_a,
            'miRNA_length': self.miRNA_length,
            'miRNA_min': self.miRNA_min,
            'miRNA_max': self.miRNA_max,
            'miRNA_end_5': self.miRNA_end_5,
            'miRNA_end_3': self.miRNA_end_3,
            'structure': self.structure,
            'homogeneity': self.homogeneity,
            'miRBase_link': self.miRBase_link
        }

    def template(self, siRNAstrand_1, siRNAstrand_2):
        """Returns the template of DNA (sh-miR)"""
        return (self.flanks5_s + siRNAstrand_1 + self.loop_s +\
            siRNAstrand_2 + self.flanks3_s).upper()


def qbackbone(data=None, url=None):
    """Interface to query on database.
    Returns serialized json data"""

    json_data = {}
    if data:
        json_data.update({"data": data})
    req = urllib2.Request(url, json.dumps(json_data), headers=HEADERS)
    try:
        return json.loads(urllib2.urlopen(req).read())
    except urllib2.URLError:
        return {'error': 'Connection to database refused.'}


def get_all(data=None):
    """Takes all objects from database"""
    return qbackbone(data=data, url=URL_ALL)


def get_by_name(data=None):
    """Takes object from database depending on the given name"""
    return qbackbone(data=data, url=URL_BY_NAME)


def get_by_mirna_s(data=None):
    """Takes object from database depending on the sequence of miRNA_s"""
    return qbackbone(data=data, url=URL_BY_MIRNA_S)
