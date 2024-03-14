#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <pthread.h>
#include <mqueue.h>

#define QUEUE_NAME "/user_info_queue"
#define MAX_SIZE 1024
#define MSG_STOP "exit"


typedef struct {
    char name[100];
    int age;
    char phone[10];
    char image_name[1000];
} UserInput;

int is_valid_phone_number(const char *phone) {
    if (strlen(phone) != 10) {
        return 0; 
    }
    if (strncmp(phone, "090", 3) != 0) {
        return 0; 
    }
    return 1;
}

void *thread1_working(){
    mqd_t myQueue1;//Create queue1
    char buffer[MAX_SIZE];//save message here
    
    myQueue1 = mq_open(QUEUE_NAME,O_WRONLY);//join queue, write-only for receiving
    UserInput userData;
    
    while(1) {
        printf("Enter name: ");
        scanf("%s", userData.name);
        printf("Enter age: ");
        scanf("%d", &(userData.age));
        printf("Enter phone number: ");
        scanf("%s", userData.phone);
        printf("Enter image file name: ");        
        scanf("%s", userData.image_name);
        
        memcpy(buffer, &userData, sizeof(userData));//copy userData to buffer
        mq_send(myQueue1, buffer, MAX_SIZE, 0);//send to queue
        
        //exit loop :"exit"
        if(strcmp(userData.name, MSG_STOP) == 0) {
            break;
        }
    }
    
    mq_close(myQueue1);//stop queue
    pthread_exit(NULL);
    
}

void *thread2_working(){
    mqd_t myQueue2;//Create queue2
    char buffer[MAX_SIZE];//receive message here
    myQueue2 = mq_open(QUEUE_NAME, O_RDONLY);//join queue, read-only
    
    while(1){
        int bytes_read;
        bytes_read = mq_receive(myQueue2, buffer, MAX_SIZE,NULL);
        UserInput *userData_receive = (UserInput *) buffer;//type cast to UserInput type

        //exit thread2
        if(strcmp(userData_receive->name, MSG_STOP) == 0) {
            break;
        }
        
        //check is_valid_phone_number
        if(is_valid_phone_number(userData_receive->phone)){
            printf("User Information:\n");
            printf("Name: %s\n", userData_receive->name);
            printf("Age: %d\n", userData_receive->age);
            printf("Phone: %s\n", userData_receive->phone);
            
            //open and store file data
            FILE *imageptr;
            char image_data_buffer[16]; //store 16 bytes data
            
            imageptr = fopen(userData_receive->image_name,"rb");//read data in binary
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

    }
    mq_close(myQueue2);
    mq_unlink(QUEUE_NAME);
    pthread_exit(NULL);
}


int main()
{
    pthread_t thread1, thread2;
    mq_unlink(QUEUE_NAME);//unlink all queue before running
    
    //queue propertises
    struct mq_attr attributes;
    attributes.mq_flags = 0;//default
    attributes.mq_maxmsg = 10;//max 10 message
    attributes.mq_msgsize = MAX_SIZE;//size of message
    attributes.mq_curmsgs = 0;//no message at start

    //create queue with above propertises
    mqd_t main_message_queue = mq_open(QUEUE_NAME, O_CREAT, 0644, &attributes);
    
    //create 2 thread
    pthread_create(&thread1, NULL, thread1_working,NULL);
    pthread_create(&thread2, NULL, thread2_working,NULL);    
    
    pthread_join(thread1,NULL);
    pthread_join(thread2,NULL);
    
    return 0;
}

