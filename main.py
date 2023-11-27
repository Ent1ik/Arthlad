from flask import Flask, request
app = Flask(name)

@app.route('/alice', methods = ['POST'])
def resp():
    text = request.json.get('request', {}).get('command')
    response_text = f"Привет, {text}! Как дела?"
    response = {
        'response' : {
            'text' : response_text,
            'end_session' : False
        },
        'version' : '2.0'
    }
    return response
