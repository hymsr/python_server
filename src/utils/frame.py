
import cv2
import os
from skimage.metrics import structural_similarity

threshold = 0.7

def extract(id_list, input_dir, output_file):
  try:
    for vid in id_list:
      print('start extract: {}'.format(vid))
      vidcap = cv2.VideoCapture(input_dir + vid)
      if os.path.exists(output_file + vid):
        print("id:{} is already extract".format(vid))
        continue
      os.makedirs(output_file + vid)
      count = 0
      ratio = 0
      preimage = ""
      while(vidcap.isOpened()):
        ret, image = vidcap.read()
        if ret == False:
          break
        if ratio % 10 == 0:
          if preimage == "":
            cv2.imwrite(output_file + vid + "/frame%d.jpg" % count, image)
            count += 1
          else:
            (ssim, diff) = structural_similarity(preimage, image, full=True, multichannel=True)
            if ssim < threshold:
              cv2.imwrite(output_file + vid + "/frame%d.jpg" % count, image)
              count += 1
          preimage = image
        ratio += 1
      vidcap.release()
      print('finish extract: {}'.format(vid))
  except Exception as e:
    print("extract failed: {}".format(str(e)))
    return False


