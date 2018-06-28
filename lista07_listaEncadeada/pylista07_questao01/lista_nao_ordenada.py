from Noh import *

class ListaEncadeada:
  def __init__(self): #construtor
    self.head = None
    self.final = None
    
  def append(self, item):
    temp = Noh(item)
    if self.head == None:
      temp.setNext(self.head)
      self.head = temp
    if self.final == None: 
      self.final = self.head
    else:
      self.final.setNext(temp)
      self.final = temp

  def insert(self, posicao, item): #Insere em uma posicao x
    temp = Noh(item)
    tamanho = self.size()
    if not self.isEmpty():
      if posicao == 0:
        ant = self.head
        self.head = temp
        temp.setNext(ant)
      if posicao > (tamanho-1) and posicao == tamanho:
        ant = self.final
        ant.setNext(temp)
        self.final = temp
      else:
        ant = self.percorre(posicao)
        temp.setNext(ant.getNext())
        ant.setNext(temp)
    else: raise Exception('A Lista está vazia!')

  def percorre(self, posicao):
    if self.isEmpty(): raise Exception('A Lista está vazia!')
    count = 1
    atual = ant = self.head
    while count <= posicao:
      ant = atual
      if count == posicao:
        return ant      
      atual = atual.getNext()
      count = count+1
    return ant

  def pop(self): #elimina o último elemento
    if self.isEmpty(): raise Exception('A Lista está vazia!')
    ant = self.percorre(self.size()-1)
    ant.setNext(None)
    self.final = ant
  
  def isEmpty(self):
    return self.head == None    

  def size(self):
    atual = self.head
    contador = 0
    while atual != None:
      contador = contador + 1
      atual = atual.getNext()
    return contador

  def remove(self, item):
    atual = self.head
    anterior = None
    encontrou = False
    while not encontrou: #percorre a lista
      if atual.getData() == item:
        encontrou = True
      else:
        anterior = atual
        atual = atual.getNext()
    if anterior == None:
      self.head = atual.getNext()
    else:
      anterior.setNext(atual.getNext())

  def print_(self):
    if self.isEmpty():
      print("Lista Vazia!")
    else:
      aux = self.head
      while aux.getData()!= None:       
        print(aux.getData())
        if aux.getNext() == None: break
        aux = aux.getNext()