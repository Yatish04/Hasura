from flask import Flask,render_template,send_file

app=Flask(__name__)

@app.route('/html')
def home():
    return render_template('picture.html')

app.run(port=8080)
