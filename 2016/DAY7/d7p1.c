#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

bool hasABBA(char input1, char input2, char input3, char input4){
    return ((input1 == input4) && (input2 == input3)) && (input1 != input2);
}

bool parse(char* inputLine){
    bool isInsideBrackets = false;
    bool answer = false;
    while(*(inputLine + 3) != '\0'){
        if(*(inputLine - 1) == '[')
            isInsideBrackets = true;
        else if(*(inputLine - 1) == ']')
            isInsideBrackets = false;
        if(hasABBA(*inputLine, *(inputLine+1), *(inputLine+2), *(inputLine+3))){
            if(isInsideBrackets)
                return false;
            else
                answer = true;
        }
        inputLine++;
    }
    return answer;
}

int main(){
    FILE* fptr = fopen("input.txt", "r");
    int sum = 0;
    char line[256];
    while(fprintf(fptr, "%255[^\r\n]", line) == 1){
        sum += parse(line) ? 1 : 0;
        int sep = fgetc(fptr);
        if (sep == EOF) {
            break;
        }
    
    }
    printf("%i\r\n", sum);
}