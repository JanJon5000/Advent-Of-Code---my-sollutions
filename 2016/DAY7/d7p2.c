#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

int parse(char* inputString){
    bool isInside = false;
    char inside[100][3];
    char outside[100][3];
    int i=0;
    int j=0;

    while(*(inputString + 2) != '\0'){
        if(*(inputString - 1) == '[' || *(inputString - 1) == ']')
            isInside = !isInside;
        if(*(inputString) == *(inputString + 2) && *(inputString) != *(inputString + 1) 
            && *(inputString) != '[' && *(inputString + 1) != '['
            && *(inputString) != ']' && *(inputString + 1) != ']'){
            if(isInside){
                inside[i][0] = *(inputString); inside[i][1] = *(inputString + 1); inside[i][2] = *(inputString + 2);  
                //printf("w srodku: %c%c%c\r\n", *(inputString), *(inputString+1), *(inputString+2));
                i++;
            }else{
                outside[j][0] = *(inputString); outside[j][1] = *(inputString + 1); outside[j][2] = *(inputString + 2);
                //printf("na zewnatrz: %c%c%c\r\n", *(inputString), *(inputString+1), *(inputString+2));
                j++;
            }
        }
        inputString++;
    }

    for(int k=0;k<i+1;k++){
        for(int l=0;l<j+1;l++){
            if(inside[k][0] == outside[l][1] && inside[k][1] == outside[l][0])
                return 1;
        }
    }
    return 0;
}   

int main(){
    FILE* fptr = fopen("input.txt", "r");
    if(fptr == NULL){
        printf("invalid file\r\n");
        return -1;
    }

    int sum = 0;
    char line[256];
    
    while(fscanf(fptr, "%255[^\r\n]", line) == 1){
        printf("%s\r\n", line);
        sum += parse(line);
        int sep = fgetc(fptr);
        if (sep == EOF) {
            break;
        }
    }
    printf("wyniki kalkulacji: %d", sum);
    
    return 0;
}