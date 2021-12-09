#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#define ARRMAX 5
#define STRMAX 20

typedef char StrType[STRMAX];

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
int main(){
    StrType inVal;
    int i = 0;
    int min;
    int index;
    char arr[ARRMAX][STRMAX];
    while (i < ARRMAX && readStr(inVal)){
        strcpy(arr[i], inVal);
        i++;
    }
    for (i = ARRMAX-1; i >= 0; i--){
        if (arr[i][0] != '\0'){
            printf("%s ", arr[i]);
        }
    }
    /*min = abs(arr[0][0]-'A');
    for (i = 0; i < ARRMAX; i++){
        if ((abs(arr[i][0]-'A')) <= min){
            min = abs(arr[i][0]-'A');
            index = i;
        }
    }
    printf("\n");
    printf("%s\n", arr[index]);*/
    return 0;
}