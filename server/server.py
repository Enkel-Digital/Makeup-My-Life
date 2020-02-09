from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello():
    return "Makeup"

if __name__ == '__main__':
    app.run()