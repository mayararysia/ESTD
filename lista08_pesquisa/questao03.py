# -*- coding: utf-8 -*-
#Lista de Exercícios 08 (Pesquisa) - Questão 03
#Mayara Rysia
from time import time
from time import sleep
from random import randint
"""
03.
Implemente a busca binária usando recursividade sem o operador slice. Lembre-se
que voce precisará passar o índice dos valores iniciais e finais na sublistas. Gere
uma lista de números aleatórios, ordene-os e verifique o desempenho.
"""

#Busca Binária com slice
def busca_binaria(uma_lista, item_procurado):
  if len(uma_lista) == 0:
    return False
  meio = len(uma_lista)//2
  if uma_lista[meio] == item_procurado:
    return True
  if item_procurado < uma_lista[meio]:
	return busca_binaria(uma_lista[:meio], item_procurado)
  else:
    return busca_binaria(uma_lista[meio+1:], item_procurado)

def sub(lista, inicio, fim):
  sub = []
  if len(lista) != 2:
    fim += 1
  for i in range(inicio, fim):
    sub.append(lista[i])
  return sub

#Busca Binária sem slice
def busca_binaria_noSlice(uma_lista, item_procurado):
  
  if len(uma_lista) == 0: return False
  meio = len(uma_lista)//2
  fim = len(uma_lista)-1

  if uma_lista[meio] == item_procurado:
    return True
  if len(uma_lista) == 1:
    return False
  if item_procurado < uma_lista[meio]:
    uma_lista = sub(uma_lista, 0, meio)
  else:
    uma_lista = sub(uma_lista, meio, fim)
  return busca_binaria_noSlice(uma_lista, item_procurado)

#cria a lista
def criaLista():
  lista = []
  for i in range(9):
    num = randint(0, 42)
    lista.append(num)
  return lista

#ordena a lista
def ordena(lista):
  
  quant = tam = len(lista)
  continua = True

  while quant>=1 and continua:
    continua = False
    for i in range(tam):
      j=i+1
      
      if j != tam and lista[i] > lista[j]:
        continua = True
        ant = lista[i]
        lista[i] = lista[j]
        lista[j] = ant
      i=j    
    quant-=1

  return lista

#com slice
def Teste(lista, num):
  print('Procurando ', num,'na lista', lista)
  inicio = time()
  result = busca_binaria(lista, num)
  fim = time()
  tempo_gasto = fim-inicio
  print('resultado', result)

  return tempo_gasto

#sem slice
def Teste02(lista, num):
  print('Procurando ', num,'na lista', lista)
  inicio = time()
  result = busca_binaria_noSlice(lista, num)
  fim = time()
  tempo_gasto = fim-inicio
  print('resultado', result)

  return tempo_gasto


if __name__ == '__main__':

  l = criaLista()
  lista = ordena(l)
  qtd_cs = qtd_ss = 0

  #Testes
  for i in range(5):

    num = randint(0, 42)

    print("<< Busca Recursiva Com Slice >> \n")
    tempo_gasto_cs = Teste(lista, num)
    print('\ttempo gasto: ', tempo_gasto_cs)
    print('\n\n')

    sleep(2)

    print("<< Busca Recursiva Sem Slice >> \n")
    tempo_gasto_ss = Teste02(lista, num)
    print('\ttempo gasto: ', tempo_gasto_ss)
    print('\n\n')

    if tempo_gasto_cs < tempo_gasto_ss:
      qtd_cs +=1
      print('\n-> Busca Recursiva Com Slice levou o menor tempo\n')   
    else:
      qtd_ss +=1
      print('\n-> Busca Iterativa Sem Slice levou o menor tempo\n')
    
    print("------- ------- ------- ------- -------")

  print("\nCONCLUSÃO\n\n ")
  if qtd_cs > qtd_ss:
    print("Busca Binária Recursiva Com Slice teve o melhor desempenho!")
  else:
    print("Busca Binária Recursiva Sem Slice teve o melhor desempenho!")

  print("Quantidade Binária Recursiva Com Slice: ", qtd_cs)
  print("Quantidade Binária Recursiva Sem Slice ", qtd_ss)