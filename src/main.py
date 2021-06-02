from flask import Flask, request, jsonify
from controller.test import test
from utils.job import init
import json
app = Flask(__name__)
# 注册模块
app.register_blueprint(test, url_prefix='/test')
init()