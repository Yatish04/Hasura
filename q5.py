from flask import Flask,render_template,send_file

app=Flask(__name__)

@app.route('/robots.txt')
def home():
    return render_template('deny.html'),404

app.run(port=8080)
