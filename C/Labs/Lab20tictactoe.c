#include <stdio.h>
#include <string.h>
#define SIZE 3
#define STRLEN 10

void fillBoard(char board[SIZE][SIZE]) {
    int row, col; 
    for (row=0; row < SIZE; row++){
        for(col=0; col < SIZE; col++) {
            scanf("%c", &board[row][col]);
        }
    }
    return;
}

void printBoard(char board[SIZE][SIZE]) {
    int row, col;
    for (row=0; row < SIZE; row++){
        for (col=0; col < SIZE; col++){
            printf("%c", board[row][col]);
        }
        printf("\n");
    }
    return;
}

int verticalWin(char board[SIZE][SIZE], char *winningSymbol){
    int col, row = 0;
    for (col = 0; col < SIZE; col++) {
        if (board[row][col]==board[row+1][col] && board[row][col]==board[row+2][col] && board[row][col] != '-'){
            *winningSymbol = board[row][col];
            return 1;
        }
        row = 0;
    }
    return 0;
}

int horizontalWin(char board[SIZE][SIZE], char *winningSymbol){
    int col = 0, row;
    for (row = 0; row < SIZE; row++){
        if (board[row][col]==board[row][col+1] && board[row][col]==board[row][col+2] && board[row][col] != '-'){
            *winningSymbol = board[row][col];
            return 1;
        }
        col = 0;
    }
    return 0;
}

int diagonalWin(char board[SIZE][SIZE], char *winningSymbol){
    int row = 0, col = 0;
    if (board[row][col]==board[row+1][col+1] && board[row][col]==board[row+2][col+2] && board[row][col]!= '-'){
        *winningSymbol = board[row][col];
        return 1;
    }
    row = 0;
    col = 2;
    if (board[row][col]==board[row+1][col-1] && board[row][col]==board[row+2][col-2] && board[row][col]!= '-'){
        *winningSymbol = board[row][col];
        return 1;
    }
    return 0;
}

int noMoves(char board[SIZE][SIZE]){
    int row,col;
    for (row=0; row < SIZE; row++){
        for (col=0; col < SIZE; col++){
            if (board[row][col] == '-'){
                return 1;
            }
        }
    }
    return 0;
}

int main(){
    char board[SIZE][SIZE], winningSymbol;
    fillBoard(board);
    printBoard(board);
    if (verticalWin(board, &winningSymbol) == 1 || horizontalWin(board, &winningSymbol) == 1 || diagonalWin(board, &winningSymbol) == 1){
        printf("%c wins\n", winningSymbol);
    } else if (noMoves(board) == 1) {
        printf("No winner yet\n");
    } else {
        printf("Game over\n");
    }
    return 0;

}