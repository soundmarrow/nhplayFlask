import pyodbc
from flask import current_app, g
# from flask import g

# Some other example server values are
# server = 'localhost\sqlexpress' # for a named instance
# server = 'myserver,port' # to specify an alternate port
# server = 'tcp:nhsql2.mountainmedia.com'
# database = 'nhplay_production'
# username = 'cfsvcuser'
# password = 'HapBbJPCE6kpDkCUmnVp'

server = 'tcp:10.5.0.5'
database = 'nhplay_staging'
username = 'cfsvcuser'
password = 'sanguineLuck73'


def get_db():
    if 'db' not in g:
        g.db = pyodbc.connect('DRIVER={ODBC Driver 18 for SQL Server};SERVER='+server +
                              ';DATABASE='+database+';ENCRYPT=yes;UID='+username+';PWD=' + password + ';TrustServerCertificate=yes')
        # g.db.row_factory = sqlite3.Row
    return g.db


def close_db(e=None):
    db = g.pop('db', None)
    if db is not None:
        db.close()


def init_app(app):
    app.teardown_appcontext(close_db)
    get_db()
    # app.cli.add_command(init_db_command)


# def init_app():
#     get_db()
    # ENCRYPT defaults to yes starting in ODBC Driver 18. It's good to always specify ENCRYPT=yes on the client side to avoid MITM attacks.
    # cnxn = pyodbc.connect('DRIVER={ODBC Driver 18 for SQL Server};SERVER='+server +
    #                       ';DATABASE='+database+';ENCRYPT=yes;UID='+username+';PWD=' + password + ';TrustServerCertificate=yes')


# cursor = cnxn.cursor()

# cursor.execute("SELECT TOP(100) * FROM hp_suppliers")
# row = cursor.fetchone()
# print(row)
# while row:
#     print(row[0])
#     row = cursor.fetchone()

# cnxn.close()

# isql -v -k "DRIVER={ODBC Driver 18 for SQL Server};SERVER=10.5.0.5;DATABASE=nhplay_staging;ENCRYPT=yes;UID=cfsvcuser;PWD=sanguineLuck73;TrustServerCertificate=yes"
