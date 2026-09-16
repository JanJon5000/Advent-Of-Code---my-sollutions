#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdbool.h>

typedef struct{
    int x;
    int y;
}coordinates_t;

typedef enum{
    NORTH = 0,
    EAST = 1,
    SOUTH = 2,
    WEST = 3,
}direction_t;

typedef struct{
    char direciton;
    int steps;
}instruction_t;

void changeDirection(char way, direction_t *currentDir){
    switch(way){
        case 'L':
            *currentDir = (*currentDir + 3)%4;
            break;
        case 'R':
            *currentDir = (*currentDir + 1)%4;
            break;
        default:
            printf("Error - zla wartosc kierunku\r\n");
            return;
    }
}

void walk(int steps, coordinates_t *coords, direction_t currentDir){
    switch(currentDir){
        case NORTH:
            coords->y += steps;
            break;
        case SOUTH:
            coords->y -= steps;
            break;
        case EAST:
            coords->x += steps;
            break;
        case WEST:
            coords->x -= steps;
            break;
        default:
            printf("Error - zla wartosc kierunku\r\n");
            break;
    }
}

instruction_t parse(char* string){
    instruction_t answer;
    answer.direciton = string[0];
    answer.steps = 0;
    string++;
    while(*string != '\0'){
        answer.steps*=10;
        answer.steps += *string - '0';
        string++;
    }
    return answer;
}

bool searchArray(coordinates_t* arr, int numberOfElements, coordinates_t element){
    for(int i=0;i<numberOfElements;i++){
        if(arr->x == element.x && arr->y == element.y){
            return true;
        }
        arr++;
    }
    return false;
}

int main(){
    coordinates_t headquaters;
    coordinates_t* allVisited = calloc(1, sizeof(coordinates_t));
    int lastIndex = 0;
    headquaters.x = 0;
    headquaters.y = 0;

    direction_t dir = NORTH;
    instruction_t currentInstruction;
    FILE* fptr;
    fptr = fopen("input.txt", "r");
    if(fptr == NULL){
        printf("Error - pliku nie znaleziono\r\n");
        return -1;
    }

    
    char word[5];
    while (fscanf(fptr, " %4[^,\r\n]", word) == 1){
        currentInstruction = parse(word);
        changeDirection(currentInstruction.direciton, &dir);
        for(int i=0;i<currentInstruction.steps;i++){
            walk(1, &headquaters, dir);
            if(searchArray(allVisited, lastIndex+1, headquaters)){
                printf("%i\r\n", abs(headquaters.x) + abs(headquaters.y));
                return 0;
            }else{
                allVisited = realloc(allVisited, (lastIndex + 2) * sizeof(coordinates_t));
                lastIndex++;
                allVisited[lastIndex] = headquaters;
            }
        }
            
        int sep = fgetc(fptr);
        if (sep == EOF) {
            break;
        }
    }
    
    printf("%i\n", abs(headquaters.x + headquaters.y));

    return 0;
}