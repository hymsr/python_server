import json

def template(res, error):
  rsp = {}
  if str(error) == "":
    rsp['msg'] = 'success: {}'.format(res)
    rsp['code'] = 0
    rsp['data'] = res
    return json.dumps(rsp, ensure_ascii=False)
  else:
    rsp['msg'] = 'error: {}'.format(str(error))
    rsp['code'] = -1
    return json.dumps(rsp, ensure_ascii=False)