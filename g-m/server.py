from flask import Flask, render_template, current_app
from sqlalchemy import create_engine,text

def noticeloader():
    sqltext="SELECT * from notice;"
    return current_app.database.execute(text(sqltext)) #sqltext를 데이터베이스에서 실행하고 그 결과를 반환한다.

def noticedeleter(title):
    sqltext="delete from notice where title='"+str(title)+"';"
    return current_app.database.execute(text(sqltext))

def noticeuploader(databasein):#databasein에는 4개의 값이 행렬로 들어가 있음
    current_app.database.execute("insert into studentlist(stname,schoolnum,phonenum,easteregg) values(%s,%s,%s,%s);",databasein) #굳이 반환이 필요없으면 이렇게 해도 된다.
    
#그리고 절대    
def noticeuploader(title,writer,summarize,maintext):
    sqltext="INSERT INTO notice(title,writer,summarize,maintext,uploadate) values('"+str(title)+"','"+str(writer)+"','"+str(summarize)+"','"+str(maintext)+"','"+"2023-05-12"+"');"
    return current_app.database.execute(text(sqltext))
#이렇게 코딩하면 안됨. sql injection 공격에 취약함.


app=Flask(__name__)


# unit-test를 실행할 때 테스트 데이터 베이스에 대한 정보를 넣어준다. = 그냥 데이터 베이스 정보 불러오기임 if else문은 혹시모를 오류를 위해 필요한거
test_config=None
if test_config is None:
    app.config.from_pyfile("config.py")
else:
    app.config.update(test_config)

# 데이터 베이스와 연동해준다.
database = create_engine(app.config['DB_URL']   , encoding = 'utf-8', max_overflow = 0)
app.database = database

app.config["SECRET_KEY"] = "secret" #데이터 베이스 접속을 위해 꼭 필요한 암호키, 설정이 안되어 있으면 보안 문제로 오류가 뜬다.

@app.route('/')
def index():
    real_data=[]
    data = noticeloader() #<sqlalchemy.engine.cursor.LegacyCursorResult object at 0x00000250846DCEE0> 형식임 = 바로 사용x
    for i in data:
        real_data.append(i)#이런 식으로 안에있는 걸 하나하나 넣어줘야됨
    return render_template('index.html',data=real_data)

if __name__ == '__main__':
    app.run(debug=True)