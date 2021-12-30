#include <stdio.h>
void prStars(int starCnt) {
	int i;
	for (i =1; i <= starCnt; i++)
		printf("*");
	printf("\n");
}

int main(){
	int i, inVal=5, stars;
	
	printf("Default values: \n");	
	prStars(3);
	prStars(7);
	prStars(inVal);
	
	do {
		printf("Enter the number of stars\n");
                scanf("%d", &stars);
        } while (stars % 2 == 0 || stars < 2 || stars > 22);
	printf("User Input: \n");
	for (i=stars; i > 0; i--)
		prStars(i);  
	return 0;
}
