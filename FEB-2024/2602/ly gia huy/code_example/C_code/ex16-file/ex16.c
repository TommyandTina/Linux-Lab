/* Exercise 16: Structs And Pointers To Them */

// point a pointer at struct
// make sense of internal memory structures
// raw memory using malloc 

/* lưu ý:
    Cần cấp phát bộ nhớ cho con trỏ char *name;
    Nhớ free bộ nhớ
    dùng %p để biết vị trí mem của struct 
*/
#include <stdio.h>
#include <assert.h>
#include <stdlib.h>
#include <string.h>

struct Person {
    char *name;
    int age;
    int height;
    int weight;
};

struct  Person *Person_create(char *name, int age, int height, int weight)
{
    struct Person *who = malloc(sizeof(struct Person));
    assert(who != NULL);

    who->name = malloc(strlen(name) + 1);
    assert(who->name != NULL);

    strncpy(who->name, name, sizeof(name));
    who->age = age;
    who->height = height;
    who->weight = weight;

    return who;
}

void Person_destroy(struct Person *who)
{
    assert(who != NULL);

    free(who->name);
    free(who);
}

void Person_print(struct Person *who)
{
    printf("Name: %s\n", who->name);
    printf("\tAge: %d\n", who->age);
    printf("\tHeight: %d\n", who->height);
    printf("\tWeight: %d\n", who->weight);
}


int main(int argc, char *argv[])
{
    //make two people structures
    struct Person *joe = Person_create("Joe Alex", 32, 64, 140);
    struct Person *frank = Person_create("Frank Blank", 20, 72, 180);

    //print them out and where they are in memory
    printf("joe is at mem location %p:\n", joe);
    Person_print(joe);
    printf("frank is at mem location %p:\n", frank);
    Person_print(frank);

    //make everyone age 20 years and print them again
    joe->age += 20;
    joe->height -= 2;
    joe->weight += 40;
    Person_print(joe);

    frank->age += 20;
    frank->weight += 20;
    Person_print(frank);

    // destroy them both so we clean up
    Person_destroy(joe);
    Person_destroy(frank);

    return 0; 
}












