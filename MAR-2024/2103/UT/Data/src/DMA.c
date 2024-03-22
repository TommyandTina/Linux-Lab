#include "include/DMA.h"
 
 
e_validation_t DMA_API(uint16_t x, uint16_t y, const st_DMA_config_t* p_dma_config)
{
    e_validation_t result = E_SUCCESS;
 
    if (p_dma_config == NULL)
    {
        result = E_VALIDATION_FAILURE;
    }
    if (E_SUCCESS == result)
    {
        if(p_dma_config->enable)
	    {
            uint16_t x1_max = p_dma_config->offset_x + p_dma_config->width - 1;
            uint16_t y1_max = p_dma_config->offset_y + p_dma_config->height - 1;
            if(x >= p_dma_config->offset_x && y >= p_dma_config->offset_y && x < x1_max && y < y1_max)
            {
                if (p_dma_config->exclude == true)
                {
                    result = E_FAILURE;
                }
            }
            else if (p_dma_config->exclude == false)
            {
                result = E_FAILURE;
            }
            else
            {
                /*Nothing*/
            }
	    }
    }
 
	return result;
}
 
double data_format_convert(uint8_t flow_encode, uint16_t component)
{
    double result = 0;
 
    if (flow_encode > 4)
    {
        return -1;
    }
 
    if (component > 0x3FFu)
    {
        component -= 0x500u;
        switch (flow_encode)
        {
        case 0:
            result = 10.25;
            break;
        case 1:
            result = 9.75;
            break;
        case 2:
            result = 8.5;
            break;
        case 3:
            result = 7.75;
            break;
        default:
            break;
        }
    }
 
    switch (flow_encode)
    {
        case 0:
            result += component / 20;
            break;
 
        case 1:
            result += component / 15;
            break;
 
        case 2:
            result += component / 10;
            break;
 
        case 3:
            result += component / 5;
            break;
        default:
            break;
    }
 
    return result;
}

bool is_DMA_Check(void){
    return false;
}