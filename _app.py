from flask import Flask, request, abort, render_template
app = Flask(__name__)


@app.get('/')
def hello_world():
    import core.db as db
    return 'Hello world!'


in_memory_datastore = {
    "COBOL": {"name": "COBOL", "publication_year": 1960, "contribution": "record data"},
    "ALGOL": {"name": "ALGOL", "publication_year": 1958, "contribution": "scoping and nested functions"},
    "APL": {"name": "APL", "publication_year": 1962, "contribution": "array processing"},
}

# Create, Read


@app.route('/programming_languages', methods=['GET', 'POST'])
def programming_languages_route():
    if request.method == 'GET':
        return list_programming_languages()
    elif request.method == "POST":
        return create_programming_language(request.get_json(force=True))


def list_programming_languages():
    return {"programming_languages": list(in_memory_datastore.values())}


def create_programming_language(new_lang):
    language_name = new_lang['name']
    in_memory_datastore[language_name] = new_lang
    return new_lang
# End Create, Read

# Read, Update, Delete


@app.route('/programming_languages/<language>', methods=['GET', 'PUT', 'DELETE'])
def programming_language_route(language):
    if request.method == 'GET':
        return get_programming_language(language)
    elif request.method == 'PUT':
        return update_programming_language(language, request.get_json(force=True))
    elif request.method == "DELETE":
        return delete_programming_language(language)


def get_programming_language(language):
    try:
        return in_memory_datastore[language]
    except:
        abort(404)


def update_programming_language(lang_name, new_lang_attributes):
    try:
        lang_getting_update = in_memory_datastore[lang_name]
    except:
        abort(404)
    finally:
        lang_getting_update.update(new_lang_attributes)
        return lang_getting_update


def delete_programming_language(lang_name):
    try:
        deleting_lang = in_memory_datastore[lang_name]
    except:
        abort(404)
    finally:
        del in_memory_datastore[lang_name]
        return deleting_lang
# End Read, Update, Delete


# @app.errorhandler(404)
# def page_not_found(e):
#     return render_template('404.html'), 404
