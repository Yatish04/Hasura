from flask import Flask,render_template,send_file

app=Flask(__name__)

@app.route('/image')
def home():
    return send_file('2.jpg', mimetype='image/gif')

app.run(port=8080)
