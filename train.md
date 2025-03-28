## 模型训练
### 检测模型
```
python tools/train.py -c configs/det/ch_PP-OCRv4/ch_PP-OCRv4_det_cml.yml
```
```
python tools/train.py -c configs/det/ch_PP-OCRv4/ch_PP-OCRv4_det_cml.yml \
     -o Global.pretrained_model=./pretrain_models/ch_PP-OCRv4_det_train/best_accuracy
```
### 识别模型
```
python tools/train.py -c configs/rec/PP-OCRv4/ch_PP-OCRv4_rec.yml
```
```
python tools/train.py -c configs/rec/PP-OCRv4/ch_PP-OCRv4_rec.yml \
     -o Global.pretrained_model=./pretrain_models/ch_PP-OCRv4_rec_train/student
```
```
python tools/train.py -c configs/rec/PP-OCRv4/ch_PP-OCRv4_rec_distillation.yml \
     -o Global.pretrained_model=./pretrain_models/ch_PP-OCRv4_rec_train/student
```

## 模型导出
### 检测模型
```
python tools/export_model.py -c configs/det/ch_PP-OCRv4/ch_PP-OCRv4_det_cml.yml \
     -o Global.pretrained_model="./output/ch_PP-OCRv4_det/best_model/model.pdparams" Global.save_inference_dir="./inference/ch_PP-OCRv4_det"
```

### 识别模型
```               
python tools/export_model.py -c configs/rec/PP-OCRv4/ch_PP-OCRv4_rec.yml \
     -o Global.pretrained_model="./output/ch_PP-OCRv4_rec/best_model/model.pdparams" Global.save_inference_dir="./inference/ch_PP-OCRv4_rec"
```

## 使用训练模型
