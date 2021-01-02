# main.c
```c
#include <stdio.h>
#include <string.h>

#define STRLNG 100

char user_input1[STRLNG];
char user_input2[STRLNG];

void str()
{


    gets(user_input1);
    gets(user_input2);
    user_input1[strlen(user_input1)] = 0;
    user_input2[strlen(user_input2)] = 0;

    if (strcmp(user_input1,user_input2) == 0)
        printf("Your strings are equal!\n");
    else
        printf("Your strings are not equal!\n");

    if (strstr(user_input1, user_input2) != 0)
        printf("Is a substring!\n");
    else if (strstr(user_input2, user_input1) != 0)
        printf("Is a substring");
    else
        printf("Is not a substring!\n");


}


int main() {

    printf("Please type in two strings:");

    str();


    return 0;
}
```
## main.c
```c
#include <stdio.h>
#include <string.h>

#define STRLNG 100

char user_input1[STRLNG];
char user_input2[STRLNG];

void str()
{


    gets(user_input1);
    gets(user_input2);
    user_input1[strlen(user_input1)] = 0;
    user_input2[strlen(user_input2)] = 0;

    if (strcmp(user_input1,user_input2) == 0)
        printf("Your strings are equal!\n");
    else
        printf("Your strings are not equal!\n");

    if (strstr(user_input1, user_input2) != 0)
        printf("Is a substring!\n");
    else if (strstr(user_input2, user_input1) != 0)
        printf("Is a substring");
    else
        printf("Is not a substring!\n");


}


int main() {

    printf("Please type in two strings:");

    str();


    return 0;
}
```
