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
    if(inNumber) *arr = number;   // domknięcie ostatniej liczby
}


triangle_t triangle_init(int* arr){
    triangle_t answer;
    answer.a = arr[0];
    answer.b = arr[1];
    answer.c = arr[2];
    return answer;
}

int main(){
    FILE* flptr = fopen("input.txt", "r");
    int placeholderArray[3];
    int counter = 0;
    triangle_t triangle;
    char word[255];
    
    while(fscanf(flptr, " %255[^\r\n]", word) == 1){
        parse(placeholderArray, word);
        printf("%i, %i, %i\r\n", placeholderArray[0], placeholderArray[1], placeholderArray[2]);
        triangle = triangle_init(placeholderArray);
        counter += isValid(triangle);

        int sep = fgetc(flptr);
        if (sep == EOF) {
            break;
        }
    }

    printf("%i\r\n", counter);
    return 0;
}