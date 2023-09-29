

def rowsToJSON(cnxn, query, args=(), one=False):
    cur = cnxn.cursor()
    cur.execute(query, args[0], args[1], args[2])
    r = [dict((cur.description[i][0], value)
              for i, value in enumerate(row)) for row in cur.fetchall()]
    # cur.connection.close()
    return (r[0] if r else None) if one else r


