from flask import Flask, make_response,jsonify,request

import json
import urllib
import sys


app=Flask(__name__)
auth_dict={}
post_dict={}

def make_req():
    authors=urllib.request.urlopen('https://jsonplaceholder.typicode.com/users').read().decode()
    auths=json.loads(authors)
    for i in auths:
        auth_dict[i['id']]=i['name']
    return

def make_req1():
    posts=urllib.request.urlopen('https://jsonplaceholder.typicode.com/posts').read().decode()
    post=json.loads(posts)
    for i in post:
        try:
            post_dict[i['userId']]+=1
        except:
            post_dict[i['userId']]=1
    return

def join():
    make_req()
    make_req1()
    str1=""
    for i in auth_dict.keys():
        try:
            str1+="Author : "+str(auth_dict[i]+ "\n" + "Number of posts : "+str(post_dict[i])+"\n"+"\n")
            print("Author :",auth_dict[i])
            print("Number of posts :",post_dict[i])
        except:
            pass
    return str1

@app.route('/authors')
def parse():
    print('This error output', file=sys.stderr)
    print('This standard output', file=sys.stdout)
    temp = join()
    return temp
app.run(port=8080)
