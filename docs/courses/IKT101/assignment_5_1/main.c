#include <stdio.h>

#define String_length 100
int i, n;


void info(){

    struct stdinfo student;

    printf("Please enter your student id:");
    scanf("%i", &student.student_id);

    getchar();
    printf("Please enter your name:");
    fgets(student.name, String_length, stdin);

    printf("Please enter your age:");
    scanf("%i", &student.age);
}

void printstudentinfo() {

    struct stdinfo student;
    printf("Student id: %d", student.student_id);
    printf("\nStudent name: %s", student.name);
    printf("Student name: %d", student.age);


}

int main() {

    info();
    printstudentinfo();

    return 0;
}