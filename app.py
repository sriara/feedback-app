from flask import Flask, request, jsonify, render_template
import json

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    data = request.get_json()
    entry = {
        "name": data['name'],
        "feedback": data['feedback']
    }
    with open('feedback.json', 'a') as f:
        f.write(json.dumps(entry) + '\n')
    return jsonify({"message": "Feedback submitted successfully!"})

if __name__ == '__main__':
    app.run(debug=True)
