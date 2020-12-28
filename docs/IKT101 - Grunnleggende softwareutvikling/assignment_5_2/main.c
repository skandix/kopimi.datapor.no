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