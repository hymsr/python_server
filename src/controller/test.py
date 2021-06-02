from flask import Flask, request, jsonify, Blueprint
from utils import download
from .template import template
import threading
from utils.download import download
from utils.frame import extract
from utils.ocr import ocr
from utils.similar import caculate
from utils.request import post, get

test = Blueprint("test", __name__)

def working(url, openid):
  start = url.rindex('/')
  name = url[start+1:]
  download(url, './data/user/video', name)
  extract([name], './data/user/video/', './data/user/frame/')
  ocr([name], './data/user/frame/', './data/user/feature/')
  reslist = caculate(name)
  print(reslist)
  resid = '0'
  sim = 0
  for res in reslist:
    if res['sim'] > sim:
      sim = res['sim']
      resid = res['id']
  if sim > 0.1:
    print("result id is: {}".format(resid))
    rsp = get('/advertisement/{}'.format(resid), {})
    if rsp['ret'] == 0:
      req = {}
      ad = rsp['advertisement']
      req['keyword'] = ad['keyword']
      print("result keyword is {}".format(ad['keyword']))
      req['image'] = ad['url']
      print(req)
      result = post('/user/block/{}/{}'.format(str(openid), 20), req)
      print(result)


  

def dealwith(req):
  try:
    openid = req["openid"]
    url = req["url"]
    t = threading.Thread(target=working,args=(url, openid))
    t.setDaemon(True)
    t.start()
    return template("已加入处理队列", "")
  except Exception as e:
    return template("", e)

@test.route('/reg', methods=['POST'])
def getvideo():
  return dealwith(request.json)
