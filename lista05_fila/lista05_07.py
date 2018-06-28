# -*- coding: utf-8 -*-
#Lista05 - Fila - Questão 07 
#Mayara Rysia
"""
07.
Modifique a implementação FilaArray para que a capacidade da fila seja limitada a um parâmetro informado no construtor.

Se enqueue for chamado quando a fila estiver cheia, lance a exceção FilaCheia.

"""
class FilaArray:
  def __init__(self, CAPACIDADE):
    self._capacidade = CAPACIDADE
    self._dados = [None] * self._capacidade
    self._tamanho = 0
    self._inicio = 0

  def __len__(self):
    return self._tamanho

  def is_empty(self):
      return self._tamanho == 0

  def first(self):
    if self.is_empty():
      raise Exception('A Fila está vazia')
    return self._dados[self._inicio]


  def dequeue(self):
    if self.is_empty():
      raise Exception('A Fila está vazia')
    result = self._dados[self._inicio]
    self._dados[self._inicio] = None
    self._inicio = (self._inicio + 1) % len(self._dados)
    self._tamanho -= 1
    return result

  def enqueue(self, e):
    #se chegou no limite da capacidade do array
    if self._tamanho == self._capacidade:
      raise Exception('Fila Cheia!')

    disponivel = (self._inicio + self._tamanho) % len(self._dados)
    self._dados[disponivel] = e
    self._tamanho += 1  

  def _aumenta_tamanho(self, novo_tamanho):
    dados_antigos = self._dados
    self._dados = [None] * novo_tamanho
    posicao = self._inicio
    for k in range(self._tamanho):
      self._dados[k] = dados_antigos[posicao] 
      posicao = (1 + posicao) % len(dados_antigos)
    self._inicio = 0

  def get(self):
    if self.is_empty():
      raise Exception('A Fila está vazia')
    aux = []
    for e in self._dados:
      if e!= None: aux.append(e)
    return aux
    
if __name__ == '__main__':

  f = FilaArray(5) 
  n=50
  try:
    for i in range(7):
      f.enqueue(n+i)
  except Exception:
      print("Fila cheia!")
  print("Fila: ", f.get())