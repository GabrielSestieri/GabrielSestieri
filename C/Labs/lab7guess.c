#include <stdio.h>
#include <stdlib.h>
#define MARGIN 3

int main() {
	int player_one, player_two;
	
	printf("Player one, please input an integer between 1 and 10 (inclusive): \n");
	scanf("%d", &player_one);
	
	system("@cls||clear");

	printf("Player two, please guess the integer provided by player one: \n");
	scanf("%d", &player_two);

	if (player_two == player_one) {
		printf("CORRECT - 5 points!!\n");
	} else {
		if (player_two < player_one && player_two >= player_one - MARGIN){
			printf("Good but low - 2 point!!\n");
		}else { 
			if (player_two > player_one && player_two <= player_one + MARGIN) {
				printf("Good but high - 2 points!!\n");
			}
		}
	}		

	return 0; 
}		
