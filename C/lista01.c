#include "stdio.h"
#include "string.h"

//Lista de Exercícios 01 (Revisão - Funções)

//questão01
int fat(int n){
    if(n == 0 || n == 1) return 1;
    return n*fat(n-1);
}

//questão02
int eh_par(int num){
    if(num%2 == 0) return 1;
    return 0;
}

//questão03: string
/*
char* significa um ponteiro para algum lugar da memória que contém um ou  char (ou seja, uma String).
*/

char* par_ou_impar(int num){
    if(eh_par(num)) return "par";
    return "ímpar";
}

//questão 04
/*Escreva uma função compare(a, b) que recebe dois números a e b como parâmetro e retorna 1 se a > b, 0 se a
== b, e -1 se a < b.*/

int compare(int a, int b){
  if(a>b) return 1;
  if(a == b) return 0;
  if(a<b) return -1;
}

//questão 05
/*Faça uma função maior_de_2(num1, num2) que, dados dois números, retorna o maior deles.*/
int maior_de_2(num1, num2){
  if(num1>num2) return num1;
  return num2;
}

//questão 06
/*Faça uma função maior_de_3(num1, num2, num3)que, dados três números, retorna o maior deles.*/
int maior_de_3(num1, num2, num3){
  int maior = num1;
  if(num2>maior) maior = num2;
  if(num3>maior) maior = num3;
  
  return maior;
}

//questão 09
/*9. Faça uma função eh_bissexto(ano) que recebe um ano como parâmetro e retorna True se o ano for bissexto e
False caso contrário*/
int eh_bissexto(int ano){
  if((ano%4 == 0 || ano%400 == 0) && ano%100!=0) return 1;
  return 0;
}

//questão11
/*Faça uma função soma_numeros(numero) que recebe como parâmetro um número N, calcula a soma de todos
os números de 1 até ele e retorna o valor da soma. Exemplo: soma_numeros(7) = 28 , pois
1+2+3+4+5+6+7=28.*/
int soma_numeros(int numero){
  if(numero>1) return numero + soma_numeros(numero-1);
}

//questão 13
/*A sequência de Fibonacci é uma sequência de números inteiros, começando normalmente por 0 e 1, na qual,
cada termo subsequente corresponde a soma dos dois anteriores. Faça uma função Fibonacci(termo) que
dado um número N representando o n-ésimo termo da sequencia de Fibonacci, retorna a soma desses termos.

Exemplo: Fibonacci(7) = 20 , pois os 7 primeiros termos da sequencia de Fibonacci 
são “0,1, 1, 2, 3, 5, 8” e
sua soma é 20.*/

int Fibonacci(int termo){
  int sum = 0, cont=1, aux=0;
  int i = 0, j=1;
 
  while(cont < termo){
    aux = i + j;
    i = j;
    j = aux;
    sum+=i;
    cont++;
  }
  return sum;
}

main(){

    int num, fatorial;
    int n1, n2, ano;
    char*str;
    
    printf("\nInsira um numero: \n");
    scanf("%d", &num);

    fatorial = fat(num);

    printf("\nFatorial do numero: %d", fatorial);
    
    if(eh_par(num)) printf("\nTrue");
    else printf("\nFalse");
    
    str = par_ou_impar(num);
    
    printf("\nString: %s", str);
    
    printf("\nInsira dois numeros: \n");
    scanf("%d%d", &n1, &n2);
    
    printf("\n %d", compare(n1, n2));
    printf("\nMaior deles: %d", maior_de_2(n1, n2));
    
    printf("\nInsira 3 numeros: \n");
    scanf("%d%d%d", &n1, &n2, &num);
    
    printf("\nMaior deles: %d", maior_de_3(n1, n2, num));
    
    printf("\nInsira um ano: \n");
    scanf("%d", &ano);
    
    if(eh_bissexto(ano)) printf("\nTrue");
    else printf("\nFalse");
    
    printf("\nInsira um nuhmero: \n");
    scanf("%d", &num);

    printf("\nSOMA: %d", soma_numeros(num));
    printf("\nFIBONACCI: %d", Fibonacci(num));
    
}
