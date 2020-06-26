from flask import Flask, jsonify

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False

user = {
    "name": "Maks",
    "age": 21
}

@app.route("/")
@app.route("/index")
def main_page():
    return jsonify(user)

app.run()