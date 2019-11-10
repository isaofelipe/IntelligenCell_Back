#!/usr/bin/env python
# coding: utf-8

# ## Load necessary modules
import jsonpickle
import keras

import sys

sys.path.insert(0, '../../')

from keras_retinanet import models
from keras_retinanet.utils.image import read_image_bgr, preprocess_image, resize_image
from keras_retinanet.utils.visualization import draw_box, draw_caption
from keras_retinanet.utils.colors import label_color
from keras_retinanet.utils.gpu import setup_gpu

# import miscellaneous modules
import cv2
import numpy as np
import time
import os

# use this to change which GPU to use
gpu = 0

# set the modified tf session as backend in keras
setup_gpu(gpu)

# load label to names mapping for visualization purposes
labels_to_names = {0: 'RBC', 1: 'Platelets', 2: 'WBC'}


class Analyzer:
    def __init__(self, image_path):
        self.image = read_image_bgr(image_path)
        self.model_path = os.path.join('retinanet/models/inference', 'cells.h5')
        self.model = models.load_model(self.model_path, backbone_name='resnet50')

    def find_objects(self):
        # copy to draw on
        draw = self.image.copy()
        draw = cv2.cvtColor(draw, cv2.COLOR_BGR2RGB)

        # pre-process image for network
        image = preprocess_image(self.image)
        image, scale = resize_image(image)

        # process image
        start = time.time()
        boxes, scores, labels = self.model.predict_on_batch(np.expand_dims(image, axis=0))
        print("processing time: ", time.time() - start)

        # correct for image scale
        boxes /= scale

        bounding_boxes = []

        # visualize detections
        for box, score, label in zip(boxes[0], scores[0], labels[0]):
            # scores are sorted so we can break
            if score < 0.5:
                break

            color = label_color(label)

            b = box.astype(int)  # x1, y1, x2, y2
            draw_box(draw, b, color=color)

            bounding_boxes.append({'label': label, 'positions': b})

            caption = "{} {:.3f}".format(labels_to_names[label], score)
            draw_caption(draw, b, caption)

        return {'draw': draw, 'bounding_boxes': bounding_boxes}
