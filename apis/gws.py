from flask_restx import Namespace, Resource, fields
# import core.db as db
# import core.helpers as helpers

api = Namespace('gws', description='GWS related operations')

# gws = api.model('GWS', {
#     'id': fields.String(required=True, description='The cat identifier'),
#     'name': fields.String(required=True, description='The cat name'),
# })

# GWS = [
#     {'id': '123', 'name': 'Felix'},
# ]


# cnx = db.get_db()


@api.route('/hello')
class HelloWorld(Resource):
    def get(self):
        return {'hello': 'get world'}

    def post(self):
        return {'hello': 'post world'}


# def gws_home():
#     return "Hello GWS!"


@api.route('/suppliers', methods=['GET'])
class Suppliers(Resource):
    def get(self):
        return helpers.rowsToJSON(cnx, "SELECT * FROM hp_suppliers WHERE active = 1")


# @api.route('/cycle/<race_date>/<track_code>/<race_num>', methods=['GET'])
# def gws_cycles(race_date=None, track_code=None, race_num=0):
#     sql = """SELECT TOP 10 * FROM gws_tracks t JOIN gws_files f ON t.track_id = f.track_id
#             WHERE file_type_id = 3
#             AND race_date = ?
#             AND track_code = ?
#             AND race = ?"""
#     cur = db.cursor()
#     cur.execute(sql, race_date, track_code, race_num)
#     r = [dict((cur.description[i][0], value)
#               for i, value in enumerate(row)) for row in cur.fetchall()]
#     cur.connection.close()
#     return r

    # return sql
    # return rowsToJSON(db, sql, [race_date, track_code, race_num])
