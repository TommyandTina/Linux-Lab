#include "logger.h"
#include "stub.h"

p_DMA_API g_hook_DMA_API;
e_validation_t ut_stub_DMA_API(uint16_t x, uint16_t y, const st_DMA_config_t* p_dma_config);
s_DMA_API g_DMA_API;

st_config_t g_uts_p_config;

//is_DMA_Check added
p_is_DMA_Check g_hook_is_DMA_Check;
e_validation_t ut_stub_is_DMA_Check(void);
s_is_DMA_Check g_is_DMA_Check;


/*UT INIT function*/
void ut_init_config(bool b)
{
    memset(&g_DMA_API, 0, sizeof(s_DMA_API));
    memset(&g_is_DMA_Check, 0, sizeof(s_is_DMA_Check));
};


/*UT DEINIT function*/
void ut_deinit_config(void)
{

};