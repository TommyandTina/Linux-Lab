#include "include/DMA.h"
#include "coverage_checker.h"

extern bool pre_check_config_C0C1_line_activate_list[100];
extern bool check_image_and_square_C0C1_line_activate_list[100];
extern bool check_noise_C0C1_line_activate_list[100];
extern bool crop_image_and_divide_C0C1_line_activate_list[100];

extern uint8_t pre_check_config_C0C1_list[100];
extern uint8_t check_image_and_square_C0C1_list[100];
extern uint8_t check_noise_C0C1_list[100];
extern uint8_t crop_image_and_divide_C0C1_list[100];

extern bool pre_check_config_C2_subexpression_activate_list[100];
extern bool check_image_and_square_C2_subexpression_activate_list[100];
extern bool check_noise_C2_subexpression_activate_list[100];
extern bool crop_image_and_divide_C2_subexpression_activate_list[100];

extern uint8_t pre_check_config_C2_list_true[100];
extern uint8_t check_image_and_square_C2_list_true[100];
extern uint8_t check_noise_C2_list_true[100];
extern uint8_t crop_image_and_divide_C2_list_true[100];

extern uint8_t pre_check_config_C2_list_false[100];
extern uint8_t check_image_and_square_C2_list_false[100];
extern uint8_t check_noise_C2_list_false[100];
extern uint8_t crop_image_and_divide_C2_list_false[100];

e_validation_t pre_check_config(st_config_t* p_config)
{
    e_validation_t result = E_SUCCESS; C0C1_checker(pre_check_config_C0C1_line_activate_list[0], pre_check_config_C0C1_list[0]);
    C2_checker(pre_check_config_C2_subexpression_activate_list[0], p_config == NULL, pre_check_config_C2_list_true[0], pre_check_config_C2_list_false[0]);
    C2_checker(pre_check_config_C2_subexpression_activate_list[1], E_SUCCESS != DMA_API(50u, 50u, &(p_config->dma_config)), pre_check_config_C2_list_true[1], pre_check_config_C2_list_false[1]);
    if ((p_config == NULL) || E_SUCCESS != DMA_API(50u, 50u, &(p_config->dma_config)))
    {   C0C1_checker(pre_check_config_C0C1_line_activate_list[1], pre_check_config_C0C1_list[1]);
        C0C1_checker(pre_check_config_C0C1_line_activate_list[2], pre_check_config_C0C1_list[2]);
        return E_FAILURE;
    }
    st_image_size_t *p_image_size = &(p_config->image_config); C0C1_checker(pre_check_config_C0C1_line_activate_list[3], pre_check_config_C0C1_list[3]);
    C2_checker(pre_check_config_C2_subexpression_activate_list[2], p_image_size->width_of_image == 400, pre_check_config_C2_list_true[2], pre_check_config_C2_list_false[2]);
    C2_checker(pre_check_config_C2_subexpression_activate_list[3], p_image_size->height_of_image == 150, pre_check_config_C2_list_true[3], pre_check_config_C2_list_false[3]);
    if (p_image_size->width_of_image == 400 && p_image_size->height_of_image == 150)
    {   C0C1_checker(pre_check_config_C0C1_line_activate_list[4], pre_check_config_C0C1_list[4]);
        p_image_size->width_of_image = 200; C0C1_checker(pre_check_config_C0C1_line_activate_list[5], pre_check_config_C0C1_list[5]);
        p_image_size->height_of_image = 125; C0C1_checker(pre_check_config_C0C1_line_activate_list[6], pre_check_config_C0C1_list[6]);
    }
    else
    {   C0C1_checker(pre_check_config_C0C1_line_activate_list[7], pre_check_config_C0C1_list[7]);
        st_square_t *p_square = &(p_config->square_config); C0C1_checker(pre_check_config_C0C1_line_activate_list[8], pre_check_config_C0C1_list[8]);
        C2_checker(pre_check_config_C2_subexpression_activate_list[4], p_square->square_width < 4u, pre_check_config_C2_list_true[4], pre_check_config_C2_list_false[4]);
        C2_checker(pre_check_config_C2_subexpression_activate_list[5], p_square->square_width > 200u, pre_check_config_C2_list_true[5], pre_check_config_C2_list_false[5]);
        C2_checker(pre_check_config_C2_subexpression_activate_list[6], p_square->square_height < 2u, pre_check_config_C2_list_true[6], pre_check_config_C2_list_false[6]);
        C2_checker(pre_check_config_C2_subexpression_activate_list[7], p_square->square_height > 200u, pre_check_config_C2_list_true[7], pre_check_config_C2_list_false[7]);
        C2_checker(pre_check_config_C2_subexpression_activate_list[8], p_square->square_shift != 4, pre_check_config_C2_list_true[8], pre_check_config_C2_list_false[8]);
        if ((p_square->square_width < 4u || p_square->square_width > 200u) && (p_square->square_height < 2u || p_square->square_height > 200u) && (p_square->square_shift != 4))
        {   C0C1_checker(pre_check_config_C0C1_line_activate_list[9], pre_check_config_C0C1_list[9]);
            C0C1_checker(pre_check_config_C0C1_line_activate_list[10], pre_check_config_C0C1_list[10]);
            result = E_FAILURE;
        }
    } 
    C0C1_checker(pre_check_config_C0C1_line_activate_list[11], pre_check_config_C0C1_list[11]);
    return result;
}

