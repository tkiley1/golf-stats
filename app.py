from flask import Flask
from flask_cors import CORS, cross_origin
from functions import *

app = Flask(__name__)
CORS(app, support_credentials=True)

@app.route('/')
@cross_origin(supports_credentials = True)
def hello():
    return str(get_match_data())



if __name__ == '__main__':
    app.run(host='0.0.0.0')
