from flask import Flask, request
# get module
import get as getst
# update module

app = Flask(__name__)

@app.route("/", methods=['POST'])
def post_motion_status(request):
    return "post motion status"

@app.route("/", methods=['GET'])
def get_motion_status(request):
    return getst.get_motion_status()


# for test 
# command
# python main.py 
if __name__ == "__main__":
    app.run(host='0.0.0.0', port='8080')