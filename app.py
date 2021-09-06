from flask import Flask
from flask import request
from ner import *


app = Flask(__name__)

@app.route('/')
def baseurl():
	return("working")

@app.route('/ner/',methods=['GET'])
def namedER():
    sentence = request.args.get('q')
    return tags(sentence)

if __name__ == '__main__':
	app.run(debug=False,host='0.0.0.0')
