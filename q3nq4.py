from flask import Flask, make_response,jsonify,request
import json
import urllib

app=Flask(__name__)

cookies_list=[]

@app.route('/cookies',methods=['POST'])
def cookies():
    request_data=request.get_json()
    username=request_data["username"]
    cookies_list.append(username)
    age=request_data["age"]
    resp=make_response()
    resp.set_cookie(username,str(age))
    return resp


@app.route('/getcookies')
def getcookies():
    str1=""
    for i in cookies_list:
        str1+="Key: "+str(i)+"; "+"Value: "+str(request.cookies.get(i))+"\n"
    return str1


app.run(port=8080)
