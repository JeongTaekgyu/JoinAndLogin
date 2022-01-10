from flask import Flask, render_template, request, redirect
# 참고로 우리가 import 해서 사용한거중에 import뒤에 jsonfy, request 도 붙일 수 있다.
app = Flask(__name__)

from pymongo import MongoClient # pymongo를 임포트 하기(패키지 인스톨 먼저 해야겠죠?)
client = MongoClient('localhost', 27017) # mongoDB는 27017 포트로 돌아갑니다.
db = client.dbsparta # 'dbsparta'라는 이름의 db를 만듭니다.

## URL 별로 함수명이 같거나,
## route('/') 등의 주소가 같으면 안됩니다.

@app.route('/')
def home():
   return render_template('login.html')

@app.route('/signUpForm')
def signup():

   print('~~ signup 으로 들어옴')
   return render_template('join.html')

@app.route('/signupCheck', methods=['POST'])
def signupCheck():

   print('~~ signupCheck 으로 들어옴')

   email = request.form.get('email_give')
   name = request.form.get('name_give')

   print('~~~ : ', email, name)
   # email_receive = request.form['email_give'];
   # name_receive = request.form['name_give'];
   # password_receive = request.form['password_give'];
   # area_receive = request.form['area_give'];

   #doc = {'name': 'bobby', 'age': 21}  # 딕셔너리 만들고
   #db.users.insert_one(doc)

   return redirect('/')

@app.route('/login')
def signin():
   
   print('signin 으로 들어옴')
   return render_template('')

if __name__ == '__main__':
   app.run('0.0.0.0', port=5000, debug=True)