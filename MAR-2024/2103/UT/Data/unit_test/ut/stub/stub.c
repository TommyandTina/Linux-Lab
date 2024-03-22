#include "stub.h"

e_validation_t ut_stub_DMA_API(uint16_t x, uint16_t y, const st_DMA_config_t* p_dma_config)
{
    s_DMA_API *IO = &g_DMA_API;
    e_validation_t ReturnValue;
    ReturnValue = IO->ReturnValue[IO->ut_index];
    IO->ut_index++;
    return ReturnValue;
}

e_validation_t DMA_API_stub(uint16_t x, uint16_t y, const st_DMA_config_t* p_dma_config)
{
    e_validation_t ret_func;
    if (NULL != g_hook_DMA_API)
    {
        ret_func = g_hook_DMA_API(x, y, p_dma_config);
    }
    else
    {
        ret_func = DMA_API(x, y, p_dma_config);
    }
    return ret_func;
}