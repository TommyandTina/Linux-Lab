#include "include/DMA.h"
#include "coverage_checker.h"

extern bool DMA_API_C0C1_line_activate_list[100];
extern bool data_format_convert_C0C1_line_activate_list[100];
extern uint8_t DMA_API_C0C1_list[100];
extern uint8_t data_format_convert_C0C1_list[100];

extern bool DMA_API_C2_subexpression_activate_list[100];
extern bool data_format_convert_C2_subexpression_activate_list[100];
extern uint8_t DMA_API_C2_list_true[100];
extern uint8_t data_format_convert_C2_list_true[100];
extern uint8_t DMA_API_C2_list_false[100];
extern uint8_t data_format_convert_C2_list_false[100];

e_validation_t DMA_API(uint16_t x, uint16_t y, const st_DMA_config_t* p_dma_config)
{
    e_validation_t result = E_SUCCESS; C0C1_checker(DMA_API_C0C1_line_activate_list[0], DMA_API_C0C1_list[0]);
    C2_checker(DMA_API_C2_subexpression_activate_list[0], p_dma_config == NULL, DMA_API_C2_list_true[0], DMA_API_C2_list_false[0]);
    if (p_dma_config == NULL)
    {   C0C1_checker(DMA_API_C0C1_line_activate_list[1], DMA_API_C0C1_list[1]);
        result = E_VALIDATION_FAILURE; C0C1_checker(DMA_API_C0C1_line_activate_list[2], DMA_API_C0C1_list[2]);
    }
    C2_checker(DMA_API_C2_subexpression_activate_list[1], E_SUCCESS == result, DMA_API_C2_list_true[1], DMA_API_C2_list_false[1]);
    if (E_SUCCESS == result)
    {   C0C1_checker(DMA_API_C0C1_line_activate_list[3], DMA_API_C0C1_list[3]);
        C2_checker(DMA_API_C2_subexpression_activate_list[2], p_dma_config->enable, DMA_API_C2_list_true[2], DMA_API_C2_list_false[2]);
        if(p_dma_config->enable)
	    {   C0C1_checker(DMA_API_C0C1_line_activate_list[4], DMA_API_C0C1_list[4]);
            uint16_t x1_max = p_dma_config->offset_x + p_dma_config->width - 1; C0C1_checker(DMA_API_C0C1_line_activate_list[5], DMA_API_C0C1_list[5]);
            uint16_t y1_max = p_dma_config->offset_y + p_dma_config->height - 1; C0C1_checker(DMA_API_C0C1_line_activate_list[6], DMA_API_C0C1_list[6]);
            C2_checker(DMA_API_C2_subexpression_activate_list[3], x >= p_dma_config->offset_x, DMA_API_C2_list_true[3], DMA_API_C2_list_false[3]);
            C2_checker(DMA_API_C2_subexpression_activate_list[4], y >= p_dma_config->offset_y, DMA_API_C2_list_true[4], DMA_API_C2_list_false[4]);
            C2_checker(DMA_API_C2_subexpression_activate_list[5], x < x1_max, DMA_API_C2_list_true[5], DMA_API_C2_list_false[5]);
            C2_checker(DMA_API_C2_subexpression_activate_list[6], y < y1_max, DMA_API_C2_list_true[6], DMA_API_C2_list_false[6]);
            C2_checker(DMA_API_C2_subexpression_activate_list[7], p_dma_config->exclude == false, DMA_API_C2_list_true[7], DMA_API_C2_list_false[7]);
            if(x >= p_dma_config->offset_x && y >= p_dma_config->offset_y && x < x1_max && y < y1_max)
            {   C0C1_checker(DMA_API_C0C1_line_activate_list[7], DMA_API_C0C1_list[7]);
                C2_checker(DMA_API_C2_subexpression_activate_list[8], p_dma_config->exclude == true, DMA_API_C2_list_true[8], DMA_API_C2_list_false[8]);
                if (p_dma_config->exclude == true)
                {   C0C1_checker(DMA_API_C0C1_line_activate_list[8], DMA_API_C0C1_list[8]);
                    result = E_FAILURE; C0C1_checker(DMA_API_C0C1_line_activate_list[9], DMA_API_C0C1_list[9]);
                }
            }
            else if (p_dma_config->exclude == false)
            {   C0C1_checker(DMA_API_C0C1_line_activate_list[10], DMA_API_C0C1_list[10]);
                result = E_FAILURE; C0C1_checker(DMA_API_C0C1_line_activate_list[11], DMA_API_C0C1_list[11]);
            }
            else
            {
                /*Nothing*/ C0C1_checker(DMA_API_C0C1_line_activate_list[12], DMA_API_C0C1_list[12]);
            }
	    }
    }
    C0C1_checker(DMA_API_C0C1_line_activate_list[13], DMA_API_C0C1_list[13]);
	return result;
}
 
