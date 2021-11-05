#include <stdio.h>
#include <string.h>
#define ARRLEN 10
#define SLEN 20

void fillScores(int scores[],int size){
	int index;
	for (index=0; index<size; index++){
		scanf("%d",&scores[index]);
	}
	return;
}
void fillNames(char names[ARRLEN][SLEN],int size){
	int index, len;
	for (index = 0; index < size; index++){
		fgets(names[index],SLEN,stdin);
		len = strlen(names[index]);
		names[index][len-1] = '\0';
	}
	return;
}
/* Implment your functions after this line */
int highestScore(int scores[], int size) {
    int highest, i, index;
    for (i=0; i < size; i++) {
        if (scores[i] > highest) {
            highest = scores[i];
            index = i;
        }
    }
    return index;    
}
int lowestScore(int scores[], int size) {
    int lowest, i, index;
    for (i=0; i < size; i++) {
        if (scores[i] < lowest) {
            lowest = scores[i];
            index = i;
        }
    }
    return index;
}

int main(){
	int scores[ARRLEN], highest, lowest;
	char names[ARRLEN][SLEN];
	fillNames(names,ARRLEN);
	fillScores(scores,ARRLEN);
    highest = highestScore(scores, ARRLEN);
    lowest = lowestScore(scores, ARRLEN);
    printf("Winner: %s with %d\n", names[highest], scores[highest]);
    printf("Eliminated: %s with %d\n", names[lowest], scores[lowest]);
	/* add your lines after this line */
	
	return 0;
}