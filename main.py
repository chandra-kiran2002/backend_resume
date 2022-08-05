from flask import Flask,request
from flask_cors import CORS, cross_origin
app=Flask(__name__)
import mail
CORS(app)

@app.route('/',methods = ['POST'])
def home():
      return "hello"


@app.route('/login',methods = ['POST'])
def login():
      print(request.json)
      if mail.sendMail(request.json["name"],request.json["email"],request.json["body"]) is True:
           return "success"
      else:
          return "failed"




if __name__ == '__main__':
   app.run(debug = True)