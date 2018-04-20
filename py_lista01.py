# -*- coding: utf-8 -*-
#Lista de Exercícios 01 (Revisão - Funções)
import math as matematica

#questão01
def fatorial(n):
  if n == 1 or n == 0:
    return 1
  else:
    return n * fatorial(n-1)
#questão02
def eh_par(n):
  if(n%2 == 0):
   return 1;
  return 0;
  
#questão03
def par_ou_impar(num):
  if(eh_par(num)):
    return "par";
  return "ímpar";

#questão04
def compare(a,b):
  if(a>b):
    return 1;
  if(a == b):
    return 0;
  if(a<b):
    return -1;
    
#questão05
def maior_de_2(num1, num2):
  if(num1>num2):
    return num1;
  return num2;

#questão06
def maior_de_3(num1, num2, num3):
  maior = num1;
  if(num2>maior):
    maior = num2;
  if(num3>maior):
    maior = num3;
  return maior;

#questão07
def dia_da_semana(dia):
  if(dia>=1 and dia <=7):
    if(dia == 1):
      return "Domingo"
    if(dia == 2):
      return "Segunda"
    if(dia == 3):
      return "Terça"
    if(dia == 4):
      return "Quarta"
    if(dia == 5):
      return "Quinta"
    if(dia == 6):
      return "Sexta"
    if(dia == 7):
      return "Sábado"
  return "Dia Inválido!"  

#questão08
def hipotenusa(cateto1, cateto2):
  cateto1 = cateto1**2
  cateto2 = cateto2**2
  h = cateto1+cateto2
  h = matematica.sqrt(h)
  return h
  
#questão 09
def eh_bissexto(ano):
  if(ano%400 == 0):  return True;
  elif(ano%4 == 0 and ano%100!=0): return True;
  return False;

#questão 10
def eh_data_valida(dia, mes, ano):
  if((dia<=31 and dia>=1) and (mes<=12 and mes>=1)):
      if(ano<=2018 and ano>=1): return True
  return False

#questão 11
def soma_numeros(numero):
  if(numero>=1):
    return numero + soma_numeros(numero-1)
  return 0

#questão 12
def eh_primo(numero):
  n = numero;
  cont = 0;
  while n>1:
    if (numero%n == 0): cont+=1
    n-=1
  if(cont == 1): return True
  return False

#questão 13
def Fibonacci(termo):
  soma = 0; cont=1; aux=0; i = 0;
  j=1;
 
  while cont < termo:
    aux = i + j;
    i = j;
    j = aux;
    soma+=i;
    cont+=1;
  return soma;
  
def main():
  #1
  num = int(input('Insira Um Número: '))
  print("Fatorial: ", fatorial(num))
  print("---")
  #2
  print("Número ", num)
  if(eh_par(num)): print("True")
  else: print("False")
  print("---")
  #3
  print("Número ", num)
  print(par_ou_impar(num))
  print("---")
  #4
  a = int(input('Insira Um Número: '))
  b = int(input('Insira Outro Número: '))
  print("Comparação:  ", compare(a, b))
  print("---")
  #5
  print("O maior: ", maior_de_2(a, b))
  print("---")
  #6
  num1 = int(input('Insira o Primeiro Número: '))
  num2 = int(input('Insira o Segundo Número: '))
  num3 = int(input('Insira o Terceiro Número: '))
  print("O maior: ", maior_de_3(num1, num2, num3))
  print("---")
  #7
  print("1-Dom")
  print("2-Seg")
  print("3-Ter")
  print("4-Quar")
  print("5-Quin")
  print("6-Sex")
  print("7-Sáb")
  dia = int(input('Insira um número correspondente ao dia da semana: '))
  print(dia_da_semana(dia))
  print("---")
  
  #8 
  a = int(input('Insira o comprimeito a do triângulo:'))
  b = int(input('Insira o comprimeito b do triângulo:'))
  print("Hipotenusa: ", hipotenusa(a, b))
  print("---")
  
  #09
  ano = int(input('Insira um ano:'))
  print("É bissexto? ", eh_bissexto(ano))
  print("---")
  
  #10
  dia = int(input('Insira o dia:'))
  mes = int(input('Insira o mês:'))
  ano =  int(input('Insira o ano:'))
  print("Data válida? ", eh_data_valida(dia, mes, ano))
  print("---")
  
  #11
  N = int(input('Insira um número:'))
  print('Número: ', N)
  print('Soma de: ', soma_numeros(N))
  print("---")
  
  #12
  print("O número ", N)
  print("É primo? ", eh_primo(N))
  print("---")
  
  #13
  print("Fibonnaci - Termo: ", N)
  print("Soma dos termos: ", Fibonacci(N))
  print("---")
 
if __name__ == "__main__":
   main()


