#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#define STRMAX 10
#define INVMAX 20 

typedef char StrType[STRMAX];
typedef char NameArrType[STRMAX][INVMAX];
typedef int CostArrType[INVMAX];

void printArr(CostArrType cost){ 
  int i;
  for (i = 0; i < INVMAX; i++){
     /*printf("%f ",cost[i]);*/
    printf("%d",cost[i]);
  }
  printf("\n");
}

int main(){
    NameArrType name;
    CostArrType cost;
    int i;
    FILE * inFile = NULL;
    inFile = fopen ("inv1.txt","r");
   	if (inFile == NULL){
		printf("Error opening file named intInput.txt\n");
        exit(EXIT_FAILURE);
   	}
   	for (i = 0; i < INVMAX; i++){
		if(fscanf(inFile,"%d",&cost[i])!=1){
            printf("%d", cost[i]);
			printf("ERROR: bad input\n");
			exit(EXIT_FAILURE);
		}
   	}
	fclose(inFile);
    printArr(inFile);
    return 0;
}

