#include <stdio.h>
#include <stdlib.h>
#include <time.h>



int rollDice(int *x, int *y) {
	int randnum1, randnum2;
	randnum1 = (rand() % 6) + 1;
	randnum2 = (rand() % 6) + 1;
	*x = randnum1;
	*y = randnum2;
	if (randnum1 == randnum2) {
		return 1;
	} else {
		return 0;
	}
}

int main() {
	srand(time(0));
	int x, y, count;
	for (count = 1; count < 11; count++) {
		if (rollDice(&x, &y) == 1) {
			printf("Doubles: %d\n", x);
		} else {
			printf("%d %d\n", x, y);	
		}
	}		
	return 0;
}