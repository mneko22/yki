from flask import Flask, request
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

COLLECTION_NAME = "Motion"
CREDENTIAL_PATH = "ca-camp-rabbit-team-2019-12-firebase-adminsdk-pack4-ff94ef4b4f.json"

def get_motion_status():
    initialize_firestore(CREDENTIAL_PATH)
    docs = get_firestore(COLLECTION_NAME)
    for doc in docs:
        doc_dict = doc.to_dict()
        return "{} document is {}".format(doc.id, doc_dict.get("motion"))


def get_request_params(request):
    # TODO いらない？？？
    pass

def initialize_firestore(credential_path):
    cred = credentials.Certificate(credential_path) #TODO ダウンロードした秘密鍵
    firebase_admin.initialize_app(cred) 

def get_firestore(collection):
    db = firestore.client()
    docs = db.collection(collection).get()
    return docs

app = Flask(__name__)

@app.route("/knock", methods=['GET'])
def request_motion_status():
    return get_motion_status()


# for test 
# command
# python main.py 
if __name__ == "__main__":
    app.run(host='0.0.0.0', port='8080')