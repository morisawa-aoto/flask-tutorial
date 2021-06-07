from flask import Flask,render_template
import random
app = Flask(__name__)

@app.route('/')
def hello():
    uranai = random.choice(["大吉","中吉","小吉"])
    return render_template("index.html",fortune=uranai)
		
if __name__ == "__main__":
    app.run(debug=True)