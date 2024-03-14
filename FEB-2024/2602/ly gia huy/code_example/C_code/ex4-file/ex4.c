/* Exercise 4: Introducing Valgrind */

// Valgrind is a program that runs your programs
// reports on all of the horrible mistakes you made

/* perform the following steps
1. curl -O https://sourceware.org/pub/valgrind/valgrind-3.22.0.tar.bz2
2. md5sum valgrind-3.22.0.tar.bz2
3. tar -xjvf valgrind-3.22.0.tar.bz2
4. cd valgrind-3.22.0
5. ./configure
6. make
7. sudo make install  */

//  run with "make ex4 -> valgrind ./ex4"
#include <stdio.h>

int main()
{
    int age = 10;
    int height;

    printf("I am %d years old.\n");
    printf("I am %d inches tall.\n", height);

    return 0;
}
