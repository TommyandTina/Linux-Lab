#include "include/DMA.h"
 
e_validation_t pre_check_config(st_config_t* p_config)
{
    e_validation_t result = E_SUCCESS;
 
    if ((p_config == NULL) || E_SUCCESS != DMA_API(50u, 50u, &(p_config->dma_config)))
    {
        return E_FAILURE;
    }
 
    st_image_size_t *p_image_size = &(p_config->image_config);
 
    if (p_image_size->width_of_image == 400 && p_image_size->height_of_image == 150)
    {
        p_image_size->width_of_image = 200;
        p_image_size->height_of_image = 125;
    }
    else
    {
        st_square_t *p_square = &(p_config->square_config);
        if ((p_square->square_width < 4u || p_square->square_width > 200u) && (p_square->square_height < 2u || p_square->square_height > 200u) \
&& (p_square->square_shift != 4))
        {
            result = E_FAILURE;
        }
    }
 
    return result;
 
}

e_validation_t check_image_and_square(st_image_size_t* p_image, st_square_t* p_square)
{
    e_validation_t result = E_SUCCESS;

    if (p_image == NULL || p_square == NULL)
    {
        result = E_FAILURE;
    }

    if (result == E_SUCCESS)
    {
        if (p_image->width_of_image > 50 && p_image->width_of_image < 100)
        {
            p_image->width_of_image = p_square->square_width * p_square->square_shift;
        }
        else
        {
            p_image->width_of_image = p_square->square_width;
        }
        
        if (p_image->height_of_image > 40 && p_image->height_of_image < 80)
        {
            p_image->height_of_image = p_square->square_height * p_square->square_shift;
        }
        else
        {
            p_image->height_of_image = p_square->square_height;
        }

    }

    return result;
}

/*********** These functions are for MCDC practices ***********/
e_validation_t check_noise(st_noise_t noise) 
{
    if (!is_DMA_Check()) {
        return E_FAILURE;
    }
    if (((noise.noise_1 > 10) && (noise.noise_2 > 11) && (noise.noise_3 > 12)) || (noise.noise_4 > 9)) {
        return E_FAILURE;
    }
    else {
        return E_SUCCESS;
    }
}

e_validation_t crop_image_and_divide(st_image_size_t* p_image, uint8_t divisor)
{
    e_validation_t result = E_SUCCESS;

    if (p_image == NULL)
    {
        result = E_FAILURE;
    }

    if (p_image->width_of_image <= 500 || p_image->height_of_image <= 500) {
        result = E_FAILURE;
    }
    else {
        /* Crop to make squared image */
        p_image->width_of_image = p_image->height_of_image;
    }

    if (result == E_SUCCESS)
    {
        if ((p_image->width_of_image % 2) != 0 && (p_image->height_of_image % 2) != 0 && \
            (p_image->width_of_image % 5) != 0 && (p_image->height_of_image % 5) != 0 && \
            (p_image->width_of_image % 6) != 0 && (p_image->height_of_image % 6) != 0)
        {
            result = E_FAILURE;
        }
        else {
            if (((divisor % 60  == 0) && (divisor <= p_image->width_of_image)) || \
                ((divisor % 120 == 0) && (divisor <= p_image->width_of_image)) || \
                ((divisor % 180 == 0) && (divisor <= p_image->width_of_image))
            ) {
                p_image->crop_size = p_image->width_of_image/divisor;
            }
        }
    }

    return result;
}
/* ************************************************************/
