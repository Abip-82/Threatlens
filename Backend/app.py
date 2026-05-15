from flask import Flask, request, jsonify
from flask_cors import CORS 

app = Flask(__name__)
CORS(app)

@app.route('/analyze', methods=['POST'])
def analyze():
    data = request.get_json()
    url = data.get('url','')

    score = 0
    reasons =[]

    if len(url) > 70:
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
            reasons.append("Suspicious keywords detected")
    
    if '//' in url:
        score += 10
        reasons.append("common redirection trap detected, // in url.")
    
    score = min(score,100)
    if score<20:
        verdict = "safe"
    
    elif score < 50:
        verdict = "Suspicious. Possible phishing."
    
    else :
        verdict = "Dangerous"

    return jsonify({
        'url':url,
        'risk_score': score,
        'verdict': verdict,
        'reasons':reasons if reasons else ["No suspicious element detected"]
    })

if __name__ == '__main__':
    import os
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)