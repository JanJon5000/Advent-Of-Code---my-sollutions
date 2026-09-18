#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

bool hasABBA(char* input){
    while(*(input + 3) != '\0'){
        if( (*input == *(input + 3)) && 
            (*(input + 1) == *(input + 2)) && 
            (*input != *(input + 1))){
                return true;
            }
        input++;
    }
    return false;
}

bool parse(char* inputLine){
    char* first = calloc(100, sizeof(char));
    char* inside = calloc(100, sizeof(char));
    char* second = calloc(100, sizeof(char));
    int i = 0;
    while(*inputLine != '['){
        *(first + i) = *inputLine;
        inputLine++; 
        i++;
    }
    *(first + i) = '\0';
    i = 0;
    inputLine++;

    printf("%s\r\n", first);

    while(*inputLine != ']'){
        *(inside + i) = *inputLine;
        inputLine++; 
        i++;
    }
    *(inside + i) = '\0';
    i = 0;
    inputLine++;

    printf("%s\r\n", inside);
    
    while(*inputLine != '\0'){
        *(second + i) = *inputLine;
        inputLine++; 
        i++;
    }
    *(second + i) = '\0';
    i = 0;
    inputLine++;

    printf("%s\r\n", second);

    bool ans = false;
    // printf("%s, %B\r\n", first, hasABBA(first));
    // printf("%s, %B\r\n", inside, hasABBA(inside));
    // printf("%s, %B\r\n", second, hasABBA(second));
   
    if((hasABBA(first) || hasABBA(second)) && !hasABBA(inside))
        ans = true;
    free(first);
    free(second);
    free(inside);
    return ans;
}

int main(){
    FILE* fptr = fopen("input.txt", "r");
    int sum = 0;
    char line[256];
    while(fscanf(fptr, "%255[^\r\n]", line) == 1){
        sum += parse(line) ? 1 : 0;
        int sep = fgetc(fptr);
        if (sep == EOF) {
            break;
        }
    }
    printf("%i\r\n", sum);
}