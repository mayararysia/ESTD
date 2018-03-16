#include<stdio.h>
#include<stdlib.h>
/*
	Name: Estrutura de Dados 2018-1
	Author: Mayara Rysia
*/

typedef struct data{
	int dia;
	int mes;
	int ano;
}Data;

 
void print(Data data, Data user){
	int idade_, flag_data, flag_user;
	
	idade_ = idade(user.ano, data.ano);
	flag_data = validacao(data);
	flag_user = validacao(user);
	
	if(flag_data && flag_user){	
		printf("\n\n");
		printf("\nData de Nascimento: %d / %d / %d ", user.dia, user.mes, user.ano);
		printf("\nIdade: %d \n", idade_);
	}else printf("\nDados Invahlido! Tente novamente!");
}

int idade(int ano_nasc, int data_atual){
	return data_atual-ano_nasc;	
}

int validacao(Data type){
	
	if(type.dia <= 0 || type.dia > 31) return 0;
	
	if(type.mes <= 0 || type.mes > 12) return 0;
	
	if(type.ano <= 0 || type.ano > 2018) return 0;
	
	return 1;
}

main(){
	Data data_atual, user;
	
	printf("\nInsira  a data atual (dia mes e ano): ");
	scanf("%d%d%d", &data_atual.dia, &data_atual.mes, &data_atual.ano);
	
	printf("\nInsira  a data do seu nascimento (dia mes e ano): ");
	scanf("%d%d%d", &user.dia, &user.mes, &user.ano);	
	print(data_atual, user);	
}
