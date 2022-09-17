import csv
import os
from pickle import TRUE
import sys

BASE_DIR = 'Instancias\Instancias'
DICT = {}
COUNT = sys.maxsize
COUNT_2 = sys.maxsize
DICT['ITEM'] = []
DICT['PESO'] = []
DICT['VALOR'] = []
DICT['CAPACIDADES'] = []

def mochila_is_avaliable(obj, len_mochila):

  COUNT = 0

  for i in range(1,int(DICT['QTD_MOCHILAS'])+1):
    for item_mochila in DICT['mochila_'+str(i)]:
      conflito = DICT[str(item_mochila)]
      index_conflito = DICT['VALOR'].index(obj)
      valor = DICT[str(item_mochila)][DICT['VALOR'].index(obj)]
      if int(valor) and len(DICT['mochila_'+str(i)]) > 0:
        COUNT += 1
    
    if len_mochila == COUNT:
      DICT['mochila_'+str(i)].append(DICT['VALOR'].index(obj))
      return TRUE
    COUNT = 0

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

  # inicio do código

  for i in range(1,int(DICT['QTD_MOCHILAS'])+1):
    DICT['mochila_'+str(i)] = []

  nova_lista = DICT['VALOR'].copy() # reordenar essa lista
  nova_lista.sort()
  nova_lista.reverse()

  for obj in nova_lista:
    for i in range(1,int(DICT['QTD_MOCHILAS'])+1):
      if not DICT['mochila_'+str(i)]:
        DICT['mochila_'+str(i)].append(DICT['VALOR'].index(obj))
        break
      else:
        if mochila_is_avaliable(obj, len(DICT['mochila_'+str(i)])):
          break

  # fim do código
  break

  