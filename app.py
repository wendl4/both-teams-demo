from flask import Flask, render_template, request, jsonify
import random

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/pick', methods=['POST'])
def pick_clubs():
    data = request.json
    clubs = data.get("clubs", [])
    if len(clubs) < 2:
        return jsonify({"error": "Please provide at least 2 clubs."}), 400
    selected_clubs = random.sample(clubs, 2)
    return jsonify({"clubs": selected_clubs})

if __name__ == '__main__':
    app.run(debug=True)