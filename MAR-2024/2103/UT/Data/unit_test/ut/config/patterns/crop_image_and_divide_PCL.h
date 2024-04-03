#ifndef CROP_IMAGE_AND_DIVIDE_H
#define CROP_IMAGE_AND_DIVIDE_H

#include "crop_image_and_divide.h"

static struct TEST_crop_image_and_divide_Pattern crop_image_and_divide_PCL[] =
{
    /* "Test Case ID        ", {{*p_image, {width_of_image, height_of_image, crop_size}, divisor},{ReturnValue, *p_image, {width_of_image, height_of_image, crop_size}},{validator,validator,validator}}     */
    /* crop_image_and_divide_0001 */ {{TEST_ADDR_NULL, {0, 0, 0}, 0},{E_FAILURE, TEST_ADDR_NOT_NULL, {0, 0, 0}},{}},
    /* crop_image_and_divide_0002 */ {{TEST_ADDR_NOT_NULL, {1, 1, 0}, 0},{E_FAILURE, TEST_ADDR_NOT_NULL, {1, 1, 0}},{}},
    /* crop_image_and_divide_0003 */ {{TEST_ADDR_NOT_NULL, {501, 501, 0}, 0},{E_FAILURE, TEST_ADDR_NOT_NULL, {501, 501, 0}},{}},
    /* crop_image_and_divide_0004 */ {{TEST_ADDR_NOT_NULL, {501, 502, 0}, 999},{E_SUCCESS, TEST_ADDR_NOT_NULL, {502, 502, 0}},{}},
    /* crop_image_and_divide_0005 */ {{TEST_ADDR_NOT_NULL, {501, 505, 0}, 101},{E_SUCCESS, TEST_ADDR_NOT_NULL, {505, 505, 5}},{}},
    /* crop_image_and_divide_0006 */ {{TEST_ADDR_NOT_NULL, {501, 666, 0}, 60},{E_SUCCESS, TEST_ADDR_NOT_NULL, {666, 666, 11}},{}},
    /* crop_image_and_divide_0007 */ {{TEST_ADDR_NOT_NULL, {501, 666, 0}, 120},{E_SUCCESS, TEST_ADDR_NOT_NULL, {666, 666, 5}},{}},
    /* crop_image_and_divide_0008 */ {{TEST_ADDR_NOT_NULL, {501, 666, 0}, 180},{E_SUCCESS, TEST_ADDR_NOT_NULL, {666, 666, 3}},{}},
    /* crop_image_and_divide_0009 */ {{TEST_ADDR_NOT_NULL, {1, 1, 0}, 0},{E_FAILURE, TEST_ADDR_NOT_NULL, {1, 501, 0}},{}}, //2, 3, 9 is MCDC for (p_image->width_of_image <= 500 || p_image->height_of_image <= 500)
};


#endif