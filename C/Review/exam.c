#include <stdio.h>
#include <string.h>
#include <ctype.h>
#define ARRMAX 10
#define STRMAX 20
typedef int StrType[STRMAX];
typedef int ArrType[ARRMAX];

int countBtwn(ArrType myArr, int size, int low, int high){
    int i;
    int count = 0;
    for (i=0;i<size;i++){
        if (myArr[i] >= low && myArr[i] <= high){
            count++;
        }
    }
    return count;
}

int fillArr(ArrType myArr, int low, int high){
    int i = 0;
    int count = 0;
    int inVal;
    printf("give a num:");
    while (scanf("%d", &inVal) == 1 && i < ARRMAX){
        if (inVal >= low && inVal <= high){
            myArr[i] = inVal;
            count++;
        }
    }
    return count;
}

int main(){
    ArrType arr;
    int lowVal, highVal, size, count;
    printf("Give two values, low and high");
    scanf("%d %d", &lowVal, &highVal);
    size = fillArr(arr, lowVal, highVal);
    count = countBtwn(arr, size, lowVal, highVal);
    if (size == count){
        printf("good\n");
    }else{
        printf("bad\n");
    }
    return 0;
}

int goodPhone(StrType myNum){
    int i;
    for (i=0;i<STRMAX;i++){
        if ( isdigit(myNum[0])==1 && isdigit(myNum[1]) == 1 && isdigit(myNum[2] == 1)){
            printf("area code is good");
        } else{
            printf("error in the first three numbers");
        }
        if (strchr(myNum[3], "-") == 1){
            printf("first dash good");
        } else{
            printf("missing a first dash");
        }
        if ( isdigit(myNum[4]) == 1 && isdigit(myNum[5]) == 1 && isdigit(myNum[6]) == 1){
            printf("extension is good");
        } else{
            printf("something is wrong with the extension");
        }
        if (strchr(myNum[7], "-") == 1){
            printf("second dash good");
        } else {
            printf("missing second dash");
        }
        if (isdigit(myNum[8]) == 1 && isdigit(myNum[9]) == 1 && isdigit(myNum[10]) == 1 && isdigit(myNum[11]) == 1){
            printf("subscriber number good");
        } else{
            printf("subscriber number not good");
        }
    }
    return 0;
}

void removeDashes(StrType myNum){
    int i;
    for (i=0;i<STRMAX;i++){
        if (myNum[i] == '-'){
            myNum[i] == "";
        }
    }
}


