#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#define SIZE 5

void fillArray(int arr[], int size) {
    int i;
    for (i = 0; i < size; i++) {
        arr[i] = (rand() % 10) + 1;
    }
    return;
}

int sumArray(int arr[], int size) {
    int sum = 0, i;
    for (i = 0; i < size; i++) {
        sum += arr[i];
    }
    return sum;
}

int main() {
    int arr1[SIZE], arr2[SIZE], sum1, sum2;
    srand(time(0));
    fillArray(arr1, SIZE);
    fillArray(arr2, SIZE);
    sum1 = sumArray(arr1, SIZE);
    sum2 = sumArray(arr2, SIZE);
    if (sum1 > sum2) {
        printf("arr1 wins %d to %d\n", sum1, sum2);
    } else if (sum1 == sum2) {
        printf("tie between arr1 and arr2 at %d\n", sum1);
    } else if (sum2 > sum1) {
        printf("arr2 wins %d to %d\n", sum2, sum1);
    }
    return 0;
}