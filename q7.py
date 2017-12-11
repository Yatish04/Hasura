from flask import Flask,render_template,send_file,request
import sys

app=Flask(__name__)

@app.route('/input')
def home():
    return render_template('newhtml.html')

@app.route('/input',methods=['POST'])
def fname():
    text1="Name :" + str(request.form["Name"])
    text2="Age :" + str(request.form["Age"])
    print(text1+"\n"+text2, file=sys.stdout)
    sys.stdout.flush()
    return "Check the Console"
app.run(port=8080)
