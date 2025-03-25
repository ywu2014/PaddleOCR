a, c = [225, 330], [260, 363]
b = [c[0], a[1]]
d = [a[0], c[1]]

print(f"{a}, {b}, {c}, {d}")



# python tools/train.py -c configs/det/ch_PP-OCRv4/ch_PP-OCRv4_det_cml.yml \
#      -o Global.pretrained_model=./pretrain_models/ch_PP-OCRv4_det_train/best_accuracy