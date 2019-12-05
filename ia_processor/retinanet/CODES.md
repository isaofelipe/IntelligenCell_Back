# For test

python ./keras_retinanet/bin/evaluate.py --image-min-side 400 --image-max-side 400 --save-path ./output/ csv ./dataset/annotations/test ./dataset/classes ./models/resnet50_csv_20_x.h5

# For train

python ./keras_retinanet/bin/train.py --workers 0 --image-min-side 400 --image-max-side 400 --epochs 20 --steps 2000 csv ./dataset/annotations/train ./dataset/classes

# For inference

python ./keras_retinanet/bin/convert_model.py ./models/training/model.h5 ./models/model.h5
