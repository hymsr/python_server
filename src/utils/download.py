import sys, os
import urllib.request

def download(url_str, save_path, filename):
    try:
        full_path = save_path + '/' + filename
        if os.path.exists(full_path):
            print("{} is already exist".format(full_path))
            return True
        if not os.path.exists(save_path):
            os.makedirs(save_path)
        print("download start: {}".format(full_path))
        urllib.request.urlretrieve(url_str, full_path)
        print("download success")
        return full_path
    except Exception as e:
        print("download failed: {}".format(str(e)))
        return False