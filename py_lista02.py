# -*- coding: utf-8 -*-
#Lista de Exercícios 02 (Revisão - Strings)
#Alunos: Mayara Rysia e Kessivaldo

def removeEspacosAMais(nome):
  tam = len(nome)
  ini=0; final = tam-1
  nomeFormatado = ""
  
  while nome[ini]== " ": #remove os espaços da direita
    ini+=1
  while nome[final]== " ": #remove os espaços da esquerda
    final-=1
  i = ini
  
  while i <= final:
    if nome[i] == " ":
      ant = i-1
      pos = i+1
      if nome[pos] == " " and nome[ant]!=" ": 
        nomeFormatado+=nome[i]
      if(nome[ant]!=" " and nome[pos]!=" "):
          nomeFormatado+=nome[i]
    else: nomeFormatado+=nome[i]
    i+=1

  return nomeFormatado

#questão 01
def palindroma(str):
  tam = len(str);
  i = 0; index = tam-1; cont = 0;
  
  while i < tam:
    if(str[i] == str[index]): cont+=1;
    index-=1;
    i+=1;
  
  if(cont == tam): print("\nPALINDROMA!");
  else: print("\nNÃO PALINDROMA!");

#questão 02
def contar_palavra(txt):
  tam = len(txt);
  i = 0; cont = 0;
  
  while i < tam:
    if(txt[i] == ' '): cont+=1;
    i+=1;
  if(txt[tam-1] != ' '): cont+=1;
  return cont;

#questão 03
def ultimaPalavra(stri):
  tam = len(stri);
  ultima = ""
  i = tam-1;
 
  while stri[i] !=' ':
    i-=1;
    if i == -1:  break
  
  i+=1
  if i == 0:
    print("Há apenas uma palavra!")
    return stri
  while i<tam:
    ultima+=stri[i]
    i+=1;
  return ultima
  
#questão 04
def formato(nome):
  string = removeEspacosAMais(nome)
  tam = len(string);
  i = tam-1; j = 0;
  nomeFormatado = "";
  
  while string[i] !=' ':
    j+=1;
    i-=1;
    if i == -1: break
    
  j = tam - j;
  
  while j<tam: 
    nomeFormatado+= string[j];
    j+=1;
    
  nomeFormatado+='/';
  
  if i == -1: return nomeFormatado
  i=0;
  
  while string[i] !=' ':
    nomeFormatado+= string[i];
    i+=1;
  return nomeFormatado;

#questão 05
def formatoBibli(nome):
  vetorNomes = []; vetorPosicaoEspaco = [];
  i=0; j = 0;

  string = removeEspacosAMais(nome)
  tamNome=len(string);
  
  while i<tamNome:
    if(string[i]==" "):
      vetorPosicaoEspaco.append(i)
    i+=1;
    
  i=0
  tam = len(vetorPosicaoEspaco)
  
  while(i<tam):
    aux = ""
    while j < vetorPosicaoEspaco[i]:
      aux += string[j]
      j+=1
    vetorNomes.append(aux)
    j = vetorPosicaoEspaco[i] + 1
    i+=1
    
  if(string[j] != ' '):
    aux = ""
    while j < tamNome:
      aux += string[j]
      j+=1
    vetorNomes.append(aux)
  
  tam = len(vetorNomes)
  i = 0
  uppercase = []
  
  while i < tam-1:
    letra = vetorNomes[i]
    uppercase += [letra[0].upper()]
    i += 1
  
  formato="";
  aux="";
  aux += vetorNomes[tam-1]
  formato += aux[0].upper()
  tam = len(aux)
  i=1
  
  while i<tam:
    formato += aux[i]
    i+=1
  formato+=',' + ' '
  tam = len(uppercase)
  i = 0
  
  while(i<tam):
    formato+=uppercase[i] + '.' + ' '
    i+=1
  return formato

#questão 06
def formatoEspaco(palavra):
    string =  removeEspacosAMais(palavra)
    formato = ""
    for caracter in string:
      if caracter != ' ':
        formato+=caracter.upper() + ' '
    return formato
    
#questão 07
def login(nome):
    string  = removeEspacosAMais(nome)
    nickname = ""
    for caracter in string:
      if caracter != ' ':
        nickname+=caracter
    return nickname
    
#questão 08
def substitui(frase, palavra, palavra2):
  vetorNomes = []
  string = removeEspacosAMais(frase)
  tam = len(string)
  i=0
 
  while(i<tam):
    j=i
    aux = ""
    while string[j] != ' ':
      aux += string[j]
      j+=1
      if j == tam: break
     
    vetorNomes.append(aux)
    i=j
    i+=1
    
  i=0
  string=""
  flag = 0
  
  for nome in vetorNomes:
    if(nome == palavra):
      flag = 1
      vetorNomes[i] = palavra2
    string+=vetorNomes[i] + " "
    i+=1
    
  if(flag == 0): print("\nPalavra Não Encontrada!")
  return string
	
def main():
  #01
  print('\n---01---\n')
  palavra = (input('Insira Uma Palavra: '))
  palindroma(palavra)
  #02
  print('\n---02---\n')
  txt = (input('Insira Um Texto: '))
  print(contar_palavra(txt), "Palavras")
  #03
  print('\n---03---\n')
  string = (input('Insira Uma String: '))
  print("Substring: ", ultimaPalavra(string))
  #04
  print('\n---04---\n')
  nome = (input('Insira um Nome: '))
  print(formato(nome))
  #05
  print('\n---05---\n')
  nome = input("Insira um nome: ")
  print("Formato de Bibliografia: ", formatoBibli(nome))
  #06
  print('\n---06---\n')
  palavra = input("Insira uma palavra de um documento: ")
  print(formatoEspaco(palavra))
  #07
  print('\n---07---\n')
  name = removeEspacosAMais(nome)
  print("Nome: ", name)
  print("Login: ", login(name))
  #08
  print('\n---08---\n')
  frase = input("Digite uma frase: ")
  palavra = input("Que palavra você deseja substituir ? ")
  palavra2 = input("Palavra substituta: ")
  print("Frase: ", substitui(frase, palavra, palavra2))
  print("FIM")
  
if __name__ == "__main__":
   main()