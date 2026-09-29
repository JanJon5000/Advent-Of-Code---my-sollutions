#include <stdio.h>
#include <string.h>

#define COLUMNS 7
#define ROWS 3

typedef struct{
    char command[6];
    char commandArgument;
    int firstArgument;
    int secondArgument;
}command_t;

command_t commandParser(char* command){
    command_t commandAns;
    int i=0;
    while(*command != ' '){
        commandAns.command[i] = *command;
        command++;
        i++;
    }
    command++;
    commandAns.command[6] = '\0';
    if(strcmp(commandAns.command, "rotate") == 0){
        while(*command != ' '){
            command++;
        }
        command++;
        commandAns.commandArgument = *command;
        command+=2;
        commandAns.firstArgument = *command - '0';
        command+=5;
        commandAns.secondArgument = *command - '0';
    }else{ //rect            
        commandAns.firstArgument = *command - '0';
        command+=2;
        commandAns.secondArgument = *command - '0';
    }
    //printf("komenda: %s, %c, %i, %i\r\n", commandAns.command, commandAns.commandArgument, commandAns.firstArgument, commandAns.secondArgument);
    return commandAns;

}


int main(){
    command_t currentCommand;
    char screen[ROWS][COLUMNS];
    for(int i=0;i<ROWS;i++){
        for(int j=0;j<COLUMNS;j++){
            screen[i][j] = '.';
        }
    }
    
    FILE* fptr = fopen("input.txt", "r");
    if(fptr == NULL){
        printf("invalid file\r\n");
        return -1;
    }
    char line[256];
    while(fscanf(fptr, " %255[^\r\n]", line) == 1){
        currentCommand = commandParser(line);
        if(currentCommand.command[0] == 'r' && currentCommand.command[1] == 'e' && currentCommand.command[2] == 'c' && currentCommand.command[3] == 't'){
            for(int i=0;i<currentCommand.secondArgument;i++){
                for(int j=0;j<currentCommand.firstArgument;j++){
                    screen[i][j] = '#';
                }
            }
            printf("wykonywany rect\r\n");
        }else{
            printf("wykonywany rotate\r\n");
            if(currentCommand.commandArgument == 'x'){
                for(int i=0;i<ROWS;i++){
                    screen[i][currentCommand.firstArgument] = screen[(-currentCommand.secondArgument + i)%COLUMNS][currentCommand.firstArgument];
                }
            }else{//y
                for(int i=0;i<COLUMNS;i++){
                    screen[currentCommand.firstArgument][i] = screen[currentCommand.firstArgument][(-currentCommand.secondArgument + i)%ROWS];
                }
            }
        }
        for(int i=0;i<ROWS;i++){
            for(int j=0;j<COLUMNS;j++){
                printf("%c ", screen[i][j]);
            }
            printf("\r\n");
        }
        printf("\r\n");
    }
    for(int i=0;i<ROWS;i++){
        for(int j=0;j<COLUMNS;j++){
            printf("%c ", screen[i][j]);
        }
        printf("\r\n");
    }

    return 0;
}