/* Exercise 15: Pointers Dreaded Pointers */

/* Lưu ý
    để trỏ đến một mảng dùng *p
    để trỏ đến một con trỏ khác **p
    dù *p hay **p thì in giá trị vẫn là *(p + i) 

    type *ptr
    "a pointer of type named ptr"
    *ptr
    "the value of whatever ptr is pointed at"
    *(ptr + i)
    "the value of (whatever ptr is pointed at plus i)"
    &thing
    "the address of thing"
    type *ptr = &thing
    "a pointer of type named ptr set to the address of thing"
    ptr++
    "increment where ptr points"
*/
#include <stdio.h>

int main(int argc, char *argv[])
{
    int ages[] = {23, 43, 12, 89, 2};
    char *names[] = {
        "Alan", "Frank",
        "Mary", "John", "Lisa"
    };

    // safely get the size of ages
    int count = sizeof(ages)/sizeof(int);
    int i = 0;

    for( i = 0; i < count; i++){
        printf("%s has %d years alive.\n", names[i], ages[i]);
    }

    printf("--\n");

    int *cur_age = ages;
    char **cur_name = names;

    //second way using pointer
    for( i = 0; i < count; i++){
        printf("%s is %d years old.\n", *(cur_name + i), *(cur_age + i));
    }

    printf("--\n");

    //thirds way, pointers are just arrays
    for(i = 0; i < count; i++){
        printf("%s is %d years old again.\n", cur_name[i], cur_age[i]);
    }

    printf("--\n");

    //four way with pointers in a stupid complex way
    for(cur_name = names, cur_age =ages; (cur_age - ages) < count; cur_name++, cur_age++){
        printf("%s lived %d years so far.\n", *cur_name, *cur_age);
    }

    return 0;
}