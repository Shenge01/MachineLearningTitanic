import pandas as pd
import numpy as np 
import joblib

from ..preprocessors.titanic_module import create_status, male_female_child, family, other_titles

pickle_jar_path = 'MachineLearning/pickle_jar'

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
	Fare = float(request['Fare'])
	Cabin = str(request['Cabin'])
	Embarked = str(request['Embarked'])

	# Create a dataframe 
	input_data = pd.DataFrame([Pclass, Name, Sex, Age, SibSp, Parch, Ticket, Fare, Cabin, Embarked]).T

	# Rename Columns 
	input_data.columns = ['Pclass','Name', 'Sex', 'Age', 'SibSp', 'Parch', 'Ticket', 'Fare', 'Cabin', 'Embarked']

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
	print(input_data.info())
	print(input_data.head())
	print("----")
	encoded = ohe_titanic.transform(input_data[cols])
	data_1 = input_data.drop(labels=cols, axis=1)
	input_data = pd.merge(data_1,encoded, how='inner', left_index=True, right_index=True)
	print(encoded.info())
	print(encoded.head())

	actual_cols = ['Age', 'Fare', 'Family', 'Pclass_first', 'Pclass_second',
					'Pclass_third', 'Embarked_C', 'Embarked_Q', 'Embarked_S',
					'Person_Child', 'Person_female', 'Person_male', 'Status_Miss',
					'Status_Mr', 'Status_Mrs', 'Status_Other']

	data_1[['Fare', 'Age']].astype(float)
	# make a prediction
	prediction = classifier_model_titanic.predict(input_data)	

	return int(prediction)