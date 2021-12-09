#include <stdio.h>
#include <string.h>
#define CSIZE 10
#define SSIZE 20
void fillArray(char names[CSIZE][SSIZE], float midterm[CSIZE], float final[CSIZE], float project[CSIZE]) {
    int i;
    for (i = 0; i < CSIZE; i++) {
        fgets(names[i], CSIZE, stdin);
        names[i][strlen(names[i])-1] = '\0';
        }
    for (i = 0; i < CSIZE; i++) {
        scanf("%f", &midterm[i]);
        }
    for (i = 0; i < CSIZE; i++) {
        scanf("%f", &final[i]);
        }
    for (i = 0; i < CSIZE; i++) {
        scanf("%f", &project[i]);
        }    
    return;
}
void bestMidTerm(char name[CSIZE][SSIZE], float midterm[CSIZE]){ 
    int index, i;
    float highest = 0.0;
    for (i=0; i < CSIZE; i++){
        if (midterm[i] > highest) {
            highest = midterm[i];
            index = i;
        }
    }
    printf(" %s has the best midterm with %.1f\n", name[index], midterm[index]);
    return;
}
void bestFinal(char name[CSIZE][SSIZE], float final[CSIZE]){ 
    int index, i;
    float highest = 0.0;
    for (i=0; i < CSIZE; i++){
        if (final[i] > highest) {
            highest = final[i];
            index = i;
        }
    }
    printf(" %s has the best final with %.1f\n", name[index], final[index]);
    return;
}
void bestProject(char name[CSIZE][SSIZE], float project[CSIZE]){ 
    int index, i;
    float highest = 0.0;
    for (i=0; i < CSIZE; i++){
        if (project[i] > highest) {
            highest = project[i];
            index = i;
        }
    }
    printf(" %s has the best project with %.1f\n", name[index], project[index]);
    return;
}
int printGrades(char name[CSIZE][SSIZE], float midterm[CSIZE], float final[CSIZE], float project[CSIZE], float *highest, float grades[CSIZE]){
    int i, index;
    for (i=0; i < CSIZE; i++){
        grades[i] = (midterm[i]*0.30)+(final[i]*0.50)+(project[i]*0.20);
        printf(" %s has a grade of %.1f\n", name[i], grades[i]);
        if (grades[i] > *highest){
            *highest = grades[i];
            index = i;
        }
    }
    return index;
}
void assignLetterGrades(char names[CSIZE][SSIZE], float grades[CSIZE]){
    int i;
    for (i=0; i < CSIZE; i++){
        if (grades[i] >= 90){
            printf(" %s has an A\n", names[i]);
        } else if (grades[i] >= 80){
            printf(" %s has a B\n", names[i]);
        } else if (grades[i] >= 70){
            printf(" %s has a C\n", names[i]);
        } else if (grades[i] >= 60){
            printf(" %s has a D\n", names[i]);
        } else {
            printf(" %s has an F\n", names[i]);
        }
    }
    return;
}
int main () {
    float midterm[CSIZE], final[CSIZE], project[CSIZE], highest, grades[CSIZE];
    char names[CSIZE][SSIZE];
    int index;
    fillArray(names, midterm, final, project);
    printf("\n----The best midterm----\n");
    bestMidTerm(names, midterm);
    printf("\n----The best final----\n");
    bestFinal(names, final);
    printf("\n----The best project----\n");
    bestProject(names, project);
    printf("\n----Individual student grades----\n");
    index = printGrades(names, midterm, final, project, &highest, grades);
    printf("\n %s has the highest grade with a %.1f\n", names[index], highest);
    printf("\n----Individual student letter grades----\n");
    assignLetterGrades(names, grades);
    return 0;
}