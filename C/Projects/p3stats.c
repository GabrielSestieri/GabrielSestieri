#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <math.h>

int input() {
    int input, count = 1;
    do {
        if (count > 2) {
            printf("PLEASE PROVIDE AN INTEGER BETWEEN -100 AND 100 (INCLUSIVE): \n");
            scanf("%d", &input);
        } else {
            printf("Please provide an integer between -100 and 100 (inclusive): \n");
            scanf("%d", &input);
        }
        count += 1;
    } while (input < -100 || input > 100); 
    return input;
}

void average(x,y,z) {
    int random;
    float average;
    random = (rand() % 201) + (-100);
    average = (float) ((x+y+z)/3);
    if (average > random) {
        printf("Average %.1f is larger than Random %d\n", average, random);
    } else if (fabs(average - random) <= 10) {
        printf("Average %.1f is within 10 of Random %d\n", average, random);
    } else if (average < random) {
        printf("Average %.1f is NOT larger than Random %d\n", average, random);
    }
}

int printvals(int var1, int var2, int var3) {
    int count = 0;
    if (var1 > var2 && var2 > var3) {
        printf("Ascending: %d %d %d\n", var3, var2, var1);
    } else if (var1 > var3 && var3 > var2) {
        printf("Ascending: %d %d %d\n", var2, var3, var1);
    } else if (var2 > var1 && var1 > var3) {
        printf("Ascending: %d %d %d\n", var3, var1, var2);
    } else if (var2 > var3 && var3 > var1) {
        printf("Ascending: %d %d %d\n", var1, var3, var2);
    } else if (var3 > var1 && var1 > var2) {
        printf("Ascending: %d %d %d\n", var2, var1, var3);
    } else if (var3 > var2 && var2 > var1) {
        printf("Ascending: %d %d %d\n", var1, var2, var3);
    } else if (var1 == var2 && var1 > var3) {
        printf("Ascending: %d %d %d\n", var3, var2, var1);
    } else if (var2 == var3 && var2 > var1) {
        printf("Ascending: %d %d %d\n", var1, var2, var3);
    } else if (var3 == var1 && var3 > var2) {
        printf("Ascending: %d %d %d\n", var2, var1, var3);
    } else if (var1 == var2 && var1 < var3) {
        printf("Ascending: %d %d %d\n", var1, var2, var3);
    } else if (var2 == var3 && var2 < var1) {
        printf("Ascending: %d %d %d\n", var2, var3, var1);
    } else if (var3 == var1 && var3 < var2) {
        printf("Ascending: %d %d %d\n", var1, var3, var2);
    }
    count += 1;
    return 0;
}

int main() {
    int var1, var2, var3;
    srand(time(0));
    var1 = input();
    var2 = input();
    var3 = input();
    average(var1,var2,var3);
    average(0,0,0);
    average(1,2,4);
    printf("In order they were received: %d %d %d\n", var1, var2, var3);
    printvals(var1, var2, var3);
    return 0;
}