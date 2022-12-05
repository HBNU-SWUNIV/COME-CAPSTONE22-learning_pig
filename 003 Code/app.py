from flask import *
import urllib.request
import requests

# app = Flask(__name__, template_folder='web')

app = Flask(__name__)
FLUTTER_WEB_APP = 'templates'


@app.route("/web/flutter.js", methods=["GET"])
def flutter_js():
    return render_template("flutter.js")


@app.route("/main.dart.js", methods=["GET"])
def main_dart_js():
    return render_template("main.dart.js")


@app.route("/web/assets/FontManifest.json", methods=["GET"])
def font_json():
    return render_template("assets/FontManifest.json")


@app.route('/')
def render_page():
    return render_template("index.html")


@app.route('/web/')
def render_page_web():
    return render_template('index.html')


@app.route('/web/<path:name>')
def return_flutter_doc(name):
    datalist = str(name).split('/')
    print(datalist)
    DIR_NAME = FLUTTER_WEB_APP

    if len(datalist) > 1:
        for i in range(0, len(datalist) - 1):
            DIR_NAME += '/' + datalist[i]

    return send_from_directory(DIR_NAME, datalist[-1])


if __name__ == '__main__':
    app.run()
