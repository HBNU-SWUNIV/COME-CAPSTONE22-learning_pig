# model
- Yolov5 객체 탐지, StrongSORT 객체 추적 
    - YOLOv5 : <https://github.com/ultralytics/yolov5>
    - StrongSORT : <https://github.com/mikel-brostrom/Yolov5_StrongSORT_OSNet>

## 1. YOLOv5s 모델을 사용하여 돼지 데이터셋을 학습
- Web에서 webview 사용하기 위해 **webviewx** 라이브러리 사용

**main.dart**
```
WebViewX(
    initialContent: "http://39.125.58.48:5001",
    initialSourceType: SourceType.url,
    width: MediaQuery.of(context).size.width,
    height: 500,
    onWebViewCreated: (controller) => webViewXController = controller,
)
```

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
## 3. pubspec.yaml
- Flutter는 사용하는 라이브러리를 pubspec.yaml 파일에 추가

### 3-1. 직접 추가하는 방법
**pubspec.yaml**
```
dependencies:
    flutter:
        sdk: flutter

    csv: ^5.0.1
    http: ^0.13.5
    webviewx: ^0.2.1
```
- 사용할 라이브러리 버전과 함께 직접 추가

### 3-2. Terminal로 추가하는 방법
**Terminal**
```
>> flutter pub add http
>> flutter pub add csv
>> flutter pub add webviewx
```
- Terminal을 이용하면 가장 최신 버전으로 자동으로 추가
```
>> flutter pub get
```
- pub add 후에 pub get 해줘야 변화가 반영됨

