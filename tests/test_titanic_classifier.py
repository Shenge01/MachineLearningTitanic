
import os
import sys
from pathlib import Path

# #AUTO_CODE_PATH = Path(__file__).parent.parent
# AUTO_CODE_PATH = os.environ.get('AUTO_CODE_PATH')
# print(AUTO_CODE_PATH)
# sys.path.append(f'{AUTO_CODE_PATH}')

from model_package.classififer_titanic import classifier_titanic_model


# Will need to look into the response object of this unit test in the future
def test_prediction_outcome():
	# When 
	test_data = {
	"Pclass":3,
	"Name":"Kelly, Mr. James","Sex":"male",
	"Age":34, 
	"SibSp":0, 
	"Parch":0,
	"Ticket":330911, 
	"Fare":7.8292,
	"Cabin":"B45",
	"Embarked":"Q"
	}

	result = classifier_titanic_model(test_data)
	print(result)
	
	
	assert result['predictions'] == 0