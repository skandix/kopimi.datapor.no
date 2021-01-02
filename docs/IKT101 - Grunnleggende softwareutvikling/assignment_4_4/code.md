# main.c
```c
#include <stdio.h>
#include <string.h>

#define STRLNG 100


int main() {

    char user_input[STRLNG];
    int i, len, freq[26];

    printf("Please type a string:");
    gets(user_input);

    len = strlen(user_input);

    for (i = 0; i < 26; ++i) {
        freq[i] = 0;
    }

    /* Find total number of occurrences of each character */
    for(i=0; i<len; i++)
    {
        /* If the current character is lowercase alphabet */
        if(user_input[i]>='a' && user_input[i]<='z')
        {
            freq[user_input[i] - 97]++;
        }
        else if(user_input[i]>='A' && user_input[i]<='Z')
        {
            freq[user_input[i] - 65]++;
        }
    }

    for(i=0; i<26; i++)
    {
        if(freq[i] != 0)
        {
            printf("'%c' = %d\n", (i + 97), freq[i]);
        }
    }

    return 0;
}
```
## main.c
```c
#include <stdio.h>
#include <string.h>

#define STRLNG 100


int main() {

    char user_input[STRLNG];
    int i, len, freq[26];

    printf("Please type a string:");
    gets(user_input);

    len = strlen(user_input);

    for (i = 0; i < 26; ++i) {
        freq[i] = 0;
    }

    /* Find total number of occurrences of each character */
    for(i=0; i<len; i++)
    {
        /* If the current character is lowercase alphabet */
        if(user_input[i]>='a' && user_input[i]<='z')
        {
            freq[user_input[i] - 97]++;
        }
        else if(user_input[i]>='A' && user_input[i]<='Z')
        {
            freq[user_input[i] - 65]++;
        }
    }

    for(i=0; i<26; i++)
    {
        if(freq[i] != 0)
        {
            printf("'%c' = %d\n", (i + 97), freq[i]);
        }
    }

    return 0;
}
```
