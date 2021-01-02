# main.c
```c
#include <stdio.h>
#include <stdlib.h>

int user_input[10];
int sum;
float average = 0;
int minimum = 100;
int maximum = -100;
int median;

void Sum () {
    printf("Please type in 10 numbers: \n");
    for (int i = 0; i < 10; i++) {

        scanf("%i", &user_input[i]);
        sum += user_input[i];

        if (user_input[i] > maximum)
        {
            maximum = user_input[i];
        }
        if (user_input[i] < minimum)
        {
            minimum = user_input[i];
        }
    }

    average = (float)sum / 10;
}

int compare(const void * a, const void * b){
    return (*(int *)a - *(int *)b);
}
void sorter()
{
    qsort(user_input, 10, sizeof(int), compare);

    printf("Sorted: \n");
    for (int i = 0; i < 10 ; i++) {
        printf("%d\n", user_input[i]);
    }

}
int main() {
    Sum();


    median = (user_input[4] + user_input[5])/2;
    printf("Sum: %i\n",sum);
    printf("Average: %g\n", average);
    printf("Maximum: %i\n", maximum);
    printf("Minimum: %i\n", minimum);
    printf("Median: %d\n", median);
    sorter();

    return 0;
}
```
## main.c
```c
#include <stdio.h>
#include <stdlib.h>

int user_input[10];
int sum;
float average = 0;
int minimum = 100;
int maximum = -100;
int median;

void Sum () {
    printf("Please type in 10 numbers: \n");
    for (int i = 0; i < 10; i++) {

        scanf("%i", &user_input[i]);
        sum += user_input[i];

        if (user_input[i] > maximum)
        {
            maximum = user_input[i];
        }
        if (user_input[i] < minimum)
        {
            minimum = user_input[i];
        }
    }

    average = (float)sum / 10;
}

int compare(const void * a, const void * b){
    return (*(int *)a - *(int *)b);
}
void sorter()
{
    qsort(user_input, 10, sizeof(int), compare);

    printf("Sorted: \n");
    for (int i = 0; i < 10 ; i++) {
        printf("%d\n", user_input[i]);
    }

}
int main() {
    Sum();


    median = (user_input[4] + user_input[5])/2;
    printf("Sum: %i\n",sum);
    printf("Average: %g\n", average);
    printf("Maximum: %i\n", maximum);
    printf("Minimum: %i\n", minimum);
    printf("Median: %d\n", median);
    sorter();

    return 0;
}
```
