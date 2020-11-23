#include <stdio.h>
#include <string.h>
#include <stdbool.h>

bool IsPalRec(char word1[], int s, int e) {

    if (s == e)
        return true;

    if (word1[s] != word1[e])
        return false;

    if (s < e + 1)
        return IsPalRec(word1, s + 1, e - 1);

    return true;
}

bool is_palindrome(char word1[]){
    int n = strlen(word1);

    if (n == 0)
        return true;

    return IsPalRec(word1,0,n-1);

}



void string_revers(char *x, int begin, int end){

    char c;
    if (begin >= end)
        return;

    c = *(x+begin);
    *(x+begin) = *(x+end);
    *(x+end) = c;

    string_revers(x, ++begin, --end);
}

int main() {

    char word1[100];
    char word2[100];

    printf("Please type a word: \n");
    fgets(word1, 100, stdin);


    printf("The word contains %i letters\n", strlen(word1) - 1);
    strcpy(word2,word1);

    if(is_palindrome(word1))
        printf("The word is a palindrome\n");
    else
        printf("The word is not a palindrome\n");


    string_revers(word2, 0, strlen(word2)-1);
    printf("The reverse of you word is %s",word2);

    return 0;
}

