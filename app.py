from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route("/redirect")
def redirectpage():
    return render_template('redirect.html')

@app.route("/query")
def querytest():
    query = request.args.get('query')
    return render_template('querytest.html', query=query)

if __name__ == '__main__':
    app.run(debug=True)
