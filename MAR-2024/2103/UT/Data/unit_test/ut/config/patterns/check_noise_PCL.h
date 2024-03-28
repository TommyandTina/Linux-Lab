#ifndef CHECK_NOISE_PCL_H
#define CHECK_NOISE_PCL_H

#include "check_noise.h"

// static struct TEST_check_noise_Pattern check_noise_PCL[] =
// {
// 	/* "Test Case ID        ",   {{{noise1,noise2,noise3,noise4},{ReturnValue,is_stub}},{ReturnValueExpected} }  */
// 	/* check_noise_0001 */ {{{0,0,0,0},{E_FAILURE,TRUE}},{E_FAILURE} },
// };

static struct TEST_check_noise_Pattern check_noise_PCL[] =
{
    /* "Test Case ID        ",   {{{noise1,noise2,noise3,noise4},{ReturnValue,is_stub}},{ReturnValueExpected} }  */
    /* check_noise_0001 */ {{{0,0,0,0},{E_FAILURE,TRUE}},{E_FAILURE} },
    /* check_noise_0002 */ {{{11,12,13,10},{E_SUCCESS,TRUE}},{E_FAILURE} },
    /* check_noise_0003 */ {{{10,11,12,9},{E_SUCCESS,TRUE}},{E_SUCCESS} },
    /* check_noise_0004 */ {{{11,11,12,9},{E_SUCCESS,TRUE}},{E_FAILURE} },
    /* check_noise_0005 */ {{{10,12,12,9},{E_SUCCESS,TRUE}},{E_FAILURE} },
    /* check_noise_0006 */ {{{10,11,13,9},{E_SUCCESS,TRUE}},{E_FAILURE} },
    /* check_noise_0007 */ {{{10,11,12,10},{E_SUCCESS,TRUE}},{E_FAILURE} },
};

#endif

// struct TEST_check_noise_Pattern {
// 	struct check_noise_input input{
//         st_noise_t noise;{
//             1
//             2
//             3
//             4
//         }
// 	    struct is_DMA_Check_info is_DMA_Check{
//             e_validation_t ReturnValue;
// 	        bool is_stub;
//         }
//     }
// 	struct check_noise_expect expected{
//         e_validation_t ReturnValue;
//     }
// };
