#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <pthread.h>


#define QUEUE_NAME "/user_info_queue"
#define MAX_SIZE 1024
#define MSG_STOP "exit"


typedef struct {
    char name[100];
    int age;
    char phone[11];
    char image_name[1000];
} UserInput;

//global variable
UserInput userData;
pthread_mutex_t lock;
pthread_cond_t cond;

typedef struct {
    char* first_three_digit;
} DigitCheck;

int is_valid_phone_number(const char *phone) {
    DigitCheck phoneDigitCheckList[] = {
        {"090"}, // Mobi
        {"086"}, // Vina
        {"096"}, // Viettel
    };
    if (strlen(phone) != 10) {
        return 0; 
    }
    
    int amountOfNumInCheckList = sizeof(phoneDigitCheckList) / sizeof(DigitCheck);
    for (int i=0; i < amountOfNumInCheckList ; i++){
        if (strncmp(phone, phoneDigitCheckList[i].first_three_digit, 3) == 0) {
            return 1; 
        }
    }
    return 0;
}




void *thread1_working(){
    while(1) {
        // Scan data from user
        printf("Enter name: ");
        scanf("%s", userData.name);
        printf("Enter age: ");
        scanf("%d", &(userData.age));
        printf("Enter phone number: ");
        scanf("%s", userData.phone);
        printf("Enter image file name: ");        
        scanf("%s", userData.image_name);

        // Lock mutex
        pthread_mutex_lock(&lock);

        // Signal to thread2 to start
        pthread_cond_signal(&cond);

        // Unlock mutex
        pthread_mutex_unlock(&lock);

        // Exit loop :"exit"
        if(strcmp(userData.name, MSG_STOP) == 0) {
            break;
        }
    }
    
    pthread_exit(NULL);
}

void *thread2_working(){
    while(1){
        // Lock mutex
        pthread_mutex_lock(&lock);

        // Wait for thread1 alert
        pthread_cond_wait(&cond,&lock);

        // Get data and print to console
        if(strcmp(userData.name, MSG_STOP) == 0) {
            break;
        }
        if(is_valid_phone_number(userData.phone)){
            printf("User Information:\n");
            printf("Name: %s\n", userData.name);
            printf("Age: %d\n", userData.age);
            printf("Phone: %s\n", userData.phone);
            
            FILE *imageptr;
            char image_data_buffer[16]; //store 16 bytes data
            
            imageptr = fopen(userData.image_name,"rb");//read data in binary
            fread(image_data_buffer, 1, 16, imageptr); //write 1 byte 16 times into buffer
            for (int i = 0; i < 16; i++) 
            {
                printf("%02x ", image_data_buffer[i]);//print it out
            }
            printf("\n");
            fclose(imageptr);           
        } else {
            printf("Invalid phone number\n");            
        }

        // Unlock mutex
        pthread_mutex_unlock(&lock);
    }

    pthread_exit(NULL);
}


int main()
{
    pthread_t thread1, thread2;
    
    pthread_mutex_init(&lock,NULL);
    pthread_cond_init(&cond1,NULL);
    pthread_cond_init(&cond2,NULL);
    
    //create 2 thread
    pthread_create(&thread1, NULL, thread1_working,NULL);
    pthread_create(&thread2, NULL, thread2_working,NULL);    
    
    pthread_join(thread1,NULL);
    pthread_join(thread2,NULL);
    
        // destroy all
    pthread_mutex_destroy(&lock);
    pthread_cond_destroy(&cond1);
    pthread_cond_destroy(&cond2);
    
    return 0;
}




