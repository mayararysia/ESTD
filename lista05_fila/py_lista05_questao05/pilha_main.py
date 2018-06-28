# -*- coding: utf-8 -*-
#pilha_main.py
#Mayara Rysia
from fila_array import *

class PilhaVazia(Exception):
  pass

class PilhaArray:	
  def __init__(self):
	  self._dados = Fila()

  def size(self):
    return self._dados.__len__()

  def is_empty(self):
    return self._dados.is_empty()
    
  def push(self, e):
    self._dados.enqueue(e)

  def top(self):
    if self.is_empty():
      raise PilhaVazia('A pilha está vazia!')
    aux = self._dados.get()
    return aux[-1]

  def pop(self):
    if self.is_empty():
      raise PilhaVazia('Está vazia!')
    aux = []
    while not self.is_empty():
      aux.append(self._dados.dequeue())
    for e in aux:
      if e != aux[-1]: self.push(e)
    return aux[-1]

  def get(self):
    return self._dados.get()

if __name__ == '__main__':
  p = PilhaArray()
  print("---LIFO---\n ")
  try:
    p.pop()
    p.is_empty()
    p.get()
  except Exception:
    print("Pilha vazia!")
  p.push(5)            # conteúdo [5]
  p.push(3)            # conteúdo [5, 3]
  p.push(4)            # conteúdo [5, 3, 4]
  p.push(5)# conteúdo [5, 3, 4, 5]
  p.push(6)# conteúdo [5, 3, 4, 5, 6]
  p.push(7)# conteúdo [5, 3, 4, 5, 6, 7]
  print(p.get())
  print("pop: ", p.pop()) # retorna 7
  print(p.size())     #retorna 5
  print(p.is_empty()) #retorna False
  print("pop: ", p.pop()) # retorna 6;
  print(p.is_empty())  #False
  print(p.get())
  print("topo: ", p.top())# retorna 5;
  p.push(4) # conteúdo [5, 3, 4, 5,4]
  print(p.size())      # retorna 5;
  print(p.get())
  print("pop: ", p.pop())     # retorna 4;
  p.push(6)            # conteúdo [5, 3, 4, 5,6]
  p.push(8)            # conteúdo [5, 3, 4, 5,6, 8]
  print(p.get())
  print("pop: ", p.pop())   # retorna 8
  print("PILHA: ", p.get())

  """
  Avaliação do Desempenho:
  Operação:   Tempo de Execução:
  p.push(e)   O(n)
  p.pop()     O(n)
  p.top()     O(1)
  """
