#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
#define ARRMAX 5
#define STRMAX 20

typedef char StrType[STRMAX];
/*This piece of code was taken from the /tmp directory from a file called fgets2*/ 
char* readStr(StrType name){
    char* retVal = fgets(name,STRMAX,stdin);
    char* nlPos;
    char c;
    if (retVal){
        nlPos = strchr(name,'\n');
        if (nlPos){
            *nlPos = '\0';
        }else{
            while ((c = getchar()) && c != '\n' && c != EOF);
        }
    }
    return retVal;
}
/*This piece of code was taken from the provided bubbleSort function in class*/
void bubbleSort(char name[ARRMAX][STRMAX]){
    int i;
    int j;
    StrType temp;
    for (i = 0;i<ARRMAX-1;i++){
        for (j = 0; j<ARRMAX-1;j++){
            if (abs(name[j][0] - 'A') > abs(name[j+1][0] - 'A')){
                strcpy(temp, name[j]);
                strcpy(name[j], name[j+1]);
                strcpy(name[j+1], temp);
            }
        }
    }
    return;
}

int main(){
    StrType inVal;
    int i = 0;
    char name[ARRMAX][STRMAX];
    while (i < ARRMAX && readStr(inVal)){
        strcpy(name[i], inVal);
        i++;
    }
    bubbleSort(name);
    for (i = 0; i <= strlen(name[i]); i++){
        if (name[i][0] != '\0'){
            printf("%s ", name[i]);
        }
    }
    printf("\n");
}