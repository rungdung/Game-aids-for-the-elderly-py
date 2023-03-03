from ultralytics import YOLO
from ultralytics.yolo.v8.detect.predict import DetectionPredictor
import cv2
import numpy as np


import glob
import os

def on_predict_batch_end(predictor):
    _, _, _, _, _ = predictor.batch
    with open('probs.txt', 'a') as f:
        for result in predictor.results:
            # Save the prediction and input image to disk
            probs = result.probs
            f.write(str(probs) + '\n')

 # Save the prediction and input image to disk

model = YOLO('model/best28-02.pt')
def startInference():
    model.add_callback("on_predict_batch_end", on_predict_batch_end )
    model.predict(source=0, show=True, save_txt=True)

def latestRoll():
    # Get the latest directory
    root = 'runs/detect/'

    folders = []
    for dir in os.listdir(root):
        path = os.path.join(root, dir)
        if os.path.isdir(path): folders.append(path)
    latest_subdir = max(folders, key=os.path.getmtime)
    print(latest_subdir)

    # Get latest file
    list_of_files = glob.glob(latest_subdir + '/labels/*') # * means all if need specific format then *.csv
    latest_file = max(list_of_files, key=os.path.getctime)
    print(latest_file)

def main():
    startInference()