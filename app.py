from flask import Flask, render_template, request, session, jsonify
from flask_cors import CORS
import json
from mlconjug3 import Conjugator
import langSet
from flask_sqlalchemy import SQLAlchemy
import random
from flask_migrate import Migrate

app = Flask(__name__)
CORS(app)
CORS(app, origins="http://127.0.0.1:5173")

app.config['TEMPLATES_AUTO_RELOAD'] = True
app.config['JSON_AS_ASCII'] = False

# used to sign the session cookie and protect it from tampering
app.secret_key = "secret"

app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///data.sqlite3?charset=utf8'
#  data - name of a table
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False  # OPTIONAL

db = SQLAlchemy(app)
migrate = Migrate(app, db)


class users_db(db.Model):
    _id = db.Column("id", db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    email = db.Column(db.String(100))

    def __init__(self, name, email):
        self.name = name
        self.email = email


class italian_verbs_db(db.Model):
    _id = db.Column("id", db.Integer, primary_key=True)
    verb = db.Column(db.String(100))

    def __init__(self, verb):
        self.verb = verb


class spanish_verbs_db(db.Model):
    _id = db.Column("id", db.Integer, primary_key=True)
    verb = db.Column(db.String(100))

    def __init__(self, verb):
        self.verb = verb


class romanian_verbs_db(db.Model):
    _id = db.Column("id", db.Integer, primary_key=True)
    verb = db.Column(db.String(100))

    def __init__(self, verb):
        self.verb = verb


class french_verbs_db(db.Model):
    _id = db.Column("id", db.Integer, primary_key=True)
    verb = db.Column(db.String(100))

    def __init__(self, verb):
        self.verb = verb


class portuguese_verbs_db(db.Model):
    _id = db.Column("id", db.Integer, primary_key=True)
    verb = db.Column(db.String(100))

    def __init__(self, verb):
        self.verb = verb


@app.route('/delete/', methods=['GET', 'POST'])
def delete_data():
    db.session.query(spanish_verbs_db).delete()
    db.session.commit()


@app.route('/add_data/', methods=['GET', 'POST'])
def adding_data():
    with open("./italian_verbs.json", 'r', encoding="utf-8") as json_file:
        data = json.load(json_file)

    italian_verbs_list = data["verbs"]
    print(italian_verbs_list)

    for verb in italian_verbs_list:
        new_verb = italian_verbs_db(verb=verb)
        db.session.add(new_verb)

    db.session.commit()


@app.route('/check_db/', methods=['GET', 'POST'])
def check_table_contents():
    records = italian_verbs_db.query.all()

    # for record in records:
    #     print(record.id, record.verb)
    return render_template('db_data.html',
                           records=records)


@app.route('/pt/', methods=['GET', 'POST'])
def index_pt():
    pt = langSet.pt
    clearOutput = langSet.clarifyOutputPt

    if request.method == 'POST':
        verb = request.form['verb']
        conjugator = Conjugator(language='pt')
        conjugations = conjugator.conjugate(verb)

        # Pass the conjugations to the HTML template
        return render_template('portuguese_conjugations.html',
                               verb=verb,
                               conjugations=conjugations,
                               pt=pt,
                               clearOutput=clearOutput)

    return render_template('form.html',
                           pt=pt)


@app.route("/api/data/", methods=['GET', 'POST'])
def get_data():
    react_data = {"message": "Hello from Flask!"}
    return app.response_class(
        response=json.dumps(react_data),
        status=200,
        mimetype='application/json'
    )


@app.route('/es/', methods=['GET', 'POST'])
def index_es():
    es = langSet.es
    clearOutput = langSet.clarifyOutputEs

    if request.method == 'POST':
        verb = request.form['verb']
        conjugator = Conjugator(language='es')
        conjugations = conjugator.conjugate(verb)

        # Pass the conjugations to the HTML template
        return render_template('spanish_conjugations.html',
                               verb=verb,
                               conjugations=conjugations,
                               es=es,
                               clearOutput=clearOutput)

    return render_template('form.html')


@app.route('/fr/', methods=['GET', 'POST'])
def index_fr():
    fr = langSet.fr
    clearOutput_avoir = None
    clearOutput_etre = None
    no_verb_in_db = None

    if request.method == 'POST':
        verb = request.form['verb']

        with open('./data/etre_or_avoir.json') as json_file:
            data = json.load(json_file)

        if verb in data:
            conjugate_with = data[verb]
            if conjugate_with == "Avoir":
                clearOutput_avoir = langSet.clarify_output_fr_avoir
            elif conjugate_with == "Être":
                clearOutput_etre = langSet.clarify_output_it_etre
            elif conjugate_with == "both":
                conjugate_with = ("Avoir", "Être")
                clearOutput_etre, clearOutput_avoir = langSet.clarify_output_fr_etre, langSet.clarify_output_fr_avoir
        else:
            conjugate_with = ("Avoir", "Être")
            clearOutput_etre, clearOutput_avoir = langSet.clarify_output_fr_etre, langSet.clarify_output_fr_avoir
            no_verb_in_db = "Sorry, we don't have this verb in our database. Conjugations are made using both auxiliaries."

        conjugator = Conjugator(language='fr')
        conjugations = conjugator.conjugate(verb)

        # Pass the conjugations to the HTML template
        return render_template('french_conjugations.html',
                               verb=verb,
                               conjugate_with=conjugate_with,
                               conjugations=conjugations,
                               fr=fr,
                               clearOutput=clearOutput_avoir if clearOutput_avoir else clearOutput_etre,
                               clearOutput_avoir=clearOutput_avoir if clearOutput_avoir else None,
                               clearOutput_etre=clearOutput_etre if clearOutput_etre else None,
                               no_verb_in_db=no_verb_in_db if no_verb_in_db else None)

    return render_template('form.html')


@app.route('/it/', methods=['GET', 'POST'])
def index_it():
    it = langSet.it
    clearOutput_avere = None
    clearOutput_essere = None
    no_verb_in_db = None

    if request.method == 'POST':
        verb = request.form['verb']

        with open('./data/essere_or_avere.json') as json_file:
            data = json.load(json_file)

        if verb in data:
            conjugate_with = data[verb]
            if conjugate_with == "avere":
                clearOutput_avere = langSet.clarify_output_it_avere
            elif conjugate_with == "essere":
                clearOutput_essere = langSet.clarify_output_it_essere
            elif conjugate_with == "both":
                conjugate_with = ("avere", "essere")
                clearOutput_essere, clearOutput_avere = langSet.clarify_output_it_essere, langSet.clarify_output_it_avere
        else:
            conjugate_with = ("avere", "essere")
            clearOutput_essere, clearOutput_avere = langSet.clarify_output_it_essere, langSet.clarify_output_it_avere
            no_verb_in_db = "Sorry, we don't have this verb in our database. Conjugations are made using both auxiliaries."

        conjugator = Conjugator(language='it')
        conjugations = conjugator.conjugate(verb)

        # Pass the conjugations to the HTML template
        return render_template('italian_conjugations.html',
                               verb=verb,
                               conjugate_with=conjugate_with,
                               conjugations=conjugations,
                               it=it,
                               clearOutput=clearOutput_avere if clearOutput_avere else clearOutput_essere,
                               clearOutput_avere=clearOutput_avere if clearOutput_avere else None,
                               clearOutput_essere=clearOutput_essere if clearOutput_essere else None,
                               no_verb_in_db=no_verb_in_db if no_verb_in_db else None)

    return render_template('form.html',
                           it=it)


@app.route('/it/search/', methods=['GET'])
def search_it():
    if (request.method == 'GET'):
        query = request.args.get('query')
        if len(query) >= 3:
            results = perform_search(str(query), './data/essere_or_avere.json')
        else:
            results = []

        return app.response_class(
            response=json.dumps(results),
            status=200,
            mimetype='application/json'
        )


def perform_search(query, file_path):
    # './data/essere_or_avere.json'
    with open(file_path) as json_file:
        data = json.load(json_file)
    results = [result for result in data if result.startswith(query)]

    return results


@app.route('/ro/', methods=['GET', 'POST'])
def index_ro():
    ro = langSet.ro
    clearOutput = langSet.clarify_output_ro

    if request.method == 'POST':
        verb = request.form['verb']
        conjugator = Conjugator(language='ro')
        conjugations = conjugator.conjugate(verb)

        # Pass the conjugations to the HTML template
        return render_template('romanian_conjugations.html',
                               verb=verb,
                               conjugations=conjugations,
                               ro=ro,
                               clearOutput=clearOutput)

    return render_template('form.html')


@app.route('/login/', methods=['GET', 'POST'])
def login():
    if request.method == "POST":
        session.permanent = True
        email = request.form["email"]
        session["user"] = email

        return render_template('login.html',
                               email=email)

    return render_template('login.html')


@app.route('/<string:language>/<string:mood>_<string:tense>_for_<int:lvl_nr>/', methods=['GET'])
def enter_validator(language, mood, tense, lvl_nr):
    if request.method == "GET":
        # lvl_nr = request.form.get('data-lvl')
        end_verb = lvl_nr * 25 + 1   # 25
        start_verb = end_verb - 25   # 1
        verb_sequence = []
        tense = tense
        mood = mood

        for verb in range(start_verb, end_verb):
            verb_sequence.append(verb)
        random.shuffle(verb_sequence)

        # first_verb = italian_verbs_db.query.filter_by(_id=start_verb).first()

        return render_template('validator.html',
                               verb_sequence=verb_sequence,
                               lvl_nr=lvl_nr,
                               tense=tense,
                               mood=mood,
                               language=language)
        # first_verb=first_verb if first_verb else None)

    return render_template("validator.html")


@app.route('/<string:language>/next_verb:_<int:verb_id>/', methods=['GET'])
def next_verb(language, verb_id):
    # verb_id = request.json['verb_id']

    if language == "it":
        database = italian_verbs_db
    elif language == "pt":
        database = portuguese_verbs_db
    elif language == "es":
        database = spanish_verbs_db
    elif language == "ro":
        database = romanian_verbs_db
    elif language == "fr":
        database = french_verbs_db

    if (request.method == 'GET'):
        next_verb = database.query.filter_by(_id=verb_id).first()
        # verb_sequence = verb_sequence[:1]
        print(next_verb)

        # conjugation function
        # conjugator = Conjugator(language=language)
        # conjugations = conjugator.conjugate(next_verb)
        # conjugation function

        return app.response_class(
            response=json.dumps(next_verb.verb),
            status=200,
            mimetype='application/json'
        )


if __name__ == "__main__":
    db.create_all()
    app.run(debug=True)
