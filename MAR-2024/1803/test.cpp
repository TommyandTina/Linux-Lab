#include <stdio.h>
#include <stdlib.h>

int main() {
    FILE *file;
    unsigned char *data;
    int width = 6; // �? r?ng c?a h�nh ?nh
    int height = 6; // �? cao c?a h�nh ?nh
    int num_pixels = width * height * 2; // S? lu?ng pixel (YUV444 c� 3 th�nh ph?n m�u), nv16 co 2 thanh phan mau
//_padded
    // M? t?p h�nh ?nh YUV444 d? d?c
    file = fopen("6_6_nv16_padded.yuv", "rb");
    if (!file) {
        fprintf(stderr, "Cannot open\n");
        return 1;
    }

    // C?p ph�t b? nh? cho d? li?u h�nh ?nh
    data = (unsigned char *)malloc(num_pixels);
    if (!data) {
        fprintf(stderr, "error\n");
        fclose(file);
        return 1;
    }

    // �?c d? li?u t? t?p h�nh ?nh
    fread(data, sizeof(unsigned char), num_pixels, file);

    // ��ng t?p h�nh ?nh
    fclose(file);

     //Xu?t d? li?u t? h�nh ?nh
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

    // Gi?i ph�ng b? nh?
    free(data);

    return 0;
}

