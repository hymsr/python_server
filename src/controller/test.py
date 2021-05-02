from flask import Flask, request, jsonify, Blueprint

test = Blueprint("test", __name__)

@test.route('/', methods=['POST'])
def hello_world():
  return jsonify(request.json)