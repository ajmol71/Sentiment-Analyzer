from flask import Flask, request, jsonify
from flask_cors import CORS
import time

app = Flask(__name__)
CORS(app)

@app.route('/get_sentiment', methods=['POST'])
def get_sentiment():
    data = request.get_json()
    text = data.get('text')
    
    # process the text and return sentiment
    time.sleep(2)
    
    return jsonify({'message': f'Text received: {text}'})

if __name__ == '__main__':
    app.run(debug=True)