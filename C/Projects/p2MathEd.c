#include <stdio.h>

int main() {
	int user_input1, user_input2, size;
	int i, divisor, count = 0, row, col;
	do {
		printf("Please enter two integers between 1 and 100 (inclusively): \n");
		scanf("%d %d", &user_input1, &user_input2);
	} while (user_input1 < 1 || user_input2 < 1 || user_input1 > 100 || user_input2 > 100 || (user_input2 - user_input1) < 3);
	printf("Evens: \n");
	for (i = user_input1; i <= user_input2; i+=2) {
		if (i % 2 != 0) {
			i++;
		}
		printf("%d ", i);
	}
	printf("\n");
	
	do {
		printf("Please enter a divisor between 1 and 100: \n");
		scanf("%d", &divisor);
	} while (divisor < 1 || divisor > 100);
	
	printf("Multiples of %d: ", divisor);
	for (i = user_input1; i <= user_input2; i++) {
		if (i % divisor == 0) {
			printf("%d ", i);
			count++;
		} 
	}
	if (count == 0){
		printf("NONE\n");
	}
	printf("\n");
	do {
		printf("Please enter a size for a multiplication table between 3-13: \n");
		scanf("%d", &size);
	} while (size < 3 || size > 13);
	for (row = 1; row <= size; row++){
		for (col = 1; col <= size; col++){
			printf("%3d ",col*row);
		}
		printf("\n");
	}
	printf("\n");	
	printf("Perfect squares between %d and %d: ", user_input1, user_input2);
	count = 0;
	for (i = 1; i <=10; i++) {
		if ((i*i) >= user_input1 && (i*i) <= user_input2) {
			printf("%d ", i*i);
			count++;
		}
	}
	if (count == 0){
		printf("NONE\n");
	}
	printf("\n");
	return 0;
}

