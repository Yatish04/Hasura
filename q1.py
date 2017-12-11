from flask import Flask

app=Flask(__name__)
@app.route('/')
def display():
    return "Hello World - Yatish"
app.run(port=8080)
