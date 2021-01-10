import os
from flask import Flask
app = Flask(__name__)

text = os.environ['TEXT']
debug = os.environ['DEBUG']
port = os.environ['PORT']

@app.route('/')
def main():
    return f"{text}"

if __name__ == '__main__':
    app.run(host ='0.0.0.0', port=port, debug=debug)