e_validation_t check_image_and_square(st_image_size_t* p_image, st_square_t* p_square)
{
    e_validation_t result = E_SUCCESS; C0C1_checker(check_image_and_square_C0C1_line_activate_list[0], check_image_and_square_C0C1_list[0]);
    C2_checker(check_image_and_square_C2_subexpression_activate_list[0], p_image == NULL, check_image_and_square_C2_list_true[0], check_image_and_square_C2_list_false[0]);
    C2_checker(check_image_and_square_C2_subexpression_activate_list[1], p_square == NULL, check_image_and_square_C2_list_true[1], check_image_and_square_C2_list_false[1]);
    if (p_image == NULL || p_square == NULL)
    {   C0C1_checker(check_image_and_square_C0C1_line_activate_list[1], check_image_and_square_C0C1_list[1]);
        C0C1_checker(check_image_and_square_C0C1_line_activate_list[2], check_image_and_square_C0C1_list[2]);
        result = E_FAILURE;
    }
    C2_checker(check_image_and_square_C2_subexpression_activate_list[2], result == E_SUCCESS, check_image_and_square_C2_list_true[2], check_image_and_square_C2_list_false[2]);
    if (result == E_SUCCESS)
    {   C0C1_checker(check_image_and_square_C0C1_line_activate_list[3], check_image_and_square_C0C1_list[3]);
        C2_checker(check_image_and_square_C2_subexpression_activate_list[3], p_image->width_of_image > 50, check_image_and_square_C2_list_true[3], check_image_and_square_C2_list_false[3]);
        C2_checker(check_image_and_square_C2_subexpression_activate_list[4], p_image->width_of_image < 100, check_image_and_square_C2_list_true[4], check_image_and_square_C2_list_false[4]);
        if (p_image->width_of_image > 50 && p_image->width_of_image < 100)
        {   C0C1_checker(check_image_and_square_C0C1_line_activate_list[4], check_image_and_square_C0C1_list[4]);
            p_image->width_of_image = p_square->square_width * p_square->square_shift; C0C1_checker(check_image_and_square_C0C1_line_activate_list[5], check_image_and_square_C0C1_list[5]);
        }
        else
        {   C0C1_checker(check_image_and_square_C0C1_line_activate_list[6], check_image_and_square_C0C1_list[6]);
            p_image->width_of_image = p_square->square_width; C0C1_checker(check_image_and_square_C0C1_line_activate_list[7], check_image_and_square_C0C1_list[7]);
        }
        C2_checker(check_image_and_square_C2_subexpression_activate_list[5], p_image->height_of_image > 40, check_image_and_square_C2_list_true[5], check_image_and_square_C2_list_false[5]);
        C2_checker(check_image_and_square_C2_subexpression_activate_list[6], p_image->height_of_image < 80, check_image_and_square_C2_list_true[6], check_image_and_square_C2_list_false[6]);
        if (p_image->height_of_image > 40 && p_image->height_of_image < 80)
        {   C0C1_checker(check_image_and_square_C0C1_line_activate_list[8], check_image_and_square_C0C1_list[8]);
            p_image->height_of_image = p_square->square_height * p_square->square_shift; C0C1_checker(check_image_and_square_C0C1_line_activate_list[9], check_image_and_square_C0C1_list[9]);
        }
        else
        {   C0C1_checker(check_image_and_square_C0C1_line_activate_list[10], check_image_and_square_C0C1_list[10]);
            p_image->height_of_image = p_square->square_height; C0C1_checker(check_image_and_square_C0C1_line_activate_list[11], check_image_and_square_C0C1_list[11]);
        }

    }
    C0C1_checker(check_image_and_square_C0C1_line_activate_list[12], check_image_and_square_C0C1_list[12]);
    return result;
}

