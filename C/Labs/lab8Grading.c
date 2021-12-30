#include <stdio.h>
#include <stdlib.h>
#define ACUT 90
#define BCUT 80
#include <string.h>

int main() {
	float user_points;
	char letter_grade;
	printf("Please enter a floating point value for the number of points you have: \n");
	scanf("%f", &user_points);
	if (user_points < 0 || user_points > 100) {
		printf("That value is out of range\n");
		exit(EXIT_FAILURE);
	}else {
		if (user_points < BCUT) {
			printf("You earned a C\n");
		}else {
			if (user_points >= BCUT && user_points < ACUT) { 
				printf("You earned a B\n");
			}else {
				if (user_points >= ACUT) {
					printf("You earned an A\n");
				}	
			}
		}
	}
	

	printf("Enter a letter grade: \n");
	scanf(" %c", &letter_grade);
	
	switch(letter_grade) {
		case 'A' :
			printf("You earned between 90 and 100 points\n");
			break;
		case 'B' :
			printf("You earned at least 80 but less than 90 points\n");
			break;	
		case 'C' :
			printf("You earned less than 80 points\n");
			break;
		default :
			printf("That is an invalid letter grade\n");
	}
	return 0;
}
