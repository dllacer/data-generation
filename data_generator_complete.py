import os
import argparse
from faker import Faker
import csv
from random import randrange

'''
Author: David Llacer (dllacer@sfy.com)
This python script generates random data and saves it in a csv file.
You can specify which data it generates!
It works for spanish data only. You can change the locale of
Nombre, Apellido, DNI, Edad, Teléfono, Ciudad, País, Contraseña
'''

def parse_args():

	parser = argparse.ArgumentParser()

	parser.add_argument("--filename", "-f", action='store', type=str, help='name of the csv file you are going to generate')
	parser.add_argument("--rows_num", "-r",action="store", type=int, help='number of rows you want to generate')
	parser.add_argument("--quote", "-q", action="store_true", default=False, help='quotes every field')
	parser.add_argument("--dummie", action="store_true", default=False, help='does nothing')
	parser.add_argument("--name", "-n",action="store_true", default=False, help='generates names')
	parser.add_argument("--lastname", "-l", action="store_true", default=False, help='generates lastnames')
	parser.add_argument("--nameandlastname", "-ln", action="store_true", default=False, help='generates names and surname')
	parser.add_argument("--dni", "-d", action="store_true", default=False, help='generates dni (spanish id card)')
	parser.add_argument("--age", "-a",action="store_true", default=False, help='generates ages')
	parser.add_argument("--phone", "-p", action="store_true", default=False, help='generates phones')
	parser.add_argument("--city", "-c",action="store_true", default=False, help='generates cities')
	parser.add_argument("--country", "-co", action="store_true", default=False, help='generates countries')

	opt = parser.parse_args()
	return opt

def rnd_phone():
	phone = "6"
	for i in range(8):
		phone = phone + str(randrange(10))

	return phone

def calc_letter(dni_num):
	return 'TRWAGMYFPDXBNJZSQVHLCKE'[int(dni_num) % 23]

def rnd_dni():
	dni = ""
	for i in range(8):
		dni += str(randrange(10))

	return dni + calc_letter(dni)

def rnd_age(low=1, high=100):
	return str(randrange(low, high))

if __name__ == '__main__':
	faker = Faker(['es_ES'])
	opt = parse_args()

	if (os.path.exists("./data_generated") == False):
		os.mkdir("data_generated")

	if opt.quote: quoting = csv.QUOTE_ALL
	else: quoting = csv.QUOTE_NONE

	if (opt.filename and opt.rows_num):
		filepath = os.path.join("data_generated", opt.filename)
		with open(filepath, 'w', newline='') as file:
			writer = csv.writer(file, quoting=quoting)
			for i in range(opt.rows_num):
				row = []
				if opt.name:
					name = faker.first_name()
					row.append(name)
				if opt.lastname:
					lastname = faker.last_name()
					row.append(lastname)
				if opt.nameandlastname:
					name = faker.first_name() + " " + faker.last_name()
					row.append(nameandlastname)
				if opt.dni:
					dni = rnd_dni()
					row.append(dni)
				if opt.age:
					age = rnd_age()
					row.append(age)
				if opt.phone:
					phone = rnd_phone()
					row.append(phone)
				if opt.city:
					city = faker.city()
					row.append(city)
				if opt.country:
					country = faker.country()
					row.append(country)

				writer.writerow(row)
	else:
		print("filename and rows_num arguments are required")
