from flask import Flask, request, jsonify
from flask_cors import CORS 

app = Flask(__name__)
CORS(app)

def check_url_safety(url):
    score = 0
    reasons =[]

    if len(url) > 50:
        score += 15
        reasons.append("URL is suspiciously long.")

    if url.count('.') > 3:
        score += 20
        reasons.append("Too many dots. Url is suspicious")

    if '@' in url:
        score += 20
        reasons.append("@ in url. It is uncommon in real urls and commonly used in phishing sites")

    sus_words = ['login', "bank" , "confirm", "quick" ,"safe", "purchase" , "secure", "paypa1" , "verify", "update" , "winner" , "lucky"]
    for word in sus_words:
        if word in url.lower():
            score +=10
            reasons.append("Suspicious keywords detected" + ":" + word)
    
    if '-' in url:
        score += 10
        reasons.append("Dash in url. Often used to mimic real brands.")
    
    if url.startswith("http://"):
        score += 20
        reasons.append("Unsecure protocol. Legit sites use https.")

    score = min(score,100)
    if score<10:
        verdict = "safe"
    
    elif score < 50:
        verdict = "Suspicious. Possible phishing."
    
    else :
        verdict = "Dangerous"

    return {
        'url':url,
        'risk_score': score,
        'verdict': verdict,
        'reasons':reasons if reasons else ["No suspicious element detected"]
    }
@app.route('/analyze', methods=['POST'])
def analyze():
    data = request.get_json()
    url = data.get('url','')
    result = check_url_safety(url)
    return jsonify(result)

if __name__ == '__main__':
    import os
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)