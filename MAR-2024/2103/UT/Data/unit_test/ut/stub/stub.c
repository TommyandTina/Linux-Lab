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
        // ret_func = DMA_API(x, y, p_dma_config);
        ret_func = g_hook_DMA_API(x, y, p_dma_config);
        //g_hook_DMA_API = ut_stub_DMA_API; we use g_hook_DMA_API as a middleman here because we still want to declare ut_stub_DMA_API but can controll the use of DMA_API_stub. What happens if we want to skip the stub or change to another stub without changing the source code in here ?
    }
    else
    {
        ret_func = DMA_API(x, y, p_dma_config);
    }
    return ret_func;
}

//is_DMA_Check added
e_validation_t ut_stub_is_DMA_Check(void)
{
    s_is_DMA_Check *IO = &g_is_DMA_Check;
    e_validation_t ReturnValue;
    ReturnValue = IO->ReturnValue[IO->ut_index];
    // IO->ut_index++;we call this function multiple time at C2_checker, so mention this to update index, we don’t want to update index when C2_checker use this function. Luckily we only use this function 1 time inside check_noise
    printf("%d is return value in (stub.c) We finish using stub\n------\n",ReturnValue);
    return ReturnValue;
}

e_validation_t is_DMA_Check_stub(void)
{
    e_validation_t ret_func;
    if (NULL != g_hook_is_DMA_Check)
    {
        printf("\nWe reach is_DMA_Check_stub, not ut_stub_is_DMA_Check\n");
        ret_func = g_hook_is_DMA_Check();
    }
    else
    {
        ret_func = is_DMA_Check();
    }
    return ret_func;
}