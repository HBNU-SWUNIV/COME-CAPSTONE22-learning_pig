import 'dart:async' show Future;
import 'package:csv/csv.dart';
import 'package:http/http.dart' as http;
import 'package:flutter/material.dart';
import 'package:webviewx/webviewx.dart';

void main() {
  runApp(const MyApp());
}

class MyApp extends StatelessWidget {
  const MyApp({super.key});

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      theme: ThemeData(
        visualDensity: VisualDensity.adaptivePlatformDensity,
      ),
      home: const HomePage(),
    );
  }
}

class HomePage extends StatefulWidget {
  const HomePage({Key? key}) : super(key: key);

  @override
  State<HomePage> createState() => _HomePageState();
}

class _HomePageState extends State<HomePage> {

  Color mainColor = const Color(0xFF1A1C1E);
  Color serveColor = const Color(0xFFFFFFFF);

  List<List<dynamic>>?csvData;

  late WebViewXController webViewXController;

  @override
  void initState() {
    super.initState();

    downloadCsv();
  }

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

  @override
  void dispose() {
    webViewXController.dispose();
    super.dispose();
  }

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      home: Scaffold(
        backgroundColor: serveColor,
        appBar: AppBar(
          backgroundColor: mainColor,
          elevation: 0.0,
          title: const Text("Capstone Design!!"),
        ),
        body: ListView(
          shrinkWrap: true,
          children: [

            WebViewX(
              initialContent: "http://39.125.58.48:5001",
              initialSourceType: SourceType.url,
              width: MediaQuery.of(context).size.width,
              height: 500,
              onWebViewCreated: (controller) => webViewXController = controller,
            ),

            SingleChildScrollView(
              scrollDirection: Axis.horizontal,
              child: Column(
                children: [
                  csvData == null ? const CircularProgressIndicator() : DataTable(
                // DataTable(
                  columns: const <DataColumn>[
                    DataColumn(
                      label: SizedBox(
                        width: 30,
                        child:Text(
                          'Location',
                          style: TextStyle(fontStyle: FontStyle.italic, fontSize: 9),
                        )
                      )
                    ),
                    DataColumn(
                      label: SizedBox(
                          width: 30,
                          child:Text(
                            'Location',
                            style: TextStyle(fontStyle: FontStyle.italic, fontSize: 9),
                          )
                      )
                    ),
                    DataColumn(
                      label: SizedBox(
                          width: 30,
                          child:Text(
                            'Location',
                            style: TextStyle(fontStyle: FontStyle.italic, fontSize: 9),
                          )
                      )
                    ),
                    DataColumn(
                      label: SizedBox(
                          width: 30,
                          child:Text(
                            'Location',
                            style: TextStyle(fontStyle: FontStyle.italic, fontSize: 9),
                          )
                      )
                    ),
                    DataColumn(
                      label: SizedBox(
                          width: 30,
                          child:Text(
                            'Location',
                            style: TextStyle(fontStyle: FontStyle.italic, fontSize: 9),
                          )
                      )
                    ),
                  ],

                  rows: csvData!.map(
                    (csvRow) => DataRow(
                      cells: csvRow.map(
                        (csvItem) => DataCell(
                          SizedBox(
                            width: 30,
                            child: Text(
                              csvItem.toString(),
                              style: const TextStyle(fontSize: 7),
                            )
                          )
                        ),
                      ).toList(),
                    ),
                  ).toList(),
                ),
                ]
              )
            )
          ],
        ),

        floatingActionButton: FloatingActionButton(
          onPressed: () async {
            csvData = null;
            csvData = await downloadCsv();
            // csvData?.removeAt(0);
            setState(() {});
          },
          child: const Icon(
              Icons.table_chart_outlined
          ),
        ),
      ),
    );
  }
}

// flutter build web --release -v