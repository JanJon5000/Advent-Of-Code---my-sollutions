#include <stdio.h>
#include <string.h>

typedef struct{
    int x;
    int y;
}coordinates_t;

char numericalKeyboard[5][5] = {{'0', '0', '1', '0', '0'},
                                {'0', '2', '3', '4', '0'},
                                {'5', '6', '7', '8', '9'},
                                {'0', 'A', 'B', 'C', '0'},
                                {'0', '0', 'D', '0', '0'}};

void moveFinger(coordinates_t* currentKey, char direction){
    coordinates_t copy;
    copy.x = currentKey->x;
    copy.y = currentKey->y;
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
        currentKey->y = currentKey->y > 4 ? 4 : currentKey->y;
        break;
    case 'R':
        currentKey->x += 1;
        currentKey->x = currentKey->x > 4 ? 4 : currentKey->x;
        break;
    default:
        break;
    }
    if(numericalKeyboard[currentKey->y][currentKey->x] == '0'){
        currentKey->x = copy.x;
        currentKey->y = copy.y;
    }
}

int main(){
    char answerCode[5];
    int currentChar = 0;
    coordinates_t current;
    current.x = 0;
    current.y = 2;
    FILE* fptr;
    fptr = fopen("input.txt", "r");
    if(fptr == NULL){
        printf("Error opening file\r\n");
    }
    char word[1024];
    while(fscanf(fptr, " %1024[^\r\n]", word) == 1){
        for(int i=0;i<strlen(word);i++){
            moveFinger(&current, word[i]);
            //printf("instrukcja: %c. Teraz jest wybrana liczba: %c\r\n", word[i], numericalKeyboard[current.y][current.x]);
        }
        answerCode[currentChar] = numericalKeyboard[current.y][current.x];
        //printf("ostatecznie wybrana liczba: %c\r\n", numericalKeyboard[current.y][current.x]);
        currentChar++;
        int sep = fgetc(fptr);
        if (sep == EOF) {
            break;
        }
    }

    printf("%s\r\n", answerCode);
    return 0;
}