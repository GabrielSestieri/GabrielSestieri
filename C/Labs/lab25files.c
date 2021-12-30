#include <stdio.h>
#include <stdlib.h>
#define ARRMAX 10
typedef int ArrType[ARRMAX];
int main(){
	/* declare variables as needed */
	FILE * inFile = NULL;
	FILE * outFile = NULL;
	ArrType fileInArr;
	int i = 0;
	int val1, val2, sum;
	char c;
	
	inFile = fopen("infile.txt","r");
	if (inFile == NULL){
                printf("Error opening file\n");
                exit(EXIT_FAILURE);
        }	

	outFile = fopen ("outfile.txt","w");
        if (inFile == NULL){
                printf("Error opening file\n");
                exit(EXIT_FAILURE);
        }
	
	/* Create a while loop that reads 2 integer values
 	* from the input file reference previously opened.  
 	* The loop should terminate if the fscanf 
 	* does not return the value 2
 	* (this would only happen if it is not able to read 2 values).
 	* Get the sum of the 2 values read, and 
 	* write that sum to the output file reference
 	* so that only one number appears on each line of the 
 	* file associated with the output file reference.
 	* Count how many pairs of values were read (and therefore how
 	* many sums were put into the output file). */
	c = fgetc(inFile);
        /*while (c != EOF){
		printf("%c", c);
                c = fgetc(inFile);
        }*/
	while (c != EOF){
			if (fscanf(inFile, "%d %d", &fileInArr[i]) == 2){
				sum = fileInArr[i] + fileInArr[i+1];	
				fprintf(outFile, "%d + %d = %d\n",fileInArr[i],fileInArr[i+1],sum);
			}else{
				printf("Error scanning file\n");
				exit(EXIT_FAILURE);
			}
		}	
	/* Have an output line to standard output to tell the number
 	* of pairs of values were read and summed. (This should 
 	* correspond to the number of lines in the file associated
 	* with the output file reference.)*/

	/* Close both file references opened above */
	fclose(inFile);
	fclose(outFile);
	return 0;
}
