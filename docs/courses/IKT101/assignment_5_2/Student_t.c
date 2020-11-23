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