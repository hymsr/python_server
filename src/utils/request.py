import json
import requests
baseUrl = 'http://localhost:8080'

def post(url, data):
  headers = {"Content-Type": "application/json"}
  rsp = requests.post(baseUrl + url, headers=headers, data=json.dumps(data))
  rsp.encoding = 'utf-8'
  return rsp.json()

def get(url, params): 
  rsp = requests.get(baseUrl + url, params=params)
  rsp.encoding = 'utf-8'
  return rsp.json()
