#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#define FIRST_LETTER 97

void decipher(char* str, int number){
    number = number % 26;
    while(*str != '\0'){
        if(*str != '-')
            *str += number;
        *str = *str > 122 ? *str - 26 : *str;
        str++;
    }
}


char* crcConstructor(int* arr){
    char* answer = calloc(5, sizeof(char));
    int charIndex = 0;

    int arrIndex = 0;
    int maxIndex = 0;
    int maxValue = 0;

    while(charIndex < 5){
        arrIndex = 0;
        maxValue = 0;
        while(arrIndex < 26){
            if(*arr > maxValue){
                maxIndex = arrIndex;
                maxValue = *arr;
            }
            arrIndex++;
            arr++;
        }
        arr-=26;
        arr[maxIndex] = 0;
        answer[charIndex] = maxIndex + FIRST_LETTER;
        charIndex++;
    }

    return answer;
}

void crcCheck(char* line){
    int letters[26] = {0};
    char* lineCopy = line;
    int index = 0;
    int sectorID = 0;

    while(*line < 48 || *line > 57){
        if(*line != '-'){
            letters[*line - FIRST_LETTER]++;
        }
        line++;
    }

    // for(int i=0;i<26;i++){
    //     printf("%c : %i\r\n", i + FIRST_LETTER, letters[i]);
    // }

    while(*line != '['){
        sectorID *= 10;
        sectorID += *line - '0';
        // printf("znak: %c, secotrID: %i\r\n", *line, sectorID);
        line++;
    }
    // printf("secotrID: %i\r\n", sectorID);
    line++;
    char* crc = calloc(6, sizeof(char));
    for(int i=0;i<5;i++){
        crc[i] = *line;
        line++;
    }

    if(!strcmp(crc, crcConstructor(letters))){
        decipher(lineCopy, sectorID);
        printf("%s : %i\r\n", lineCopy, sectorID);
    }
}

int main(){
    FILE* fptr = fopen("input.txt", "r");

    if(fptr == NULL){
        printf("Niepoprawny plik\r\n");
        return -1;
    }

    char line[256];
    while(fscanf(fptr, " %255[^\r\n]", line) == 1){
        crcCheck(line);
    }

    return 0;
}