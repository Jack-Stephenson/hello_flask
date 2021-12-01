from flask import Flask
app = Flask(__name__)
@app.route('/')
def hello_world():
    return "Hello World!"
@app.route('/dojo')
def dojo():
    return "Dojo!"
@app.route('/say/<name>')
def say(name):
    return "Hi " + name + "!"
@app.route('/repeat/<number>/<inputt>')
def repeat(number, inputt):
    inputt *= int(number)
    return inputt
if __name__=="__main__":
    app.run(debug=True)