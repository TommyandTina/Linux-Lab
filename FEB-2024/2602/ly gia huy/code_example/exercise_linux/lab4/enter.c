#include <stdio.h>
#include <stdlib.h>
#include <fcntl.h>
#include <unistd.h>

void test_operations(char operation) {
    int fd;
    char buf[100];

    fd = open("/dev/mychardev-0", O_RDWR);
    if (fd < 0) {
        perror("Failed to open the device");
        exit(EXIT_FAILURE);
    }

    switch (operation) {
        case 'o': // Mở thiết bị
            printf("Opening the device...\n");
            break;
        
        case 'w': // Ghi dữ liệu vào thiết bị
            printf("Writing data to the device...\n");
            write(fd, "Test data", sizeof("Test data"));
            break;
        
        case 'r': // Đọc dữ liệu từ thiết bị
            printf("Reading data from the device...\n");
            read(fd, buf, sizeof(buf));
            printf("Data read from the device: %s\n", buf);
            break;
        
        case 'c': // Đóng thiết bị
            printf("Closing the device...\n");
            break;
        
        default:
            printf("Invalid operation\n");
            break;
    }

    // Đóng thiết bị
    close(fd);
}

int main(int argc, char *argv[]) {
    if (argc != 2) {
        printf("Usage: %s <operation>\n", argv[0]);
        printf("Operation: o (open), w (write), r (read), c (close)\n");
        return EXIT_FAILURE;
    }

    char operation = argv[1][0];
    test_operations(operation);

    return EXIT_SUCCESS;
}
