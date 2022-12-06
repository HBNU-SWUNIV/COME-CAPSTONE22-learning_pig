# WebApp
- Flutter 사용하여 개발
- main.dart 파일에 대한 설명

## 1. 실시간 돈사 영상 가져오기
- Web에서 webview 사용하기 위해 **webviewx** 라이브러리 사용
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
