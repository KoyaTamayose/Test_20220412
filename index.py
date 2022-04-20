from flask import Flask,render_template  # 必要なライブラリのインポート

app = Flask(__name__)#アプリの設定

@app.route('/') #どのページで実行する関数か設定
def index():
    return render_template('form.html')  #HelloWorldを返却

if __name__ == "__main__":  #ここはmain
    app.run(debug=True,port=8888)     #実行する    