/*********** These functions are for MCDC practices ***********/
e_validation_t check_noise(st_noise_t noise) 
{
    C2_checker(check_noise_C2_subexpression_activate_list[0], !is_DMA_Check(), check_noise_C2_list_true[0], check_noise_C2_list_false[0]);
    if (!is_DMA_Check()) {
        C0C1_checker(check_noise_C0C1_line_activate_list[0], check_noise_C0C1_list[0]);
        C0C1_checker(check_noise_C0C1_line_activate_list[1], check_noise_C0C1_list[1]);
        return E_FAILURE;
    } //note that at C2_checker on top call 2 times is_DMA_Check() -> eliminate IO->index++ inside stub function
    C2_checker(check_noise_C2_subexpression_activate_list[1], noise.noise_1 > 10, check_noise_C2_list_true[1], check_noise_C2_list_false[1]);
    C2_checker(check_noise_C2_subexpression_activate_list[2], noise.noise_2 > 11, check_noise_C2_list_true[2], check_noise_C2_list_false[2]);
    C2_checker(check_noise_C2_subexpression_activate_list[3], noise.noise_3 > 12, check_noise_C2_list_true[3], check_noise_C2_list_false[3]);
    C2_checker(check_noise_C2_subexpression_activate_list[4], noise.noise_4 > 9, check_noise_C2_list_true[4], check_noise_C2_list_false[4]);
    if (((noise.noise_1 > 10) && (noise.noise_2 > 11) && (noise.noise_3 > 12)) || (noise.noise_4 > 9)) {
        C0C1_checker(check_noise_C0C1_line_activate_list[2], check_noise_C0C1_list[2]);
        C0C1_checker(check_noise_C0C1_line_activate_list[3], check_noise_C0C1_list[3]);
        return E_FAILURE;
    }
    else {
        C0C1_checker(check_noise_C0C1_line_activate_list[4], check_noise_C0C1_list[4]);
        C0C1_checker(check_noise_C0C1_line_activate_list[5], check_noise_C0C1_list[5]);
        return E_SUCCESS;
    }
}

