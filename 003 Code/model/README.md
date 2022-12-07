# model
- Yolov5 객체 탐지, StrongSORT 객체 추적 
    - YOLOv5 : <https://github.com/ultralytics/yolov5>
    - StrongSORT : <https://github.com/mikel-brostrom/Yolov5_StrongSORT_OSNet>

## 1. YOLOv5s 모델을 사용하여 돼지 데이터셋을 학습
- YOLOv5s 모델 사용
<img src ="https://user-images.githubusercontent.com/102698011/206202341-b8763b23-5c4f-4fd9-9af1-843eb3ef4bb1.PNG" width="50%" height="50%">

-총 4개의 클래스(standing, belly, side, sitting)로 레이블링 후 데이터셋 구축 후 학습 결과

<img src ="https://user-images.githubusercontent.com/102698011/206209424-d3d6d88c-dee4-47ba-8dd9-6069ea697319.PNG" width="50%" height="50%">


## 2. StrongSort 활용하여 ID,Distance 구하기

**track.py**
- track.py에 전프레임과 현재프레임의 ID의 Distance 구함

```python
def distance_frames(prev_bbox, cur_bbox):
    prev_x = (prev_bbox[0]+prev_bbox[2])/2
    prev_y = (prev_bbox[3]+prev_bbox[1])/2

    cur_x = (cur_bbox[0]+cur_bbox[2])/2
    cur_y = (cur_bbox[3]+cur_bbox[1])/2
    dist = math.sqrt(math.pow(prev_x - cur_x, 2) + math.pow(prev_y - cur_y, 2))
    return dist
```

- ID와 Distance를 딕셔너리 형태로 변환하여 저장
```python
 if frame_idx >= 1 and id in prev:
                            dist = distance_frames(prev[id], cur[id])

                            if id not in dist_dict:
                               dist_dict[id] = dist
                            else:
                               dist_dict[id] +=dist
```
## 3. 모델 실행법
- 학습을 통한 완성된 모델이 필요

### 3-1. 객체 탐지(detection) 실행
**detect.py**
```
python detect.py --conf-thres  --iou-thres  --source --weights --agnostic-nms
```
###### --source : 영상,이미지의 주소
###### --weights : 학습을 통해 만들어진 best.pt
###### --iou-thres : iou 임계치 (NMS에 대한)
###### --conf-thres : conf 임계치 (NMS에 대한)
###### --agnostic-nms : 객체의 바운딩 박스만을 찾고 싶을때 사용


### 3-2. 객체 추적(tracking) 실행
**main.py**
```
python main.py --source  --yolo_model  --agnostic-nms --show-browser
```
   
###### --source : 영상의 주소
###### --yolo_model : 완성된 모델의 경로
###### --show-browser : flask를 통해 웹으로 전송  


