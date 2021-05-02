from flask import Flask, request, jsonify
import json
app = Flask(__name__)

@app.route('/', methods=['POST'])
def hello_world():
  return jsonify(request.json)