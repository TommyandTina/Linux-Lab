#include <stdio.h>
#include <stdlib.h>
#include <fcntl.h>
#include <unistd.h>
#include <string.h>

#define DEVICE_FILE "/dev/mychardev-0"

int main() {
    int fd;
    char choice;
    char buffer[100];
    ssize_t bytes_read, bytes_written;

    // Open the device file
    fd = open(DEVICE_FILE, O_RDWR);
    if (fd < 0) {
        perror("Failed to open the device file");
        return -1;
    }

    while (1) {
        printf("Enter operation:\n");
        printf("o: Open\n");
        printf("w: Write\n");
        printf("r: Read\n");
        printf("c: Close\n");
        printf("q: Quit\n");
        printf("Choice: ");
        scanf(" %c", &choice);

        switch (choice) {
            case 'o':
                // Open the device file
                if (fd < 0) {
                    fd = open(DEVICE_FILE, O_RDWR);
                    if (fd < 0) {
                        perror("Failed to open the device file");
                    } else {
                        printf("Device file opened successfully.\n");
                    }
                } else {
                    printf("Device file is already open.\n");
                }
                break;

            case 'w':
                // Write to the device file
                printf("Enter data to write: ");
                scanf("%s", buffer);
                bytes_written = write(fd, buffer, strlen(buffer));
                if (bytes_written < 0) {
                    perror("Failed to write to the device file");
                } else {
                    printf("Data written to device: %s\n", buffer);
                }
                break;

            case 'r':
                // Read from the device file
                bytes_read = read(fd, buffer, sizeof(buffer));
                if (bytes_read < 0) {
                    perror("Failed to read from the device file");
                } else {
                    buffer[bytes_read] = '\0'; // Null terminate the string
                    printf("Data read from device: %s\n", buffer);
                }
                break;

            case 'c':
                // Close the device file
                if (fd >= 0) {
                    close(fd);
                    printf("Device file closed.\n");
                    fd = -1; // Reset file descriptor
                } else {
                    printf("Device file is already closed.\n");
                }
                break;

            case 'q':
                // Quit the program
                if (fd >= 0) {
                    close(fd);
                }
                printf("Exiting...\n");
                return 0;

            default:
                printf("Invalid choice. Please try again.\n");
        }
    }

    return 0;
}
