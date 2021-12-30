#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int rand10() {
	int num;
	num = (rand() % 10) + 1;	
	return num;
}

int main() {
	int num;
	int guess;
	srand(time(0));
	num = rand10();
	
	do {
		printf("Guess the number between 1 and 10 \n");
		scanf("%d", &guess);
		if (guess < num) {
			printf("Too low\n");
		}
		if (guess > num) {
			printf("Too high\n");
		}
	} while (guess !=num);
	printf("Correct\n");		
	
	return 0;
}
