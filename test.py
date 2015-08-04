import os
import csv
import random
import string 

#pega os dados do sistema em seu diretorio cwd = current working directory

def pegar_diretorio(arquivo):
	diretorioatual = os.getcwd()
 	diretorio_arquivo = os.path.join(os.getcwd(), arquivo)
 	print diretorio_arquivo
 	return diretorio_arquivo

diretorio = pegar_diretorio('dados_em_colunas_estatico.csv')

#le o csv de um determinado diretorio

def ler_csv(diretorioArquivo):
	with open(diretorio, 'rU') as csvfile:
 		reader = csv.reader(csvfile)
 		for row in reader:	
 			print row

ler_csv(diretorio)