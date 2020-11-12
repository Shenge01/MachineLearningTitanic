from ..model_package.classififer_titanic import classifier_titanic_model

def test_health_endpoint_returns_200(flask_test_client):
	# When
	response = flask_test_client.get('/health')

	# Then
	assert response.status_code == 200
	
def test_prediction_endpoint_returns_prediction(flask_test_client):
	# When 
	test_json_data = {"Pclass":3, "Name":"Kelly, Mr. James","Sex":"male", "Age":34.5, "SibSp":0, "Parch":0,"Ticket":330911, "Fare":7.8292, "Cabin":"B45", "Embarked":"Q"}

	response = flask_test_client.post('/v1/predict/xgboostclassifier', json=test_json_data)

	# Then 
	assert response == 1