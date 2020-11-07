# imports
import qna
import knowbase
from flask import Flask, request, jsonify
from flask_cors import CORS

# app setup
app = Flask(__name__)
CORS(app, support_credentials=True)

# endpoints
# default endpoint
@app.route('/', methods=['GET'])
def default_endpoint():
    res = jsonify({
        "success": True
    })
    return res

# post a question | respond with answer
@app.route('/answer/ask', methods=['POST'])
def question():
    try:    
        req = request.json
        ans = qna.ask(req['question'])
        return jsonify({
            'success': True,
            'answer': ans
        })
    except:
        return jsonify({
            'success': False,
        })

# post a question | respond with top 3 matches
@app.route('/answer/search', methods=['POST'])
def search_ans():
    try:
        req = request.json
        results = qna.search(req['question'])
        return jsonify({
            'success': True,
            'answer': results
        })
    except:
        return jsonify({
            'success': False,
        })

# post a qna | add a new qna to kb
@app.route('/kb/new', methods=['POST'])
def new_qna():
    req = request.json
    msg = knowbase.addNewQNA(req['question'], req['answer'])
    return jsonify({
        'success': msg,
    })

# post a question and id | add a new question
@app.route('/kb/update', methods=['POST'])
def update_qna():
    req = request.json
    msg = knowbase.updateQNA(req['qid'], req['question'])
    return jsonify({
        'success': msg
    })

# main
if __name__ == "__main__":
    app.run(debug=True)