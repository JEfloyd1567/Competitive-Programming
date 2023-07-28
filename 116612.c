#include<stdio.h>
#include<stdlib.h>
#include<string.h>
int main(){
	int i=0,casos=0,subcasos=0,longitud=0,pasos=0,cont=0,j=0;
    scanf("%d",&longitud);
	char carretera[longitud];
	while(scanf("%d",&pasos)){
		if(pasos==0){
			break;
			return 0;
		}
		for(i=0;i<pasos;i++){
			scanf("%s",&carretera[i]);
		}
		for(j=0;j<pasos;j++){
			if(carretera[j]=='.'){
				cont++;
				j++;
			}
			if(carretera[j]=='R'){
				cont++;
				j++;
	 	    }
			if(carretera[j]=='Z'){
				cont++;
				j++;
			}
			if(carretera[j]=='D'){
				cont++;
				j++;
			}
	    }
    }
	printf("%d\n",cont);			
}


