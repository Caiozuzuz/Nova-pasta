import csv
import os
import sys

BASE_DIR = 'Instancias\Instancias'
DICT = {}
COUNT = sys.maxsize
COUNT_2 = sys.maxsize
DICT['ITEM'] = []
DICT['PESO'] = []
DICT['VALOR'] = []
DICT['CAPACIDADES'] = []

for file in os.listdir(BASE_DIR):
  with open(BASE_DIR + '\\' + file, 'r') as file:
    my_reader = csv.reader(file, delimiter=',')
    for row in my_reader:
      split_row = row[0].split(';')
      if split_row[0] == 'QTD_ITENS':
        DICT['QTD_ITENS'] = split_row[1]
      elif split_row[0] == 'QTD_MOCHILAS':
        DICT['QTD_MOCHILAS'] = split_row[1]
      elif split_row[0] == 'CAPACIDADES':
        for capacidade in split_row:
          if capacidade != 'CAPACIDADES':
            DICT['CAPACIDADES'].append(capacidade)
      elif split_row[0] == 'ITEM' and split_row[1] == 'PESO':
        COUNT = 0
      elif COUNT != sys.maxsize and COUNT < int(DICT['QTD_ITENS']):
        DICT['ITEM'].append(split_row[0])
        DICT['PESO'].append(split_row[1])
        DICT['VALOR'].append(split_row[2])
        COUNT += 1
      elif split_row[0] == 'ITEM' and split_row[1] == '0':
        COUNT_2 = 0
        for item_matrix in split_row:
          if item_matrix != 'ITEM':
            DICT[item_matrix] = []
      elif COUNT_2 != sys.maxsize and COUNT_2 < int(DICT['QTD_ITENS']):
        COLUM_INDEX = ''
        for item_matrix_2 in range(1,21,1):
          DICT[str(COUNT_2)].append(split_row[item_matrix_2])
        COUNT_2 += 1
        COLUM_INDEX = ''

      print(split_row)
    
  COUNT = sys.maxsize
  COUNT_2 = sys.maxsize
  print()
  print(DICT)
  print()

  # inicio do código

  print(DICT['VALOR']) # copiar essa lista

  nova_lista = DICT['VALOR'].copy() # reordenar essa lista
  nova_lista.sort()
  nova_lista.reverse()
  print()
  print(nova_lista)
  print()
  print(DICT['VALOR'].index(nova_lista[0])) # te fala o index

  # fim do código

  break

  