#include <stdio.h>
#include <stdlib.h>
#define LETTERS 8

char findMax(int* arr){
    char answer = 'a';
    int maxValue = 0;
    for(int i=0;i<26;i++){
        if(arr[i] > maxValue){
            maxValue = arr[i];
            answer = 'a' + i;
        }
    }
    return answer;
}


int main(){
    int letters[LETTERS][26] = {{0}, {0}, {0}, {0}, {0}, {0}, {0}, {0}};
    FILE* fptr = fopen("input.txt", "r");
    if(fptr == NULL){
        printf("Blad otwierania pliku\r\n");
        return -1;
    }

    int i = 0;
    char line[256];
    while(fscanf(fptr, " %255[^\r\n]", line) == 1){
        printf("%s\r\n", line);
        for(i = 0;i<LETTERS;i++){
            letters[i][line[i] - 'a'] += 1;
        }

        int sep = fgetc(fptr);
        if (sep == EOF) {
            break;
        }
    }

    for(i = 0;i<LETTERS;i++){
        line[i] = findMax(letters[i]);
    }

    printf("wiadomosc: %s\r\n", line);
    return 0;
}