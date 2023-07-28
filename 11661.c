#include<stdio.h>
#include<stdlib.h>
#include<string.h>
int main(){
	int casos=0,subcasos=0,cont=0,cont2=0,i=0,j=0;
	char carretera[2000000];
	scanf("%d",&casos);
	while(scanf("%s",carretera[i])){
		subcasos=0;
		cont=0;
		cont2=0;
		i=0;
		j=0;
		if(casos==0){
			break;
			return 0;
		}
		scanf("%d",&subcasos);
			for(i=0;i<subcasos;i++){
				scanf("%s",carretera[i]);
				while(j<subcasos){
					if(carretera[j]==82){
						cont++;
					}
					else if(carretera[j]==90){
						cont++;
				   }
					else if(carretera[j]==68){
						cont++;
				   }
				   else if(carretera[j]==254){
				   	    j++;
				   }
			}
		}
			printf("%d",cont);
	}
}

