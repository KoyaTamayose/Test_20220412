from flask import Flask,  request,render_template 

app = Flask(__name__)

#初回アクセス時
@app.route('/')
def index():
    return render_template('form.html') 

@app.route("/join_text",methods=["POST"])
def join_text():
    moji_A = request.form["moji_A"]
    moji_B = request.form["moji_B"]
    return render_template('form.html', moji_A = moji_A, moji_B = moji_B,)

if __name__ == "__main__":
  app.run(debug=True,port=8888)