#include<stdio.h>
 
int main() {
	int size,rows,cols, star = 0, space;
    	do {
		printf("Enter the number of rows\n");
    		scanf("%d", &size);
	} while (size % 2 == 0 || size < 2 || size > 22);

	printf("Right Triangle: \n"); 
    	for(rows = 0; rows < size; rows++) {
		for(cols = 0; cols < size - rows; cols++) {
            		printf("* ");
        	}
        	printf("\n");
    	}
	printf("Pyramid: \n");
	for (rows = 0; rows < size; rows++) {
        	for (cols = 0; cols <= (size - rows - 1); cols++) {
            		printf(" ");
        	}
        	while (star != (2 * rows + 1)) {
            		printf("*");
            		star++;
        	}	
       		star = 0;
        	printf("\n");
    	}
	printf("Diamond: \n");
	size = (size/2)+1;
    	for (rows = 1; rows <= size; rows++) {
    		for (space = 1; space <= size-rows; space++)
      			printf(" ");

    		for (space = 1; space <= 2*rows-1; space++)
      			printf("*");

    		printf("\n");
  	}	

  	for (rows = 1; rows <= size - 1; rows++) {
    		for (space = 1; space <= rows; space++)
      			printf(" ");

    		for (space = 1 ; space <= 2*(size-rows)-1; space++)
      			printf("*");

   		printf("\n");
  	}	
	
	return 0;
}
