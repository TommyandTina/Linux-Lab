#ifndef CROP_IMAGE_AND_DIVIDE_H_
#define CROP_IMAGE_AND_DIVIDE_H_
#include "DMA.h"

struct crop_image_and_divide_input {
    uint32_t _p_image; 
    st_image_size_t p_image;
    uint32_t divisor;
};

struct crop_image_and_divide_expect {
	e_validation_t ReturnValue;
    uint32_t _p_image;
    st_image_size_t p_image; 
};

struct crop_image_and_divide_params {
    st_image_size_t* p_image;
    uint32_t divisor;
};

struct TEST_crop_image_and_divide_Pattern {
	struct crop_image_and_divide_input input;
	struct crop_image_and_divide_expect expected;
    bool validator[3];
};

#endif

/*
typedef struct
{
    uint32_t width_of_image;
    uint32_t height_of_image;
    uint32_t crop_size;
}st_image_size_t;
*/