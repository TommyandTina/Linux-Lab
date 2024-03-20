#include <stdio.h>
#include <stdlib.h>

int main() {
    FILE *file;
    unsigned char *data;
    int width = 6; // Ð? r?ng c?a hình ?nh
    int height = 6; // Ð? cao c?a hình ?nh
    int num_pixels = width * height * 2; // S? lu?ng pixel (YUV444 có 3 thành ph?n màu), nv16 co 2 thanh phan mau
//_padded
    // M? t?p hình ?nh YUV444 d? d?c
    file = fopen("6_6_nv16_padded.yuv", "rb");
    if (!file) {
        fprintf(stderr, "Cannot open\n");
        return 1;
    }

    // C?p phát b? nh? cho d? li?u hình ?nh
    data = (unsigned char *)malloc(num_pixels);
    if (!data) {
        fprintf(stderr, "error\n");
        fclose(file);
        return 1;
    }

    // Ð?c d? li?u t? t?p hình ?nh
    fread(data, sizeof(unsigned char), num_pixels, file);

    // Ðóng t?p hình ?nh
    fclose(file);

     //Xu?t d? li?u t? hình ?nh
    for (int i = 0; i < num_pixels; i++) {
    	static int each_line = 0;
		static int six_line = 0;
//    	if(i<(num_pixels/3)){
    		printf("%3d ", data[i]);
    		each_line++;
//		} else {
//			if(i%2==0){
//				printf("%3d ", data[i]);
//				each_line++;
//			}
//		}
        	
        if ((each_line) % width == 0) 
		{
            printf("\n");  
            six_line ++;
				if ((six_line) % height == 0) 
				{
            		printf("\n");  
            		six_line = 0;
        		}	            
        }
    }
    printf("\n\n");

    // Gi?i phóng b? nh?
    free(data);

    return 0;
}

