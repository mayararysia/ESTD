# -*- coding: utf-8 -*-
#fila.py
#Mayara Rysia

class Fila:
  def __init__(self):
    self._dados = [None]
    self._inicio = 0
    self._tamanho = 0

  def enqueue(self, e): #insere
    disponivel = self._tamanho
    if self._dados[disponivel] == None:
      self._dados[disponivel] = e
      #self._dados.append(None)
    self._tamanho += 1
    self._aumenta_tamanho(self._tamanho+1)
  

  def _aumenta_tamanho(self, novo_tamanho):
    dados_antigos = self._dados
    self._dados = [None] * novo_tamanho
    for i in range(self._tamanho):
      self._dados[i] = dados_antigos[i]

  def dequeue(self): #remove
    if self.is_empty():
      raise Exception('A Fila está vazia')
    result = self._dados[self._inicio]
    del self._dados[self._inicio]
    self._tamanho -= 1
    return result 

  def __len__(self): #retorna tamanho
    return self._tamanho

  def is_empty(self): #vazia
    return self.__len__() == 0
  
  def first(self):
    if self.is_empty():
      raise Exception('A Fila está vazia')
    return self._dados[self._inicio]
  
  def get(self):
    if self.is_empty():
      raise Exception('A Fila está vazia')
    aux = []
    for e in self._dados:
      if e!= None: aux.append(e)
    return aux