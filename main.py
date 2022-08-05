from flask import Flask,request
app=Flask(__name__)
import mail


@app.route('/login',methods = ['POST'])
def login():
      print(request.json)
      mail.sendMail(request.json["name"],request.json["email"],request.json["body"])
      return "success"




if __name__ == '__main__':
   app.run(debug = True)