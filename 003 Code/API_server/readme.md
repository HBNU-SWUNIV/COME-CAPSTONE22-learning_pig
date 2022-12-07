### API Server
  - Flask를 사용하여 개발
  
  ### 1. 웹에 DB데이터 보여주기
  - app.start_33번째 줄
  - IP 뒤에 "/view"를 치면 실행
  - sql문과 cursor를 이용하여 HTML 파일로 전달
  
```
  @app.route('/view')
  def index():
    sql = "SELECT * from pig_state ORDER BY distance"
    cursor.execute(sql)
    data_list = cursor.fetchall()

    return render_template('test1.html', data_list=data_list)
```


  ### 2. DB에서 값을 불러와 작성 후 Flutter에 작성된 csv파일 전송
  - app.start_42번째 줄
  - IP 뒤에 "/output/test.csv"를 치면 실행
  - Flask에 포함된 sendfile()을 사용하여 전송 
  
```
@app.route("/output/test.csv", methods=['GET'])
def output():
    try:
        sql = "SELECT * from pig_state ORDER BY distance"
        cursor.execute(sql)
        data_list = cursor.fetchall()

        file = open("test.csv", mode="w", newline='')
        writer = csv.writer(file)

        for i in data_list:
            writer.writerow([i[0], i[1], i[2], i[3], i[4]])

        file = 'C:\\Users\\themd\\PycharmProjects\\pythonProject\\demo_flask\\test.csv'
        if os.path.isfile(file):
            print("Yes. it is a file")
        elif os.path.isdir(file):
            print("Yes. it is a directory")
        elif os.path.exists(file):
            print("Something exist")
        else:
            print("Nothing So create file")

        return send_file("test.csv")
    except:
        return "Invalid URL or some error occured while making the GET request to the specified URL"
```

  ### 3. 모델에 포함된 send()에서 json형태의 값을 받아 DB에 저장
  - app.start_70번째 줄
  - 별개의 코드에서 POST요청을 통해 값을 전송해야 함
  - .commit()을 통해 실제 DB에 값을 추가함
  
```
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

    try:
        sql = "INSERT INTO pig_state (location, date, time, distance, ID) VALUES (%s, %s, %s, %s, %s)"
        for i in range(len(id)):
            if dis[i] != 0:
                cursor.execute(sql, ('02', current_date, current_time, dis[i], id[i]))
        Test_db.commit()

        return "Success"
    except:
        return "Fail"
```
  ### 4. send.py 사용법
  - ID, distance에 원하는 데이터를 리스트의 형태로 저장하면, json형태로 변환하여 post 요청함
  - send()함수가 호출되어야만 함
  - 보내고자 하는 호스트의 IP/input을 url로 적으면 전송한 값이 DB에 저장
  
  ```
  def send():
    url = "http://1.226.102.182:7070/input"
    data = {
        'id': ID,
        'distance': distance}

    data = json.dumps(data)

    headers = {'Content-Type': 'application/json', 'Accept': 'application/json'}
    response = requests.post(url, data, headers=headers)
    print(response)
    return response.text
    ```
    
    
    
  
