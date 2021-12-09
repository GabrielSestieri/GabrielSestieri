#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <ctype.h>
#define STRMAX 20

typedef char StrType[STRMAX];

int goodPhone(StrType myNum){
    int i;
    if (strlen(myNum) != 12) return 0;

    for (i=0; i < 3; i++){
        if (!isdigit(myNum[i])){
            return 0;
        } else{ (printf("error in area code"));}
    }
    if (myNum[i] != '-') return 0;
    else (printf("error in first dash"));
    i++;
    for ( ; i < 7; i++){
        if(!isdigit(myNum[i])) return 0;
        else (printf("error in extension"));
    }
    if (myNum[i] != '-') return 0;
    else (printf("error in second dash"));
    i++;
    for ( ; i<12; i++){
        if (!isdigit(myNum[i])) return 0;
        else (printf("error in sub code"));
    }
    return 1;
    /*for (i=0;i<STRMAX;i++)
    {
        printf("%d", isdigit(myNum[1]));
        if (isdigit(myNum[0]) == 0 && isdigit(myNum[1]) == 0 && isdigit(myNum[2]) == 0){
           printf("error in the first three numbers\n");
        }
        if (isdigit(myNum[3]) != 0){
            printf("missing a first dash\n");
        }
        if ( isdigit(myNum[4]) != 1 && isdigit(myNum[5]) != 1 && isdigit(myNum[6]) != 1){
            printf("something is wrong with the extension\n");
        }
        if ( isdigit(myNum[7]) != 0){
            printf("missing second dash\n");
        }
        if (isdigit(myNum[8]) != 1 && isdigit(myNum[9]) != 1 && isdigit(myNum[10]) != 1 && isdigit(myNum[11]) != 1){
            printf("subscriber number not good\n");
        }
        return 1;
    }
    return 0;
    */
}

int main(){
    int ls;
    StrType myNum = "240-801-209-";
    ls = goodPhone(myNum);
    if (ls == 1){
        printf("Phone number is good!\n");
    }
    return 0;
}
