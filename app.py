from flask import Flask, render_template, jsonify


app = Flask(__name__)

PLAYERS = [{
  'id': 1,
  'Fname': 'Aaron',
  'Nname': 'Atomic Bomb',
  'B/T': 'R/R',
  'Spitch': 'Twice Tombstone',
  'TC': 'true'
}, {
  'id': 2,
  'Fname': 'Fred',
  'B/T': 'R/R',
  'TC': 'false'
}, {
  'id': 3,
  'Fname': 'Chris',
  'B/T': 'R/R',
  'Spitch': 'Boozer',
  'TC': 'true'
}]


@app.route("/")
def players():
  return render_template('home.html', players=PLAYERS)


@app.route("/api/players")
def list_players():
  return jsonify(PLAYERS)


if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
