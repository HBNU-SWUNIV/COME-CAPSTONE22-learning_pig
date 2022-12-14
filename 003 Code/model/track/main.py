from flask import Flask, render_template, Response
import cv2
from track import detect
#from track import test12

app = Flask(__name__)

@app.route('/')
def index():
   """Video streaming ."""
   return render_template('index.html')

import argparse
parser = argparse.ArgumentParser()
parser.add_argument('--yolo_model', nargs='+', type=str, default='', help='model.pt path(s)') #yolov5s.pt
parser.add_argument('--deep_sort_model', type=str, default='osnet_x0_25_market1501')
parser.add_argument('--source', type=str, default='https://www.youtube.com/', help='source')  # file/folder, 0 for webcam
parser.add_argument('--output', type=str, default='inference/output', help='output folder')  # output folder
parser.add_argument('--imgsz', '--img', '--img-size', nargs='+', type=int, default=[640], help='inference size h,w')
parser.add_argument('--conf-thres', type=float, default=0.5, help='object confidence threshold')
parser.add_argument('--iou-thres', type=float, default=0.5, help='IOU threshold for NMS')
parser.add_argument('--fourcc', type=str, default='mp4v', help='output video codec (verify ffmpeg support)')
parser.add_argument('--device', default='', help='cuda device, i.e. 0 or 0,1,2,3 or cpu')
parser.add_argument('--show-vid', action='store_true', help='display tracking video results')
parser.add_argument('--show-browser', action='store_true', help='display tracking video results')
parser.add_argument('--save-vid', action='store_true', help='save video tracking results')
parser.add_argument('--save-txt', action='store_true', help='save MOT compliant results to *.txt')
# class 0 is person, 1 is bycicle, 2 is car... 79 is oven
parser.add_argument('--classes', nargs='+', type=int, help='filter by class: --class 0, or --class 16 17')
parser.add_argument('--agnostic-nms', action='store_true', help='class-agnostic NMS')
parser.add_argument('--augment', action='store_true', help='augmented inference')
parser.add_argument('--update', action='store_true', help='update all models')
parser.add_argument('--evaluate', action='store_true', help='augmented inference')
parser.add_argument("--config_deepsort", type=str, default="deep_sort/configs/deep_sort.yaml")
parser.add_argument("--half", action="store_true", help="use FP16 half-precision inference")
parser.add_argument('--visualize', action='store_true', help='visualize features')
parser.add_argument('--max-det', type=int, default=1000, help='maximum detection per image')
parser.add_argument('--save-crop', action='store_true', help='save cropped prediction boxes')
parser.add_argument('--dnn', action='store_true', help='use OpenCV DNN for ONNX inference')
parser.add_argument('--project', default='runs/track', help='save results to project/name')
parser.add_argument('--name', default='exp', help='save results to project/name')
parser.add_argument('--exist-ok', action='store_true', help='existing project/name ok, do not increment')
opt = parser.parse_args()
opt.imgsz *= 2 if len(opt.imgsz) == 1 else 1  # expand


@app.route('/video_feed')
def video_feed():
   """Video streaming route. Put this in the src attribute of an img tag."""


   return Response(detect(opt),
                   mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/test')
def testa():

    return
if __name__ == '__main__':


    app.run(debug=True, threaded=True,host = "0.0.0.0", port=5001)



