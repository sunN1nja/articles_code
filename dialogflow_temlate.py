from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def webhook():
    req = request.get_json(silent=True, force=True)
    action = req.get('queryResult').get('action')
    
    if action == 'your_action_name':
        response = {
            "fulfillmentText": "This is the response from your webhook!"
        }
    else:
        response = {
            "fulfillmentText": "Action not recognized."
        }
    
    return jsonify(response)

if __name__ == '__main__':
    app.run(port=5000)