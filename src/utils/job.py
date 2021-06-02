from datetime import datetime
from datetime import date
from apscheduler.schedulers.blocking import BlockingScheduler

from utils.download import download
from .request import get
from utils.frame import extract
from utils.ocr import ocr

testlist = ['8', '9', '7', '6', ]

def job():
    params = {}
    params['page_index'] = "1"
    params['page_size'] = "-1"
    print("start request server")
    rsp = get('/advertisement', params)
    id_list = []
    if rsp['ret'] == 0:
        for ad in rsp['advertisement']:
            if ad['url'] != None:
                download(ad['url'], './data/video', str(ad['id']))
                id_list.append(str(ad['id']))
    extract(id_list, "./data/video/", "./data/frame/")
    ocr(id_list, "./data/frame/", "./data/feature/")
                

def init():
    print("start init")
    job()
    # extract(testlist, "./data/video/", "./data/frame/")
    # ocr(testlist, "./data/frame/", "./data/feature/")