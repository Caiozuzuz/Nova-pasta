import os
from pickle import TRUE
import sys

def mochila_is_avaliable(obj, DICT):
  COUNT = 0
  for i in range(1,int(DICT['QTD_MOCHILAS'])+1):
    len_mochila = len(DICT['mochila_'+str(i)])
    for item_mochila in DICT['mochila_'+str(i)]:
      index_atual = DICT['VALOR'].index(obj)
      conflito = DICT[str(item_mochila)]
      posicao = DICT[str(item_mochila)][DICT['VALOR'].index(obj)]
      if int(DICT[str(item_mochila)][DICT['VALOR'].index(obj)]) and len(DICT['mochila_'+str(i)]) > 0:
        COUNT += 1
    
    if len_mochila == COUNT:
      DICT['mochila_'+str(i)].append(DICT['VALOR'].index(obj))
      return TRUE
    COUNT = 0

def resolve_instancia_for_folder(folder_in, folder_out):
  for file in os.listdir(folder_in):
    file_name_splited = file.split('.')
    resolve_instancia(folder_in+'/'+file,folder_out+'/'+file_name_splited[0]+'_solution.'+file_name_splited[1])

def resolve_instancia(arq_instancia, arq_solucao):
  DICT = {}
  DICT['ITEM'] = []
  DICT['PESO'] = []
  DICT['VALOR'] = []
  DICT['CAPACIDADES'] = []
  COUNT = sys.maxsize
  COUNT_2 = sys.maxsize
  with open(arq_instancia, 'r') as file:
    for row in file:
      split_row = row.strip('\n').split(';')
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
        for item_matrix_2 in range(1,int(DICT['QTD_ITENS'])+1,1):
          DICT[str(COUNT_2)].append(split_row[item_matrix_2])
        COUNT_2 += 1
    
  COUNT = sys.maxsize
  COUNT_2 = sys.maxsize

  for i in range(1,int(DICT['QTD_MOCHILAS'])+1):
    DICT['mochila_'+str(i)] = []

  nova_lista = DICT['VALOR'].copy()
  nova_lista.sort()
  nova_lista.reverse()

  for obj in nova_lista:
    for i in range(1,int(DICT['QTD_MOCHILAS'])+1):
      if not DICT['mochila_'+str(i)]:
        DICT['mochila_'+str(i)].append(DICT['VALOR'].index(obj))
        break
      else:
        if mochila_is_avaliable(obj, DICT):
          break
  
  for i in range(1,int(DICT['QTD_MOCHILAS'])+1):
    DICT['peso_mochila_'+str(i)] = 0
    DICT['valor_mochila_'+str(i)] = 0

  for i in range(1,int(DICT['QTD_MOCHILAS'])+1):
    for item_mochila in DICT['mochila_'+str(i)]:
      DICT['peso_mochila_'+str(i)] += int(DICT['PESO'][item_mochila])
      DICT['valor_mochila_'+str(i)] += int(DICT['VALOR'][item_mochila])

  for i in range(1,int(DICT['QTD_MOCHILAS'])+1):
    while DICT['peso_mochila_'+str(i)] > int(DICT['CAPACIDADES'][i-1]):
      DICT['mochila_'+str(i)].pop(-1)
      DICT['peso_mochila_'+str(i)] = 0
      for item_mochila in DICT['mochila_'+str(i)]:
        DICT['peso_mochila_'+str(i)] += int(DICT['PESO'][item_mochila])


  DICT['VALOR_TOTAL'] = 0
  for i in range(1,int(DICT['QTD_MOCHILAS'])+1):
    DICT['VALOR_TOTAL'] += DICT['valor_mochila_'+str(i)]

  for i in range(1,int(DICT['QTD_MOCHILAS'])+1):
    DICT['peso_mochila_'+str(i)] = str(DICT['peso_mochila_'+str(i)])

  with open(arq_solucao, 'w') as csv_file: 
    for key, value in DICT.items(): 
        csv_file.write('%s;%s\n' % (key, value))
