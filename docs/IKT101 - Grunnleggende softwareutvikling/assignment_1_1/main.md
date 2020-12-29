main.c
```c
#include <stdio.h>

int main() {
    printf("Hello, Christian!\n");
    return 0;
}
```
CMakeLists.txt
```cmake
cmake_minimum_required(VERSION 3.14)
project(assignment_1_1 C)

set(CMAKE_C_STANDARD 99)

add_executable(assignment_1_1 main.c)
```