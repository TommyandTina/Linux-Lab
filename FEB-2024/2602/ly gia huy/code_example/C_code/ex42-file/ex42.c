/* Exercise 42: Stacks and Queues */

#include <stdio.h>
#include "stack.h"
#include "queue.h"

void test_stack() {
    printf("Testing Stack\n");
    Stack *stack = Stack_create();
    Stack_push(stack, "First");
    Stack_push(stack, "Second");
    Stack_push(stack, "Third");

    printf("Expected count is 3, Actual count: %d\n", Stack_count(stack));

    printf("Popping...\n");
    while (Stack_count(stack) > 0) {
        char *value = Stack_pop(stack);
        printf("%s\n", value);
    }

    Stack_destroy(stack);
}

void test_queue() {
    printf("Testing Queue\n");
    Queue *queue = Queue_create();
    Queue_send(queue, "First");
    Queue_send(queue, "Second");
    Queue_send(queue, "Third");

    printf("Expected count is 3, Actual count: %d\n", Queue_count(queue));

    printf("Receiving...\n");
    while (Queue_count(queue) > 0) {
        char *value = Queue_recv(queue);
        printf("%s\n", value);
    }

    Queue_destroy(queue);
}

int main() {
    test_stack();
    test_queue();
    return 0;
}
