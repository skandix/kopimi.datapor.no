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
