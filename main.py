from flask import Flask, request, jsonify

app = Flask(name)

@app.route('/alice', methods=['POST'])
def resp():
    request_data = request.json.get('request', {})
    command = request_data.get('command', '')

    response_text = "Assalamu aleykum"

    response = {
        'response': {
            'text': response_text,
            'end_session': False
        },
        'session': request_data.get('session', {}),
        'version': '1.0'
    }

    return jsonify(response)

if name == 'main':
    app.run(debug=True)
