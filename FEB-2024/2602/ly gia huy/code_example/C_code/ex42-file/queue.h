#ifndef QUEUE_H
#define QUEUE_H

#include <stdlib.h>
#include <assert.h>
#include "data_structures.h"

typedef struct Queue {
    Node *front;
    Node *rear;
    int count;
} Queue;

Queue* Queue_create() {
    Queue *queue = malloc(sizeof(Queue));
    assert(queue != NULL);
    queue->front = NULL;
    queue->rear = NULL;
    queue->count = 0;
    return queue;
}

void Queue_destroy(Queue *queue) {
    Node *current = queue->front;
    while (current != NULL) {
        Node *temp = current;
        current = current->next;
        free(temp);
    }
    free(queue);
}

void Queue_send(Queue *queue, void *data) {
    Node *node = malloc(sizeof(Node));
    assert(node != NULL);
    node->data = data;
    node->next = NULL;

    if (queue->rear != NULL) {
        queue->rear->next = node;
    } else {
        queue->front = node;
    }
    queue->rear = node;
    queue->count++;
}

void* Queue_recv(Queue *queue) {
    if (queue->front == NULL) return NULL;

    Node *node = queue->front;
    void *data = node->data;
    queue->front = node->next;
    
    if (queue->front == NULL) {
        queue->rear = NULL;
    }

    free(node);
    queue->count--;
    return data;
}

void* Queue_peek(Queue *queue) {
    if (queue->front == NULL) return NULL;
    return queue->front->data;
}

int Queue_count(Queue *queue) {
    return queue->count;
}

#endif // QUEUE_H
