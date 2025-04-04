from paddleocr import PaddleOCR, draw_ocr
from utils import drawBoxes, draw_ocr_seq
import cv2
import matplotlib.pyplot as plt

# Paddleocr supports Chinese, English, French, German, Korean and Japanese
# You can set the parameter `lang` as `ch`, `en`, `french`, `german`, `korean`, `japan`
# to switch the language model in order
rec_model_dir='./inference/ch_PP-OCRv4_rec'
det_model_dir='./inference/ch_PP-OCRv4_det/Student'
# ocr = PaddleOCR() 
# ocr = PaddleOCR(use_angle_cls=True, rec_model_dir=rec_model_dir, det_model_dir=det_model_dir) 
ocr = PaddleOCR(
        use_angle_cls=True, rec_model_dir=rec_model_dir, det_model_dir=det_model_dir,
        det_db_thresh=0.2, det_db_box_thresh=0.5, drop_score=0.3    # 降低检测阈值, 有些漏检的会检测到
    ) 
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
result_name = 'feature1_result5'
image = plt.imread(img_path)
canvas = drawBoxes(image, boxes, thickness=1)
text_seq = draw_ocr_seq(canvas, boxes, txts, scores, font_path='/home/linkedata/projects/ai/MultiModal/ocr/data/font/simfang.ttf')
canvas_save = cv2.cvtColor(canvas, cv2.COLOR_BGR2RGB)
cv2.imwrite(f'{out_dir}/{result_name}.png', canvas_save)

print(text_seq)
# 打开文件，'w' 表示写入模式
with open(f'{out_dir}/{result_name}.txt', 'w') as file:
    for idx, content in text_seq:
        # 将元组中的元素按照特定格式写入
        file.write(f'{idx} {content}\n')