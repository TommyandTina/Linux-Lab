#ifndef CHECK_IMAGE_AND_SQUARE_PCL_H
#define CHECK_IMAGE_AND_SQUARE_PCL_H

#include "check_image_and_square.h"

static struct TEST_check_image_and_square_Pattern check_image_and_square_PCL[] =
{
    /* "Test Case ID", { {_p_image,_p_square,{width_of_image, height_of_image,crop_size},{square_width, square_height, square_shift}},{Returnvalue,_p_image,_p_square, {width_of_image, height_of_image,crop_size},{square_width, square_height, square_shift} },{validator,validator,validator,validator,validator,validator,validator,validator} } */
    /* check_image_and_square_0001 */ { { TEST_ADDR_NULL  , TEST_ADDR_NULL , {0,0,0},{0,0,0}},{E_FAILURE,TEST_ADDR_NULL,TEST_ADDR_NULL,{0,0,0},{0,0,0}},{FALSE,FALSE,FALSE}},
    /* check_image_and_square_0002 */ { { TEST_ADDR_NOT_NULL, TEST_ADDR_NULL, {51,41,0},{10,10,1}},{E_FAILURE,TEST_ADDR_NOT_NULL,TEST_ADDR_NULL,{51,41,0},{10,10,1}},{FALSE,FALSE,FALSE}},
    /* check_image_and_square_0003 */ { { TEST_ADDR_NULL, TEST_ADDR_NOT_NULL, {51,41,0},{10,10,1}},{E_FAILURE,TEST_ADDR_NULL,TEST_ADDR_NOT_NULL,{51,41,0},{10,10,1}},{FALSE,FALSE,FALSE}},
    /* check_image_and_square_0004 */ { { TEST_ADDR_NOT_NULL, TEST_ADDR_NOT_NULL, {51,41,0},{10,8,10}},{E_SUCCESS,TEST_ADDR_NOT_NULL,TEST_ADDR_NOT_NULL,{100,80,0},{10,10,1}},{TRUE,TRUE,TRUE}},
    /* check_image_and_square_0005 */ { { TEST_ADDR_NOT_NULL, TEST_ADDR_NOT_NULL, {49,39,0},{10,10,1}},{E_SUCCESS,TEST_ADDR_NOT_NULL,TEST_ADDR_NOT_NULL,{10,10,0},{10,10,1}},{TRUE,TRUE,TRUE}},
    /* check_image_and_square_0006 */ { { TEST_ADDR_NOT_NULL, TEST_ADDR_NOT_NULL, {101,81,0},{10,10,1}},{E_SUCCESS,TEST_ADDR_NOT_NULL,TEST_ADDR_NOT_NULL,{10,10,0},{10,10,1}},{TRUE,TRUE,TRUE}},
};


#endif