from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route('/route1')
def route1():
    return render_template('page1.html')

@app.route('/route2')
def route2():
    return render_template('page2.html')

@app.route('/route3')
def route3():
    return render_template('page3.html')

if __name__ == "__main__":
    app.run()


