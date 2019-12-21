import json
import os
from flask import Flask, request, Response, jsonify
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

COLLECTION_NAME = "Motion"
CREDENTIAL_PATH = "ca-camp-rabbit-team-2019-12-firebase-adminsdk-pack4-ff94ef4b4f.json"
# SLACK_SIGNING_SECRET = os.environ['SLACK_SIGNING_SECRET']
# SLACK_OAUTH_ACCESS_TOKEN = os.environ['SLACK_OAUTH_ACCESS_TOKEN']
# SLACK_CHANNEL = os.environ['SLACK_CHANNEL']

cred = credentials.Certificate(CREDENTIAL_PATH)
firebase_admin.initialize_app(cred)

def verify_slack():
    data = request.data.decode('utf-8')
    data = json.loads(data)
    if 'challenge' in data:
        token = str(data['challenge'])
        return Response(token, mimetype='text/plane')

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
            ret_str += "{} is occupied.<br>".format(doc_id)
        else:
            ret_str += "{} is not occupied.<br>".format(doc_id)
    return ret_str

def response_to_slack(state_message):
    param = {
        'token': SLACK_OAUTH_ACCESS_TOKEN,
        'channels': SLACK_CHANNEL,
        'filename': 'cat.png',
        'title': 'cat'
    }

    requests.post(url=SLACK_UPLOAD_URL, params=param, files=files)

app = Flask(__name__)

@app.route("/knock", methods=['POST'])
def request_motion_status():
    data = request.data.decode('utf-8')
    data = json.loads(data)
    if 'challenge' in data:
        challenge = str(data['challenge'])
        ret_message = get_motion_status()
        return jsonify({"challenge": challenge, "message": ret_message}), 200




# for test 
# command
# python main.py 
if __name__ == "__main__":
    app.run(host='0.0.0.0', port='8080')