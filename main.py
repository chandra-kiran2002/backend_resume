from flask import Flask,request
app=Flask(__name__)
import mail


@app.route('/login',methods = ['POST', 'GET'])
def login():
      print(request.json)
      mail.sendMail()
      return "hi"




if __name__ == '__main__':
   app.run(debug = True)