import json
import os
from flask import Flask, request, Response, jsonify
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

COLLECTION_NAME = "Motion"
CREDENTIAL_PATH = "ca-camp-rabbit-team-2019-12-firebase-adminsdk-pack4-ff94ef4b4f.json"
cred = credentials.Certificate(CREDENTIAL_PATH)
firebase_admin.initialize_app(cred)
def get_motion_status():
    docs = get_firestore(COLLECTION_NAME)
    return get_message(docs)

def get_firestore(collection):
    db = firestore.client()
    docs = db.collection(collection).get()
    return docs

def get_message(docs):
    """Firestoreの結果からメッセージを生成
    
    Arguments:
        docs {operator} -- Firestoreからのget結果
    
    Returns:
        str -- メッセージ内容
    """
    ret_str = ""
    for doc in docs:
        doc_id = doc.id
        doc_dict = doc.to_dict()
        motion = doc_dict.get("motion")
        if motion:
            ret_str += "{} is occupied.\n".format(doc_id)
        else:
            ret_str += "{} is not occupied.\n".format(doc_id)
    return ret_str

app = Flask(__name__)

@app.route("/knock", methods=['POST'])
def request_motion_status():
    if request.headers['Content-Type'] != 'application/json':
        app.logger.debug(request.headers['Content-Type'])
        return jsonify(res='error'), 400

    # event apiの認証部分
    if request.json['type'] == 'url_verification':
        return jsonify({
            'status': 'OK',
            'data': request.json['challenge']
        }), 200

    if request.json['event']['type'] == 'message':
        text = request.json['event']['text']
        if text == "こんこん":
            ret_message = get_motion_status()
            return jsonify({
                'status': 'OK',
                'text': ret_message
            }), 200
        else:
            return jsonify({
                'status': 'OK',
                'text': "こんこんって聞いてね"
            }), 200



# for test 
# command
# python main.py 
if __name__ == "__main__":
    app.run(host='0.0.0.0', port='8080')