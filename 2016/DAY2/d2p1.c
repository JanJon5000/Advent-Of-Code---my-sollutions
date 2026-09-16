#include <stdio.h>
#include <string.h>

typedef struct{
    int x;
    int y;
}coordinates_t;

int numericalKeyboard[3][3] = {{1, 2, 3}, {4, 5, 6}, {7, 8, 9}};
void moveFinger(coordinates_t* currentKey, char direction){
    switch (direction){
    case 'U':
        currentKey->y -= 1;
        currentKey->y = currentKey->y < 0 ? 0 : currentKey->y;
        break;
    case 'L':
        currentKey->x -= 1;
        currentKey->x = currentKey->x < 0 ? 0 : currentKey->x;
        break;
    case 'D':
        currentKey->y += 1;
        currentKey->y = currentKey->y > 2 ? 2 : currentKey->y;
        break;
    case 'R':
        currentKey->x += 1;
        currentKey->x = currentKey->x > 2 ? 2 : currentKey->x;
        break;
    default:
        break;
    }
}

int main(){
    int answerCode = 0;
    coordinates_t current;
    current.x = 1;
    current.y = 1;
    FILE* fptr;
    fptr = fopen("input.txt", "r");
    if(fptr == NULL){
        printf("Error opening file\r\n");
    }
    char word[1024];
    while(fscanf(fptr, " %1024[^\r\n]", word) == 1){
        for(int i=0;i<strlen(word);i++){
            moveFinger(&current, word[i]);
            //printf("instrukcja: %c. Teraz jest wybrana liczba: %i\r\n", word[i], numericalKeyboard[current.y][current.x]);
        }
        answerCode *= 10;
        answerCode += numericalKeyboard[current.y][current.x];
        //printf("ostatecznie wybrana liczba: %i\r\n", numericalKeyboard[current.y][current.x]);
        int sep = fgetc(fptr);
        if (sep == EOF) {
            break;
        }
    }

    printf("%i\r\n", answerCode);
    return 0;
}