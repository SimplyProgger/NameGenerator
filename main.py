import csv
from random import randint


def GenerateName(sex=None):

	if sex == None:
		with open('resource/russian_names.csv', encoding='UTF-8') as csvFile:
			csvReader = csv.DictReader(csvFile, delimiter=';')
			dict_names = list(csvReader)
			len_dict = len(dict_names)
			random_index = randint(0, len_dict)
			return dict_names[random_index]['Name']


	if sex.lower() == 'male':
		with open('resource/russian_names.csv', encoding='UTF-8') as csvFile:
			csvReader = csv.DictReader(csvFile, delimiter=';')
			dict_names = list(csvReader)
			len_dict = len(dict_names)
			random_index = randint(0, len_dict)
			sex_random = dict_names[random_index]['Sex']
			while sex_random != 'М':
				random_index = randint(0, len_dict)
				sex_random = dict_names[random_index]['Sex']
			return dict_names[random_index]['Name']


	elif sex.lower() == 'female':
		with open('resource/russian_names.csv', encoding='UTF-8') as csvFile:
			csvReader = csv.DictReader(csvFile, delimiter=';')
			dict_names = list(csvReader)
			len_dict = len(dict_names)
			random_index = randint(0, len_dict)
			sex_random = dict_names[random_index]['Sex']
			while sex_random != 'Ж':
				random_index = randint(0, len_dict)
				sex_random = dict_names[random_index]['Sex']
			return dict_names[random_index]['Name']


	else:
		raise BadValueError('Выбран неправильный пол')
			


print(GenerateName(sex='ер'))