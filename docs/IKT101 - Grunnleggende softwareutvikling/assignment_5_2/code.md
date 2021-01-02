# Student_t.h
```h
//
// Created by Paal on 20/09/2019.
//

#ifndef ASSIGNMENT_5_2_STUDENT_T_H
#define ASSIGNMENT_5_2_STUDENT_T_H

typedef struct stdinfo{
    int student_id;
    char name[100];
    int age;
}student_t;

void info(student_t student);
void printstudentinfo(student_t student);
#endif //ASSIGNMENT_5_2_STUDENT_T_H

```
# main.c
```c
#include <stdio.h>
#include <string.h>
#include "Student_t.h"

int main() {

    student_t student;
    int user_input = 0;
    int j = 1;

    memset(&student, 0, sizeof(student));

    if (user_input != 3) {

        printf("please chose an option: \n");

        printf("1: Student information.\n");
        printf("2: Write you own student information.\n");
        printf("3: exit.\n");
        scanf("%i", &user_input);

        if (user_input < 4) {
            if (user_input == 1) {

                student.student_id = "%i";
                strcpy(student.name, "%s");
                student.age = "%i";

                printstudentinfo(student);

            } else if (user_input == 2) {
                for (int i = 0; i < 1; ++i) {
                    printf("Id:\n");
                    scanf(user_input);
                }
                for (int k = 0; k < 1; ++k) {
                    printf("Name:\n");
                    gets(user_input);

                }
                for (int l = 0; l < 1; ++l) {
                    printf("age:\n");
                    scanf(user_input);
                }
                info(student);


            }
            user_input++;
        }
    }
    return 0;
}
```
# Student_t.c
```c
//
// Created by Paal on 20/09/2019.
//

#include "Student_t.h"
#include <stdio.h>

void printstudentinfo(student_t student) {

    FILE *file = fopen("student_read.txt", "r");

    if (!file){
        printf("Failed to open file.\n");

    }

    int sum = 0;

    while (!feof(file)){
        int value = 0;
        char string[100] = { 0 };

        fscanf(file, "%i", &value);
        fgets(string, 0, stdin);
        fscanf(file, "%i", &value);

        sum += value;
    }
    fclose(file);

    printf("Student info\n", student);
    printf("id: %i\n", student.student_id);
    printf("Name: %s\n", student.name);
    printf("Age: %i\n", student.age);
    getchar();

}

void info(student_t student)
{
    FILE* file2 = fopen("student_write.txt", "w");

    fprintf(file2, "Id: %i\n");
    fprintf(file2, "Name: %d\n");
    fprintf(file2, "Age: %i\n");

    fclose(file2);
}
```
## Student_t.h
```h
//
// Created by Paal on 20/09/2019.
//

#ifndef ASSIGNMENT_5_2_STUDENT_T_H
#define ASSIGNMENT_5_2_STUDENT_T_H

typedef struct stdinfo{
    int student_id;
    char name[100];
    int age;
}student_t;

void info(student_t student);
void printstudentinfo(student_t student);
#endif //ASSIGNMENT_5_2_STUDENT_T_H

```
## main.c
```c
#include <stdio.h>
#include <string.h>
#include "Student_t.h"

int main() {

    student_t student;
    int user_input = 0;
    int j = 1;

    memset(&student, 0, sizeof(student));

    if (user_input != 3) {

        printf("please chose an option: \n");

        printf("1: Student information.\n");
        printf("2: Write you own student information.\n");
        printf("3: exit.\n");
        scanf("%i", &user_input);

        if (user_input < 4) {
            if (user_input == 1) {

                student.student_id = "%i";
                strcpy(student.name, "%s");
                student.age = "%i";

                printstudentinfo(student);

            } else if (user_input == 2) {
                for (int i = 0; i < 1; ++i) {
                    printf("Id:\n");
                    scanf(user_input);
                }
                for (int k = 0; k < 1; ++k) {
                    printf("Name:\n");
                    gets(user_input);

                }
                for (int l = 0; l < 1; ++l) {
                    printf("age:\n");
                    scanf(user_input);
                }
                info(student);


            }
            user_input++;
        }
    }
    return 0;
}
```
## Student_t.c
```c
//
// Created by Paal on 20/09/2019.
//

#include "Student_t.h"
#include <stdio.h>

void printstudentinfo(student_t student) {

    FILE *file = fopen("student_read.txt", "r");

    if (!file){
        printf("Failed to open file.\n");

    }

    int sum = 0;

    while (!feof(file)){
        int value = 0;
        char string[100] = { 0 };

        fscanf(file, "%i", &value);
        fgets(string, 0, stdin);
        fscanf(file, "%i", &value);

        sum += value;
    }
    fclose(file);

    printf("Student info\n", student);
    printf("id: %i\n", student.student_id);
    printf("Name: %s\n", student.name);
    printf("Age: %i\n", student.age);
    getchar();

}

void info(student_t student)
{
    FILE* file2 = fopen("student_write.txt", "w");

    fprintf(file2, "Id: %i\n");
    fprintf(file2, "Name: %d\n");
    fprintf(file2, "Age: %i\n");

    fclose(file2);
}
```
