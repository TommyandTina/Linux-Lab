#ifndef STACK_H
#define STACK_H

#include <stdlib.h>
#include <assert.h>
#include "data_structures.h"

typedef struct Stack {
    Node *top;
    int count;
} Stack;

Stack* Stack_create() {
    Stack *stack = malloc(sizeof(Stack));
    assert(stack != NULL);
    stack->top = NULL;
    stack->count = 0;
    return stack;
}

void Stack_destroy(Stack *stack) {
    Node *current = stack->top;
    while (current != NULL) {
        Node *temp = current;
        current = current->next;
        free(temp);
    }
    free(stack);
}

void Stack_push(Stack *stack, void *data) {
    Node *node = malloc(sizeof(Node));
    assert(node != NULL);
    node->data = data;
    node->next = stack->top;
    stack->top = node;
    stack->count++;
}

void* Stack_pop(Stack *stack) {
    if (stack->top == NULL) return NULL;

    Node *node = stack->top;
    void *data = node->data;
    stack->top = node->next;
    free(node);
    stack->count--;
    return data;
}

void* Stack_peek(Stack *stack) {
    if (stack->top == NULL) return NULL;
    return stack->top->data;
}

int Stack_count(Stack *stack) {
    return stack->count;
}

#endif // STACK_H
