#ifndef CHECK_NOISE_PCL_H
#define CHECK_NOISE_PCL_H
#include "check_noise.h"

static struct TEST_check_noise_Pattern check_noise_PCL[] =
{
    /* "Test Case ID        ",   {{{noise1,noise2,noise3,noise4},{ReturnValue,is_stub}},{ReturnValueExpected} }  */
    /* check_noise_0001 */ {{{0,0,0,0},{FALSE,TRUE}},{E_FAILURE} }, // Test when is_DMA_Check() returns FALSE
    /* check_noise_0002 */ {{{11,12,12,9},{TRUE,TRUE}},{E_SUCCESS} },
    /* check_noise_0003 */ {{{11,12,13,9},{TRUE,TRUE}},{E_FAILURE} }, 
    /* check_noise_0004 */ {{{11,12,12,10},{TRUE,TRUE}},{E_FAILURE} }, 
    /* check_noise_0005 */ {{{11,11,13,9},{TRUE,TRUE}},{E_SUCCESS} }, 
    /* check_noise_0006 */ {{{10,12,13,9},{TRUE,TRUE}},{E_SUCCESS} }, 
};

#endif