double data_format_convert(uint8_t flow_encode, uint16_t component)
{
    double result = 0; C0C1_checker(data_format_convert_C0C1_line_activate_list[0], data_format_convert_C0C1_list[0]);
    C2_checker(data_format_convert_C2_subexpression_activate_list[0], flow_encode > 4, data_format_convert_C2_list_true[0], data_format_convert_C2_list_false[0]);
    if (flow_encode > 4)
    {   C0C1_checker(data_format_convert_C0C1_line_activate_list[1], data_format_convert_C0C1_list[1]);
        C0C1_checker(data_format_convert_C0C1_line_activate_list[2], data_format_convert_C0C1_list[2]);
        return -1;
    }
    C2_checker(data_format_convert_C2_subexpression_activate_list[1], component > 0x3FFu, data_format_convert_C2_list_true[1], data_format_convert_C2_list_false[1]);
    if (component > 0x3FFu)
    {   C0C1_checker(data_format_convert_C0C1_line_activate_list[3], data_format_convert_C0C1_list[3]);
        component -= 0x500u; C0C1_checker(data_format_convert_C0C1_line_activate_list[4], data_format_convert_C0C1_list[4]);
        switch (flow_encode)
        {
        case 0:
            C0C1_checker(data_format_convert_C0C1_line_activate_list[5], data_format_convert_C0C1_list[5]);
            result = 10.25; C0C1_checker(data_format_convert_C0C1_line_activate_list[6], data_format_convert_C0C1_list[6]);
            C0C1_checker(data_format_convert_C0C1_line_activate_list[7], data_format_convert_C0C1_list[7]);
            break;
        case 1:
            C0C1_checker(data_format_convert_C0C1_line_activate_list[8], data_format_convert_C0C1_list[8]);
            result = 9.75; C0C1_checker(data_format_convert_C0C1_line_activate_list[9], data_format_convert_C0C1_list[9]);
            C0C1_checker(data_format_convert_C0C1_line_activate_list[10], data_format_convert_C0C1_list[10]);
            break;
        case 2:
            C0C1_checker(data_format_convert_C0C1_line_activate_list[11], data_format_convert_C0C1_list[11]);
            result = 8.5; C0C1_checker(data_format_convert_C0C1_line_activate_list[12], data_format_convert_C0C1_list[12]);
            C0C1_checker(data_format_convert_C0C1_line_activate_list[13], data_format_convert_C0C1_list[13]);
            break;
        case 3:
            C0C1_checker(data_format_convert_C0C1_line_activate_list[14], data_format_convert_C0C1_list[14]);
            result = 7.75; C0C1_checker(data_format_convert_C0C1_line_activate_list[15], data_format_convert_C0C1_list[15]);
            C0C1_checker(data_format_convert_C0C1_line_activate_list[16], data_format_convert_C0C1_list[16]);
            break;
        default:
            C0C1_checker(data_format_convert_C0C1_line_activate_list[17], data_format_convert_C0C1_list[17]);
            C0C1_checker(data_format_convert_C0C1_line_activate_list[18], data_format_convert_C0C1_list[18]);
            break;
        }
        C0C1_checker(data_format_convert_C0C1_line_activate_list[19], data_format_convert_C0C1_list[19]); // For switch statement
    }
    switch (flow_encode)
    {
        case 0:
            C0C1_checker(data_format_convert_C0C1_line_activate_list[20], data_format_convert_C0C1_list[20]);
            result += component / 20; C0C1_checker(data_format_convert_C0C1_line_activate_list[21], data_format_convert_C0C1_list[21]);
            C0C1_checker(data_format_convert_C0C1_line_activate_list[22], data_format_convert_C0C1_list[22]);
            break;
        case 1:
            C0C1_checker(data_format_convert_C0C1_line_activate_list[23], data_format_convert_C0C1_list[23]);
            result += component / 15; C0C1_checker(data_format_convert_C0C1_line_activate_list[24], data_format_convert_C0C1_list[24]);
            C0C1_checker(data_format_convert_C0C1_line_activate_list[25], data_format_convert_C0C1_list[25]);
            break;
        case 2:
            C0C1_checker(data_format_convert_C0C1_line_activate_list[26], data_format_convert_C0C1_list[26]);
            result += component / 10; C0C1_checker(data_format_convert_C0C1_line_activate_list[27], data_format_convert_C0C1_list[27]);
            C0C1_checker(data_format_convert_C0C1_line_activate_list[28], data_format_convert_C0C1_list[28]);
            break; 
        case 3:
            C0C1_checker(data_format_convert_C0C1_line_activate_list[29], data_format_convert_C0C1_list[29]);
            result += component / 5; C0C1_checker(data_format_convert_C0C1_line_activate_list[30], data_format_convert_C0C1_list[30]);
            C0C1_checker(data_format_convert_C0C1_line_activate_list[31], data_format_convert_C0C1_list[31]);
            break; 
        default:
            C0C1_checker(data_format_convert_C0C1_line_activate_list[32], data_format_convert_C0C1_list[32]);
            C0C1_checker(data_format_convert_C0C1_line_activate_list[33], data_format_convert_C0C1_list[33]);
            break;
    }
    C0C1_checker(data_format_convert_C0C1_line_activate_list[34], data_format_convert_C0C1_list[34]); // For switch statement
    C0C1_checker(data_format_convert_C0C1_line_activate_list[35], data_format_convert_C0C1_list[35]);
    return result;
}

bool is_DMA_Check(void){
    return false;
}