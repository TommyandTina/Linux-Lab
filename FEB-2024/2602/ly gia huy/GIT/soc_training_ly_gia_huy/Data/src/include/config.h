#ifndef CONFIG_H
#define CONFIG_H
#include "DMA.h"
 
e_validation_t pre_check_config(st_config_t* p_config);
e_validation_t check_image_and_square(st_image_size_t* p_image, st_square_t* p_square);
/*********** These functions are for MCDC practices ***********/
e_validation_t check_noise(st_noise_t noise);
e_validation_t crop_image_and_divide(st_image_size_t* p_image, uint8_t divisor);
/* ************************************************************/
 
#endif