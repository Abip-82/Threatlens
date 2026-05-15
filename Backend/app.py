from flask import Flask, request, jsonify
from flask_cors import CORS 

app = Flask(__name__)
CORS(app)

@app.route('/analyze', methods=['POST'])
def analyze():
    data = request.get_json()
    url = data.get('url','')

    jsonify({
        'url':url,
        'risk_score':42,
        'reason':'Placeholder: Real detailed analysis coming soon.'
    })

if __name__ == '__main__':
    app.run(debug=True)