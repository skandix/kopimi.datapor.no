#include <stdio.h>

double sum(double d1, double d2) { return d1 + d2; }
//void sum(double d1, double d2) { return d1 + d2; }
//double sum(double d1, double d2) { d1 + d2;}
//void sum(double d1, double d2) { sum = d1 + d2; }

int main() {

    double total = sum(5,3);
    printf("%g",total);

    return 0;
}