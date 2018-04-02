#include<stdio.h>
#include<stdlib.h>
#include<conio.h>
#include<string.h>
/*
	Name: Primeiro Exercício sobre Strings
	Author: Mayara Rysia
	Date: 28/03/18 10:45
	Description: 
	
		Faça um programa que contenha um menu e funções que atendam os seguintes requisitos:
			a) Ler uma string S1 (tamanho máximo 20 caracteres);
			b) Imprimir o tamanho da string S1;
			c) Comparar a string S1 com uma nova string S2 fornecida pelo usuário e imprimir o resultado da
			comparação;
			d) Concatenar a string S1 com uma nova string S2 e imprimir na tela o resultado da concatenação;		
			e) Imprimir a string S1 de forma reversa;		
			f) Contar quantas vezes um dado caractere aparece na string S1. Esse caractere desse ser
			informado pelo usuário;		
			g) Substituir a primeira ocorrência do caractere C1 da string s1 pelo caractere C2. Os caracteres C1
			e C2 serão lidos pelo usuário;
			
			h) Verificar se uma string s2 é substring de s1. A string s2 deve ser informada pelo usuário;
			
			i) Retornar uma substring da string s1. Para isso o usuário deve informar a partir de qual posição
			deve ser criada a substring e qual é o tamanho da substring.
			
		OBS.:
		Repositório público da aluna: https://github.com/mayararysia/ESTD
		Ambiente de Desenvolvimento: Dev-C++ 5.11.
*/

//protótipos:
void limpa_tela(void);
int tamanho(char[]);
int compara(char[], char[]);
void concatena(char[], char[]);
void reverte(char[]);
void substring(char[], char[], int, int);
int validaStr(char[]);

int main(){
	
	char S1[21] = "", S2[21] = "", sub[21] = "", str_concatenada[41] = "";
	char caracter, opcao;
	char C1, C2;
	
	int tam, tam2, result, str1_comp, str2_comp;
	int  i, j, flag, cont = 0;
	int posicao, length;
	
	
	do{
		printf("\n\t\t<< MENU DE OPCOES >>\n\n");
		printf("a - Ler uma String;\n\n");
		printf("b - Imprimir o tamanho da string;\n\n");
		printf("c - Comparar Strings;\n\n");
		printf("d - Concatenar Strings;\n\n");
		printf("e - Inverter String;\n\n");
		printf("f - Contar Ocorrencia de Um Caractere na String;\n\n");
		printf("g - Substituir Caractere;\n\n");
		printf("h - Verificar se String eh Substring;\n\n");
		printf("i - Retornar uma Substring da String;\n\n");
		printf("X - SAIR DO MENU.\n\n");
		printf("OPCAO: ");
		scanf(" %c", &opcao);
	
		switch(opcao) {
			case 'a':
				printf("\nInsira uma string: ");
				scanf("%s", &S1);
				break;
			case 'b':
				tam = tamanho(S1);
				printf("\nTamanho da string: %d", tam);
				getch();
				break;
			case 'c':
				if(validaStr(S1)){				
					printf("\nInsira uma nova string: ");
					scanf("%s", &S2);
					
					result = compara(S1, S2);
						
					printf("\nResultado da Comparacao: %d", result);
				}else
					printf("\nInsira a string S1!\n");
				getch();
				break;
			case 'd':
				str1_comp = compara(S1, "");
				str2_comp = compara(S2, "");
				
				if(str1_comp!=0 && str2_comp!=0){				
					strcpy(str_concatenada, S1);
					concatena(str_concatenada, S2);
					
					printf("\nConcatenacao: %s", str_concatenada);
				}else
					printf("\nString(s) vazia(s)!");
				getch();
				break;
			case 'e':
				if(validaStr(S1))
					reverte(S1);
				else
					printf("\nInsira a string S1!\n");
				getch();
				break;
			case 'f':
				if(validaStr(S1)){
					
					printf("\nInsira um caractere: ");
					scanf(" %c", &caracter);
					
					tam = tamanho(S1);
					
					for(i = 0; i < tam; i++)
						if(S1[i] == caracter) 
							cont++;
					printf("\nO caractere '%c' aparece %d vezes em '%s'.", caracter, cont, S1);
				}else
					printf("\nInsira a string S1!\n");
				getch();
				break;
			case 'g':				
				if(validaStr(S1)){
				
					tam = tamanho(S1);
					printf("\nInsira um caracter para C1: ");
					scanf(" %c", &C1);
					
					printf("\nInsira um caracter para C2: ");
					scanf(" %c", &C2);
					
					for(i = 0; i < tam; i++){	
						if(S1[i] == C1){
							S1[i] = C2;
							break;
						}
					}
					printf("\nString: %s ", S1);
				}else
					printf("\nInsira a string S1!\n");
					
				getch();
				break;
			case 'h':
				
				if(validaStr(S1)){				
				
					printf("\nInsira a string S2: ");
					scanf("%s", &S2);
					
					tam2 = tamanho(S2);
					tam = tamanho(S1);
					cont = 0;
					
					if(tam2 <= tam){
						for(i = 0; i <tam; i++){
							flag = 0;
							for(j = 0; j < tam2; j++){
								if(S1[i] == S2[j]) flag = 1;
							}
							if(flag == 1) 
								cont++;
						}
						if(cont == tam2) 
							printf("\n'%s'  eh substring de '%s'.", S2, S1);
						else 
							printf("\n'%s' nao eh substring de '%s'.", S2, S1);
					}else 
						printf("\n'%s' nao eh substring de '%s'.", S2, S1);
				}else
					printf("\nInsira a string S1!\n");
				getch();
				break;
			case 'i':
   				
   				if(validaStr(S1)){
   					
   					tam = tamanho(S1);
   					
				   	printf("\nEntre com a posicao e tamanho da substring:\n");
   					scanf("%d%d", &posicao, &length);
   					
   					if(posicao<=tam || length > tam) {
	
						substring(S1, sub, posicao, length);						
						printf("\nA substring eh:  %s \n", sub);
						
					} else 
						printf("\nPosicao ou tamanho pedido ultrapassa a string!\n");
				}else 
					printf("\nInsira a string S1!\n");
				getch();
				break;
			case 'x':
				exit(0);
				break;
			case 'X':
				exit(0);
				break;		
			default:
				printf("\n\nOPCAO INVALIDAH!");
				getch();
		}
		limpa_tela();
	}while(opcao!='x' || opcao!='X');
		
	return 0;
}//fim do main

//funções:

void limpa_tela(void){
    system("cls");
}

int tamanho(char string[]){		
	return strlen(string);
}

int compara(char str1[], char str2[]){	
	return strcmp(str1, str2);	
}

void concatena(char string_destino[], char string_origem[]){
 	strcat(string_destino, string_origem);
}

void reverte(char string[]){	
	int i, tam;	
	tam = tamanho(string);
	printf("\n");
	for(i = tam-1; i >= 0; i--)
		printf("%c", string[i]);
}

void substring(char str[], char sub[], int posicao, int tam){
	int index = 0;
 
    while (index < tam) {
      sub[index] = str[posicao];
      index++;
      posicao++;
    }
    sub[index] = '\0';
}

int validaStr(char str[]){
	int tam;
	
	tam = tamanho(str);
	
	if(tam > 1 && str[0] != "") return 1;
	
	return 0;
}