e_validation_t crop_image_and_divide(st_image_size_t* p_image, uint32_t divisor)
{
    e_validation_t result = E_SUCCESS; C0C1_checker(crop_image_and_divide_C0C1_line_activate_list[0], crop_image_and_divide_C0C1_list[0]);
    C2_checker(crop_image_and_divide_C2_subexpression_activate_list[0], p_image == NULL, crop_image_and_divide_C2_list_true[0], crop_image_and_divide_C2_list_false[0]);
    if (p_image == NULL)
    {   C0C1_checker(crop_image_and_divide_C0C1_line_activate_list[1], crop_image_and_divide_C0C1_list[1]);
        C0C1_checker(crop_image_and_divide_C0C1_line_activate_list[2], crop_image_and_divide_C0C1_list[2]);
        return result = E_FAILURE;
    }
    printf("\n%d is width,%d is height\n",p_image->width_of_image,p_image->height_of_image);
    C2_checker(crop_image_and_divide_C2_subexpression_activate_list[1], p_image->width_of_image <= 500, crop_image_and_divide_C2_list_true[1], crop_image_and_divide_C2_list_false[1]);
    C2_checker(crop_image_and_divide_C2_subexpression_activate_list[2], p_image->height_of_image <= 500, crop_image_and_divide_C2_list_true[2], crop_image_and_divide_C2_list_false[2]);
    if (p_image->width_of_image <= 500 || p_image->height_of_image <= 500) {
        C0C1_checker(crop_image_and_divide_C0C1_line_activate_list[3], crop_image_and_divide_C0C1_list[3]);
        C0C1_checker(crop_image_and_divide_C0C1_line_activate_list[4], crop_image_and_divide_C0C1_list[4]);
        result = E_FAILURE;
    }
    else {
        /* Crop to make squared image */ C0C1_checker(crop_image_and_divide_C0C1_line_activate_list[5], crop_image_and_divide_C0C1_list[5]);
        p_image->width_of_image = p_image->height_of_image; C0C1_checker(crop_image_and_divide_C0C1_line_activate_list[6], crop_image_and_divide_C0C1_list[6]);
    }
    C2_checker(crop_image_and_divide_C2_subexpression_activate_list[3], result == E_SUCCESS, crop_image_and_divide_C2_list_true[3], crop_image_and_divide_C2_list_false[3]);
    if (result == E_SUCCESS)
    {   C0C1_checker(crop_image_and_divide_C0C1_line_activate_list[7], crop_image_and_divide_C0C1_list[7]);
        C2_checker(crop_image_and_divide_C2_subexpression_activate_list[4], p_image->width_of_image % 2, crop_image_and_divide_C2_list_true[4], crop_image_and_divide_C2_list_false[4]);
        C2_checker(crop_image_and_divide_C2_subexpression_activate_list[5], p_image->height_of_image % 2, crop_image_and_divide_C2_list_true[5], crop_image_and_divide_C2_list_false[5]);
        C2_checker(crop_image_and_divide_C2_subexpression_activate_list[6], p_image->width_of_image % 5, crop_image_and_divide_C2_list_true[6], crop_image_and_divide_C2_list_false[6]);
        C2_checker(crop_image_and_divide_C2_subexpression_activate_list[7], p_image->height_of_image % 5, crop_image_and_divide_C2_list_true[7], crop_image_and_divide_C2_list_false[7]);
        C2_checker(crop_image_and_divide_C2_subexpression_activate_list[8], p_image->width_of_image % 6, crop_image_and_divide_C2_list_true[8], crop_image_and_divide_C2_list_false[8]);
        C2_checker(crop_image_and_divide_C2_subexpression_activate_list[9], p_image->height_of_image % 6, crop_image_and_divide_C2_list_true[9], crop_image_and_divide_C2_list_false[9]);
        if ((p_image->width_of_image % 2) != 0 && (p_image->height_of_image % 2) != 0 && \
            (p_image->width_of_image % 5) != 0 && (p_image->height_of_image % 5) != 0 && \
            (p_image->width_of_image % 6) != 0 && (p_image->height_of_image % 6) != 0)
        {
            C0C1_checker(crop_image_and_divide_C0C1_line_activate_list[8], crop_image_and_divide_C0C1_list[8]);
            C0C1_checker(crop_image_and_divide_C0C1_line_activate_list[9], crop_image_and_divide_C0C1_list[9]);
            result = E_FAILURE;
        }
        else {
            C2_checker(crop_image_and_divide_C2_subexpression_activate_list[10], divisor % 60  == 0, crop_image_and_divide_C2_list_true[10], crop_image_and_divide_C2_list_false[10]);
            C2_checker(crop_image_and_divide_C2_subexpression_activate_list[11], divisor % 120 == 0, crop_image_and_divide_C2_list_true[11], crop_image_and_divide_C2_list_false[11]);
            C2_checker(crop_image_and_divide_C2_subexpression_activate_list[12], divisor % 180 == 0, crop_image_and_divide_C2_list_true[12], crop_image_and_divide_C2_list_false[12]);
            C2_checker(crop_image_and_divide_C2_subexpression_activate_list[13], divisor <= p_image->width_of_image, crop_image_and_divide_C2_list_true[13], crop_image_and_divide_C2_list_false[13]);
            if (((divisor % 60  == 0) && (divisor <= p_image->width_of_image)) || \
                ((divisor % 120 == 0) && (divisor <= p_image->width_of_image)) || \
                ((divisor % 180 == 0) && (divisor <= p_image->width_of_image))
            ) {
                C0C1_checker(crop_image_and_divide_C0C1_line_activate_list[10], crop_image_and_divide_C0C1_list[10]);
                p_image->crop_size = p_image->width_of_image/divisor; C0C1_checker(crop_image_and_divide_C0C1_line_activate_list[11], crop_image_and_divide_C0C1_list[11]);
            }
        }
    }
    C0C1_checker(crop_image_and_divide_C0C1_line_activate_list[12], crop_image_and_divide_C0C1_list[12]);
    return result;
}
/* ************************************************************/
