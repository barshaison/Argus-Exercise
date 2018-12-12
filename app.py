from flask import Flask, request
import requests
import json
app = Flask(__name__)


@app.route('/', methods=['GET'])
def welcome():
   return 'Welcome to Argus exercise!   :) '


@app.route('/api/resource', methods=['GET'])
def read():
   try:
       f = open("msg.txt", "r")
       return f.read()
   except Exception as e:
       return "Request Failed: " + str(e)


@app.route('/write', methods=['POST'])
def write():
    try:
        content = request.json
        f = open("msg.txt", "w")
        f.write(str(content))

        return "Message was sent successfully!"
    except Exception as e:
        return "Failed to write message: " + str(e)


@app.route('/api/resource', methods=['POST'])
def trigger():
    try:
        content = request.json
        headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
        data = content
        r = requests.post("http://18.194.230.122:80/write",data=json.dumps(data),headers=headers)
        return "Request executed successfully!"
    except Exception as e:
        return "Request Failed: " + str(e)


if __name__ == '__main__':
   app.run(debug=True, host='0.0.0.0', port=80)
