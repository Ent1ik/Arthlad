from flask import Flask, request
app = Flask(__name__)

@app.route('/alice', methods = ['POST'])
def resp():
    text = request.json.get('request', {}).get('command')
    response_text = f"Assalamu aleykum"
    response = {
        'response' : {
            'text' : response_text,
            'end_session' : False,
            'intent' : 'response'
        },
        'version' : '1.0'
    }
    return response
