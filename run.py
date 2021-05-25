# Entry point to start our flask application

from flask import Flask, request

from model_package.classififer_titanic import classifier_titanic_model

app = Flask(__name__)

@app.route("/")
def test():
	return "It Works!!"

@app.route("/xgboostclassifier", methods=['POST'])
def titanic_functions():
	api_request = request.get_json()

	result = classifier_titanic_model(api_request)

	return result