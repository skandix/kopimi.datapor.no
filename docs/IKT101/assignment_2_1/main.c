#include <stdio.h>

int main() {

    float sum;
    float num;
    int num_given = 0;
    float average = 0;

    printf("Here you need to enter 5 numbers\n or more until 0 is given\n");
    printf("Please enter your numbers:\n");

    while (num > 0 || num_given == 0){
        scanf("%f", &num);

        sum +=num;

        num_given++;
    }

    average = sum / (num_given - 1);

    printf("Count: %i\n", (num_given-1));
    printf("Sum: %g\n", sum);
    printf("Average: %g\n", average);

    return 0;

}