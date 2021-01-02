# main.c
```c
#include <stdio.h>
#include <string.h>
#include <ctype.h>

#define STRING_LENGTH 100

void upper_string(char s[])
{
    int c = 0;

    while (s[c] != '\0'){
        if(s[c] >= 'a' && s[c] <= 'z'){
            s[c] = s[c] - 32;
        }
        c++;
    }
}

void lower_string(char s[]){
    int c = 0;

    while (s[c] != '\0'){
        if(s[c] >= 'A' && s[c] <= 'Z'){
            s[c] = s[c] + 32;
        }
        c++;
    }
}

int main() {

    char user_input[STRING_LENGTH] = { 0 };
    char user_input2[STRING_LENGTH];
    char user_input3[STRING_LENGTH];
    char left[STRING_LENGTH], right[STRING_LENGTH];
    int length, mid, j , k;

    printf("Please type in a string: \n");

    fgets(user_input, STRING_LENGTH, stdin);

    length = strlen(user_input);
    mid = length/2;
    for ( j = 0; j < mid; j++) {
        left[j] = user_input[j];
    }
    left[j] = '\0';

    for ( j = mid, k = 0; j <= length; j++, k++) {
        right[k] = user_input[j];
    }

    strcpy(user_input2,user_input);
    strcpy(user_input3, user_input);

    upper_string(user_input3);
    lower_string(user_input2);

    printf("You typed the string: %s\n", user_input);
    printf("Here is your string in uppercase: %s\n", user_input3);
    printf("Here is your string in lowercase: %s\n", user_input2);
    printf("The string split in two: %s-%s", left, right);





    return 0;
}
```
## main.c
```c
#include <stdio.h>
#include <string.h>
#include <ctype.h>

#define STRING_LENGTH 100

void upper_string(char s[])
{
    int c = 0;

    while (s[c] != '\0'){
        if(s[c] >= 'a' && s[c] <= 'z'){
            s[c] = s[c] - 32;
        }
        c++;
    }
}

void lower_string(char s[]){
    int c = 0;

    while (s[c] != '\0'){
        if(s[c] >= 'A' && s[c] <= 'Z'){
            s[c] = s[c] + 32;
        }
        c++;
    }
}

int main() {

    char user_input[STRING_LENGTH] = { 0 };
    char user_input2[STRING_LENGTH];
    char user_input3[STRING_LENGTH];
    char left[STRING_LENGTH], right[STRING_LENGTH];
    int length, mid, j , k;

    printf("Please type in a string: \n");

    fgets(user_input, STRING_LENGTH, stdin);

    length = strlen(user_input);
    mid = length/2;
    for ( j = 0; j < mid; j++) {
        left[j] = user_input[j];
    }
    left[j] = '\0';

    for ( j = mid, k = 0; j <= length; j++, k++) {
        right[k] = user_input[j];
    }

    strcpy(user_input2,user_input);
    strcpy(user_input3, user_input);

    upper_string(user_input3);
    lower_string(user_input2);

    printf("You typed the string: %s\n", user_input);
    printf("Here is your string in uppercase: %s\n", user_input3);
    printf("Here is your string in lowercase: %s\n", user_input2);
    printf("The string split in two: %s-%s", left, right);





    return 0;
}
```
