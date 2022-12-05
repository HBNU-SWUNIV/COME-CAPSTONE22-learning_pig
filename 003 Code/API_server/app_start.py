import csv
import os.path
from flask import Flask, render_template, request, send_file, Response
import pymysql
import json
from datetime import datetime
from io import StringIO

Test_db = pymysql.connect(
    user='root',
    passwd='7514910',
    host='127.0.0.1',
    db='test_piglet',
    charset='utf8'
)

cursor = Test_db.cursor()
app = Flask(__name__)

# field names
fields_name = ['Location', 'Date', 'Time', 'Distance', 'ID']

now = datetime.now()
current_time = now.strftime("%H:%M:%S")
current_date = now.strftime("%Y-%m-%d")


@app.route('/')
def main():
    return "Hello world"


@app.route('/view')
def index():
    sql = "SELECT * from pig_state ORDER BY distance"
    cursor.execute(sql)
    data_list = cursor.fetchall()

    return render_template('test1.html', data_list=data_list)


@app.route("/output/test.csv", methods=['GET'])
def output():
    try:

        file = 'C:\\Users\\themd\\PycharmProjects\\pythonProject\\demo_flask\\test.csv'
        if os.path.isfile(file):
            print("Yes. it is a file")
        elif os.path.isdir(file):
            print("Yes. it is a directory")
        elif os.path.exists(file):
            print("Something exist")
        else:
            sql = "SELECT * from pig_state ORDER BY distance"
            cursor.execute(sql)
            data_list = cursor.fetchall()

            file = open("test.csv", mode="w", newline='')
            writer = csv.writer(file)

            for i in data_list:
                writer.writerow([i[0], i[1], i[2], i[3], i[4]])
            print("Nothing So create file")

        return send_file("test.csv")
    except:
        return "Invalid URL or some error occured while making the GET request to the specified URL"


@app.route("/input", methods=['GET', 'POST'])
def inp():
    if request.method == "POST":
        sql = "Truncate pig_state"
        cursor.execute(sql)
        Test_db.commit()
        json_data = json.loads(request.get_data())
        if len(json_data) == 0:
            return 'No parameter'
        print(json_data)

        id = json_data['id']
        dis = json_data['distance']

        # id_list = list(map(int, id.split(', ')))
        # dis_list = list(map(float, dis.split(', ')))
    try:
        sql = "INSERT INTO pig_state (location, date, time, distance, ID) VALUES (%s, %s, %s, %s, %s)"
        for i in range(len(id)):
            if dis[i] != 0:
                cursor.execute(sql, ('02', current_date, current_time, dis[i], id[i]))
        Test_db.commit()

        return "Success"
    except:
        return "Fail"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=7070, threaded=True, debug=True)
