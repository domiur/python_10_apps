from flask import Flask

app=Flask(__name__)

@app.route('/')
def home():
    return "hello world 1" 

@app.route('/about')
def about():
    return "hello world 2"


if __name__=="__main__":
    app.run(debug=True)