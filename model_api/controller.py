from flask import Blueprint, request, jsonify
from ..model_package.classififer_titanic import classifier_titanic_model

from .config import get_logger

_logger = get_logger(logger_name=__name__)

prediction_app = Blueprint('prediction_app', __name__)

@prediction_app.route('/health', methods=['GET'])
def health():
	if request.method == 'GET':
		return 'ok'

@prediction_app.route('/v1/predict/xgboostclassifier', methods=['POST'])
def predict():
	if request.method == 'POST':
		json_data = request.get_json()
		_logger.info(f'Inputs: {json_data}')

		result = classifier_titanic_model(request=json_data)
		_logger.info(f'Outputs: {result}')

		predicted_class = result.get('predictions')
		# version = result.get('version')

		return jsonify({'predictions':predicted_class})