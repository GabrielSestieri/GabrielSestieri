#include <stdio.h>
/* This program will take two given inputs describing the length and width of a lawn and will output those dimensions in various measurements such as square feet, inches, yards, and meters.
 * Gabriel Sestieri, September 29th 2021, CMSC106. */
int main(){
	int length, length_in, length_yd, length_remainder_ft, width, width_in, width_yd, width_remainder_ft, square_feet;
	float length_meter, width_meter;
	printf("1. Please input your two dimensions represented as length and width, respectively, in feet and as whole numbers: \n");
	scanf("%d %d", &length, &width);
	
	square_feet = length*width;
	printf("2. Your lawn is %d square feet.\n", square_feet);
	
	length_in = length*12;
 	width_in = width*12;
	printf("3. In inches, your lawn's dimensions are %d by %d.\n", length_in, width_in);

	length_yd = length/3;
	length_remainder_ft = length%3;
	width_yd = width/3;
	width_remainder_ft = width%3;
	printf("4. In yards and feet, your lawn's dimensions are %dyd and %dft by %dyd and %dft.\n", length_yd, length_remainder_ft, width_yd, width_remainder_ft);

	length_meter = length*0.3048;
	width_meter = width*0.3048;
	printf("5. In meters, your lawn's dimensions are %.3f by %.3f.\n", length_meter, width_meter);
	
	return 0;
}
