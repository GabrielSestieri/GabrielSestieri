#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#define SIZE 5

int main() {
    int arr1[SIZE], arr2[SIZE], i, sum1 = 0, sum2 = 0;
    srand(time(0));
    for (i = 0; i < SIZE; i++) {
        arr1[i] = (rand() % 10) + 1;
        arr2[i] = (rand() % 10) + 1;
    }
    for (i = 0; i < SIZE; i++) {
        sum1 += arr1[i];
        sum2 += arr2[i];
    }
    if (sum1 > sum2) {
        printf("arr1 wins %d to %d\n", sum1, sum2);
    } else if (sum1 == sum2) {
        printf("tie between arr1 and arr2 at %d\n", sum1);
    } else if (sum2 > sum1) {
        printf("arr2 wins %d to %d\n", sum2, sum1);
    }
    return 0;
}