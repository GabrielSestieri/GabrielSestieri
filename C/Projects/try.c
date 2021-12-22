#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#define STRMAX 10
#define INVMAX 20 

typedef char StrType[STRMAX];
typedef char NameArrType[STRMAX][INVMAX];
typedef float CostArrType[INVMAX];

void  fill(CostArrType cost, NameArrType name, FILE *fileName){
	int i;
   	for (i = 0; i < STRMAX; i++){
		if (fscanf(fileName,"%f %s", &cost[i], &name[i])>2){
			printf("ERROR: bad input\n");
			exit(EXIT_FAILURE);
		}
   	}
}

void  fillOrder(CostArrType quantity, NameArrType product, FILE *fileName){
	int i;
   	for (i = 0; i < STRMAX; i++){
		if (fscanf(fileName,"%s\n%f", &product[i], &quantity[i])>2){
			printf("ERROR: bad input\n");
			exit(EXIT_FAILURE);
		}
    }
}

void bubbleSort(CostArrType cost, NameArrType name){
    int i;
    int j;
    float tempp;
    StrType temp;
    for (i = 0;i<STRMAX-1;i++){
        for (j = 0; j<STRMAX-1;j++){
            if (abs(name[j][0] - 'A') > abs(name[j+1][0] - 'A')){
                strcpy(temp, name[j]);                
                tempp = cost[j];
                strcpy(name[j], name[j+1]);
                cost[j] = cost[j + 1];
                strcpy(name[j+1], temp);
                cost[j+1] = tempp;
            }
        }
    }
    return;
}

void printArr(CostArrType cost, NameArrType name){ 
    int i;
    for (i = 0; i < STRMAX-1; i++){
        printf("%s ", name[i]);
        printf("[$%.2f]\n", cost[i]);
        }
    printf("\n");
}

float printOrder(CostArrType quantity, NameArrType product, CostArrType cost, amt){ 
    int i;
    float total;
    for (i = 0; i < strlen(product)-2; i++){
        printf("%.0f %s [$%.2f] = %f \n", quantity[i], product[i], cost[i], amt);
        if (total < amt){
            total += amt;
        }
        /*printf("%s: ", product[i]);
        printf("%.0f\n", quantity[i]);*/
        }
    printf("\n");
    printf("Total: %f", total);
}

int main(){
   	FILE * inFile = NULL;
   	FILE * orderFile = NULL;
    FILE * receiptFile = NULL;
    NameArrType name;
   	CostArrType cost;
    double amt = 0.0;
    int i;
    NameArrType product;
    CostArrType quantity;

    char ordername[STRMAX];
   	inFile = fopen ("inventory1.txt","r");
   	if (inFile == NULL){
		printf("Error opening file named intInput.txt\n");
        	exit(EXIT_FAILURE);
   	}
	fill(cost, name,inFile);
   	printf("INVENTORY LIST: \n");
   	printArr(cost,name);
    printf("SORTED INVENTORY LIST: \n");
    bubbleSort(cost, name);
    printArr(cost,name);

    printf("Enter order name:\n");
    scanf("%s",&ordername);
    orderFile = fopen(&ordername, "r");   
    if (orderFile == NULL){
		printf("Error opening file named intInput.txt\n");
        exit(EXIT_FAILURE);
   	}
    fillOrder(quantity, product, orderFile);
    printf("YOUR ORDER: \n");
    amt = quantity[i]*cost[i];
    printOrder(quantity, product, cost, amt);
    
    
    
	
   	return 0;
}
