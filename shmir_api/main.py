#!/usr/bin/env python3.3
"""
Flask server which provide RESTful api for database and mfold
"""


DEBUG = True


from flask import Flask

from database.database import disconnect
import database.handlers
import mfold.handlers


app = Flask(__name__)


@app.teardown_appcontext
def close_connection(exception):
    disconnect()


app.add_url_rule('/database/get_all', 'database.get_all',
                 database.handlers.get_all)
app.add_url_rule('/database/get_by_name', 'database.get_by_name',
                 database.handlers.get_by_name)
app.add_url_rule('/database/get_by_mirna_s', 'database.get_by_miRNA_s',
                 database.handlers.get_by_miRNA_s)
app.add_url_rule('/mfold', 'mfold', mfold.handlers.get_mfold)


if __name__ == '__main__':
    app.run()
