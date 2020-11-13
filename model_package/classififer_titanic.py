import pandas as pd
import numpy as np 
import joblib

from ..preprocessors.titanic_module import create_status, male_female_child, family, other_titles

#pickle_jar_path = 'MachineLearning/pickle_jar'
pickle_jar_path = 'pickle_jar'

ohe_titanic = joblib.load(f'{pickle_jar_path}/ohe_titanic.pkl')
classifier_model_titanic = joblib.load(f"{pickle_jar_path}/xg_boost_titanic.pkl")

def classifier_titanic_model(request):
	# Cast values from the incoming request
	Pclass = int(request['Pclass'])
	Name = str(request['Name'])
	Sex = str(request['Sex'])
	Age = int(request['Age'])
	SibSp = int(request['SibSp'])
	Parch = int(request['Parch'])
	Ticket = int(request['Ticket'])
	Fare = int(request['Fare'])
	Cabin = str(request['Cabin'])
	Embarked = str(request['Embarked'])

	# Create a dataframe 
	input_data = pd.DataFrame([Pclass, Name, Sex, Age, SibSp, Parch, Ticket, Fare, Cabin, Embarked]).T

	# Rename Columns 
	input_data.columns = ['Pclass','Name', 'Sex', 'Age', 'SibSp', 'Parch', 'Ticket', 'Fare', 'Cabin', 'Embarked']

	input_data[['Fare', 'Age']] = input_data[['Fare', 'Age']].astype(int)
	print(input_data.info())

	# Feature Engineering 
	# Create Status
	input_data['Status'] = input_data['Name'].apply(create_status)
	# Replace titles with 'Other'
	input_data['Status'] = other_titles(input_data, 'Status')
	# Total Family members
	input_data['Family'] = family(input_data.SibSp, input_data.Parch)
	# Classify by Gender
	input_data['Person'] = input_data[['Age','Sex']].apply(male_female_child, axis = 1)
	# Drop Unrequired Fields 
	input_data.drop(['Name', 'SibSp', 'Parch', 'Ticket', 'Cabin', 'Sex'], axis = 1, inplace=True)
	#['Name','SibSp', 'Parch','Ticket','Cabin', 'Sex']
	cols = ['Pclass', 'Embarked', 'Person', 'Status']

	input_data.Pclass = input_data.Pclass.map({1 : 'first',2 : 'second', 3 : 'third'})
	
	# Encode categorical fetatures
	encoded = ohe_titanic.transform(input_data)

	#print(f"COLUMNS OF THIS ARE {encoded.columns}")

	encoded = encoded[['Pclass_third', 'Pclass_first', 'Pclass_second', 'Age', 'Fare',
				'Embarked_S', 'Embarked_C', 'Embarked_Q', 'Person_male',
				'Person_female', 'Person_Child', 'Family', 'Status_Mr', 'Status_Mrs',
				'Status_Miss', 'Status_Other']]

	# make a prediction
	prediction = classifier_model_titanic.predict(encoded)	

	return int(prediction)