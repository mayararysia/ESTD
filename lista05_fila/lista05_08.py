# -*- coding: utf-8 -*-
#Lista05 - Fila - Questão 08 
#Mayara Rysia
"""
8. Em certas aplicações do TAD fila, é comum repetidamente realizar dequeue e então, imediamente, realizar enqueue com o
mesmo elemento. Modifique a implementação FilaArray para incluir um método rodar() que deve ser semanticamente
identifico a f.enqueue(f.dequeue) . Assegure que sua implementação do método rodar seja mais eficiente do que a
chamada separada para f.enqueue(f.dequeue) .
"""
class FilaArray:
  CAPACIDADE_PADRAO = 5

  def __init__(self):
    self._dados = [None] * FilaArray.CAPACIDADE_PADRAO
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
    if self._tamanho == len(self._dados):
      self._aumenta_tamanho(2 * len(self._dados))
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

  def rodar(self):
    self.enqueue(self.dequeue())

  def get(self):
    if self.is_empty():
      raise Exception('A Fila está vazia')
    aux = []
    for e in self._dados:
      if e!= None: aux.append(e)
    return aux
    
if __name__ == '__main__':
  f = FilaArray()
  n=5
  for i in range(3):
    f.enqueue(n)
    n+=1
  print(f.get())
  f.rodar() 
  print(f.get())

