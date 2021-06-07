from flask import Flask,render_template
import random
app = Flask(__name__)

@app.route('/')
def hello():
    unsei_list=["大吉","中吉","小吉"]
    uranai = random.choice(unsei_list)
    return render_template("index.html",fortune=uranai,fortune_list=unsei_list)
		
if __name__ == "__main__":
    app.run(debug=True)


@app.route('/fortune')
def fortune():
    unsei_list=["大吉","中吉","小吉"]
    uranai_list=[
        {"day":"今日","fortune":random.choice(unsei_list)},
        {"day":"明日","fortune":random.choice(unsei_list)},
        {"day":"明後日","fortune":random.choice(unsei_list)}
    ]
    return render_template('fortune.html',fortune_list=uranai_list)
