from flask import Flask,request
app=Flask(__name__)

@app.route("/")
def index():
    print(request.headers)
    return "hello,world"

if __name__=="__main__":
    app.run()