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
      elif COUNT_2 == 0 and COUNT < int(DICT['QTD_ITENS']):
        COLUM_INDEX = ''
        for item_matrix in split_row:
          if split_row.index(item_matrix) == 0:
            COLUM_INDEX = item_matrix
            DICT[COLUM_INDEX] = []
          else:
            DICT[COLUM_INDEX].append(item_matrix)
          COUNT_2 -= 1
        COLUM_INDEX = ''

      # print(split_row)
    # break
  print()
  print(DICT)
  print()


# print()
# print(DICT['VALOR'])

  