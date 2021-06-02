from aip import AipOcr
import glob
import cv2
import os

APP_ID = '23113753'
API_KEY = '4snbtok96Phcy6iif3VFsHUB'
SECRET_KEY = '7kUlpKkxIlEdeF0EkWQIDv0Hc6T5GUx7'

client = AipOcr(APP_ID, API_KEY, SECRET_KEY)

def ocr(id_list, input_dir, output_dir):
  try:
    for id in id_list:
      if os.path.exists('{}{}'.format(output_dir, id)):
        print('id: {} is already ocr'.format(id))
        continue
      path = input_dir + id
      frame_list = glob.glob(path + '/*') #获取当前文件夹下个数
      text_set = set()
      print('start ocr: {}'.format(id))
      for i in frame_list:
        img = open(i, mode='rb')
        data = client.basicAccurate(img.read())
        print("done one")
        for word in data['words_result']:
          text_set.add(word['words'])
      print('start save feature: {}'.format(id))
      file_handle=open('{}{}'.format(output_dir, id), mode='w')
      for word in text_set:
        file_handle.write(word + '\n')
  except Exception as e:
    print("ocr failed: {}".format(str(e)))
    return False
