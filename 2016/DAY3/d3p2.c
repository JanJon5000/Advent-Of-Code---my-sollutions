#include <stdio.h>

typedef struct{
    int a;
    int b;
    int c;
}triangle_t;

int isValid(triangle_t triangle){
    if(triangle.a + triangle.b <= triangle.c)
        return 0;
    if(triangle.c + triangle.b <= triangle.a)
        return 0;
    if(triangle.c + triangle.a <= triangle.b)
        return 0;
    return 1;
}

void parse(int* arr, char* str){
    int number = 0;
    int inNumber = 0;
    while(*str != '\0'){
        if(*str != ' '){
            number = number * 10 + (*str - '0');
            inNumber = 1;
        } else if(inNumber){
            *arr++ = number;
            number = 0;
            inNumber = 0;
        }
        str++;
    }
    if(inNumber) *arr = number;
}

triangle_t triangle_init(int a, int b, int c){
    triangle_t answer;
    answer.a = a;
    answer.b = b;
    answer.c = c;
    return answer;
}

int main(){
    FILE* flptr = fopen("input.txt", "r");
    int placeholderArray[3][3];
    int counter = 0;
    int lineCounter = 0;
    triangle_t triangle;
    char word[255];
    
    while(fscanf(flptr, " %255[^\r\n]", word) == 1){
        parse(placeholderArray[lineCounter], word);
        lineCounter++;
        if(lineCounter == 3){
            printf("po transponowaniu: \r\n");
            for(int i=0;i<3;i++){
                triangle = triangle_init(placeholderArray[0][i], placeholderArray[1][i], placeholderArray[2][i]);
                printf("%i, %i, %i\r\n", triangle.a, triangle.b, triangle.c);
                counter += isValid(triangle);
            }
            lineCounter = 0;
        }
    }

    printf("%i\r\n", counter);
    return 0;
}