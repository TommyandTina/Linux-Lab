#include <stdio.h>
#include <stdlib.h>
#include <string.h>

//this code is to add padding and calculate stride and size 

int main() {
    int width = 4000; // replace by image width
    int height = 2160; // replace by image height
//    int bpp = 8*3; // bits per pixel for: NV16 format - 8, RGB24 - 24
	int align = 256; //must align with __ value
	int num_of_planar = 3;//nv16 has 2, rgb24 has 3
    // Calculate stride, align-1 is to round up stride to align with 256 
    int stride = (((width + align-1) / align)*align)*num_of_planar;

    // Calculate size (in bytes) and print out stride and size - EX2_1
    int size = stride * height;
    printf("Stride: %d bits\n", stride);
    printf("Width (in pixels): %d bits\n", stride/num_of_planar);    
    printf("Size: %d bits\n", size);

//EX2_2 : 

    // Allocate memory for the buffer: 'image' - which align with 'stride' inside 'size'
    unsigned char *image = malloc(size);
    if (image == NULL) {
        printf("Failed to allocate memory for image\n");
        return 1;
    }

    // Initialize the image data to 0
    memset(image, 0x0, size);

    // Open the NV16 file
    FILE *file = fopen("imageprocessing_requirement2_4000_2160.rgb", "rb");
    if (file == NULL) {
        printf("Failed to open file\n");
        free(image);
        return 1;
    }

    // Read the image data from the file
    for (int i = 0; i < height; ++i) {
        if (fread(image + i * stride, 1, width*num_of_planar, file) != width*num_of_planar) {
            printf("Failed to read image data from file\n");
            free(image);
            fclose(file);
            return 1;
        }
    }
    
//    for (int i = height; i < height*num_of_planar; ++i) {
//        if (fread(image + i * stride, 1, width/2, file) != width/2) {
//            printf("Failed to read image data from file2\n");
//            free(image);
//            fclose(file);
//            return 1;
//        }
//        if (fread(image + i * stride + width/2 + (stride-width+1)/2, 1, width/2, file) != width/2) {
//            printf("Failed to read image data from file3\n");
//            free(image);
//            fclose(file);
//            return 1;
//        }
//    }

    // Close the input file
    fclose(file);

    // Open the output file
    file = fopen("imageprocessing_requirement2_4000_2160_padded.rgb", "wb");
    if (file == NULL) {
        printf("Failed to open output file\n");
        free(image);
        return 1;
    }

    // Write the image data to the file
    if (fwrite(image, 1, size, file) != size) {
        printf("Failed to write image data to file\n");
    }

    // Clean up
    free(image);
    fclose(file);

    return 0;
}

