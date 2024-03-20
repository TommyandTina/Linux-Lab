#include <stdio.h>
#include <stdlib.h>

int main() {
    FILE *file;
    unsigned char *data;
    int width = 3856; // Ð? r?ng c?a hình ?nh
    int height = 1964; // Ð? cao c?a hình ?nh
    int num_pixels = width * height * 3; // S? lu?ng pixel (YUV444 có 3 thành ph?n màu), nv16 co 2 thanh phan mau

    // M? t?p hình ?nh YUV444 d? d?c
    file = fopen("imageprocessing_requirement1_yuv444p.yuv", "rb");
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
//    for (int i = 0; i < num_pixels; i++) {
//    	static int each_line = 0;
//		static int six_line = 0;
//    	if(i<(num_pixels/3)){
//    		printf("%3d ", data[i]);
//    		each_line++;
//		} else {
//			if(i%2==0){
//				printf("%3d ", data[i]);
//				each_line++;
//			}
//		}
//        	
//        if ((each_line) % 6 == 0) 
//		{
//            printf("\n");  
//            six_line ++;
//				if ((six_line) % 6 == 0) 
//				{
//            		printf("\n");  
//            		six_line = 0;
//        		}	            
//        }
//    }
    printf("\n\n");
    
    // M? t?p d?u ra d? ghi
    FILE *output_file;
    unsigned char *data_out = (unsigned char *)malloc(num_pixels*2/3);//only need 2/3 compare to yuv444
    output_file = fopen("imageprocessing_requirement1_nv16.yuv", "wb");
    if (output_file == NULL) {
        perror("Failed to open output file");
        fclose(output_file);
        return 1;
    }
    
    //write to new file
        for (int i = 0; i < num_pixels; i++) {
        static int data_out_index = 0;
    	if(i<(num_pixels/3)){
    		data_out[data_out_index]=data[i];
    		data_out_index++;
		} else {
			if(i%2==0){
	    		data_out[data_out_index]=data[i];
	    		data_out_index++;
			}
		}
	}
	
	// Ghi n?a d?u c?a d? li?u vào t?p m?i
    fwrite(data_out, sizeof(unsigned char), num_pixels*2/3, output_file);
    fclose(output_file);
    // Gi?i phóng b? nh?
    free(data);
    free(data_out);

    return 0;
}

