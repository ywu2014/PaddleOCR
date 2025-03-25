from paddleocr import PaddleOCR, draw_ocr
from utils import drawBoxes, draw_ocr_seq
import cv2
import matplotlib.pyplot as plt

# Paddleocr supports Chinese, English, French, German, Korean and Japanese
# You can set the parameter `lang` as `ch`, `en`, `french`, `german`, `korean`, `japan`
# to switch the language model in order
rec_model_dir='./output/ch_PP-OCRv4_rec/best_model/model'
det_model_dir='./output/ch_PP-OCRv4_det/latest'
ocr = PaddleOCR(use_angle_cls=True, rec_model_dir=rec_model_dir, det_model_dir=det_model_dir) 
out_dir = './inference/out'
img_dir = './inference/data'

img_name = 'feature1.jpg'
img_path = f'{img_dir}/{img_name}'
out_path = f'{out_dir}/{img_name}'
result = ocr.ocr(img_path, cls=True)
for idx in range(len(result)):
    res = result[idx]
    for line in res:
        print(line)

# draw result
result = result[0]
boxes = [line[0] for line in result]
txts = [line[1][0] for line in result]
scores = [line[1][1] for line in result]

# 画的很模糊
# from PIL import Image
# image = Image.open(img_path).convert('RGB')
# im_show = draw_ocr(image, boxes, txts, scores, font_path='/home/linkedata/projects/ai/MultiModal/ocr/data/font/simfang.ttf')
# im_show = Image.fromarray(im_show)
# im_show.save(out_path, quality=100)

# 自己画吧
image = plt.imread(img_path)
canvas = drawBoxes(image, boxes, thickness=1)
text_seq = draw_ocr_seq(canvas, boxes, txts, scores, font_path='/home/linkedata/projects/ai/MultiModal/ocr/data/font/simfang.ttf')
canvas_save = cv2.cvtColor(canvas, cv2.COLOR_BGR2RGB)
cv2.imwrite(f'{out_dir}/feature1_result3.png', canvas_save)

print(text_seq)