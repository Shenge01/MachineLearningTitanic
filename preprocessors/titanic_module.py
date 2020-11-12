import re

def create_status(name):
    m = re.search(" [A-Za-z]+\.", name)
    if m:
        status = re.sub('\.', '', re.sub(" ", "", m.group(0)))
        return status
    else:
        return "None"

def male_female_child(column):
    age, sex = column
    if age < 16:
        return 'Child'
    else:
        return sex

def family(field1, field2):
	return int(field1 + field2)

def other_titles(data_object, column):
	Others = ['Dona','Master', 'Dr', 'Rev',
			 'Major', 'Col', 'Mlle', 'Ms', 
			 'Lady', 'Capt', 'Countess', 
			 'Mme', 'Sir', 'Jonkheer', 'Don']
	for title in data_object[column]:
		if title in Others:
			data_object.column = data_object[column].replace(title, 'Other')

	return data_object[column]