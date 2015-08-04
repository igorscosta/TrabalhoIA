import csv

with open('planilha.csv', 'rb') as csvfile:
	spamreader = csv.DictReader('csvfile', delimiter=';')
	print spamreader