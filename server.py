from flask import Flask, render_template

app = Flask(__name__)

@app.route('/play/<int:num>/<bgcolor>')
def index(num,bgcolor):
    return render_template("index.html",bgcolor = bgcolor, num=num)
    




if __name__=="__main__":
    app.run(debug=True,host='localhost',port=5001)
