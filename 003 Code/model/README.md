# model
- Yolov5 객체 탐지, StrogSORT 객체 추적 

## 1. 실시간 돈사 영상 가져오기
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

## 2. 돼지 활동량 표 가져오기
- CSV 파일을 다운로드 받아 Datatable로 변환

**main.dart**
```
Future<dynamic> downloadCsv() async {
    const url = "http://1.226.102.182:7070/output/test.csv";

    try {
        final Uri uri = Uri.parse(url);
        var csvFile = await http.read(uri);
        return const CsvToListConverter().convert(csvFile, eol: "\n");
    } catch(e) {
        print('download error:$e');
    }
}
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

