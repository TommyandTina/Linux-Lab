#include <stdio.h>
#include <stdlib.h>

int main() {
    int width = 6; // replace with your image width
    int height = 6; // replace with your image height
    int bpp = 8; // 8 bits per pixel for NV16 format, 24bits per pixel for RGB24

    // Calculate stride (in bytes), assuming each row starts at an address which is a multiple of 4 bytes, add 31 to make sure the result will round up
    int stride = ((width * bpp + 31) / 32) * 4;

    // Calculate size (in bytes)
    int size = stride * height;

    printf("Stride: %d bytes\n", stride);
    printf("Size: %d bytes\n", size);

    // Open the NV16 file
    FILE *file = fopen("6_6_444.yuv", "rb");
    if (file == NULL) {
        printf("Failed to open file\n");
        return 1;
    }

    // Allocate memory for the image
    unsigned char *image = (unsigned char *)malloc(size);
    if (image == NULL) {
        printf("Failed to allocate memory for image\n");
        fclose(file);
        return 1;
    }

    // Read the image data from the file
    size_t bytesRead = fread(image, 1, size, file);
    if (bytesRead != size) {
        printf("Failed to read image data from file\n");
        free(image);
        fclose(file);
        return 1;
    }

    // At this point, 'image' contains the NV16 image data and can be used for further processing

    // Clean up
    free(image);
    fclose(file);

    return 0;
}

