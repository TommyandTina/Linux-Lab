#ifndef _MODULE_UTIL_H
#define _MODULE_UTIL_H
#include "base.h"

#define UT_DMA_API      (10)
#define UT_is_DMA_Check      (10)
typedef e_validation_t (*p_DMA_API)(uint16_t x, uint16_t y, const st_DMA_config_t* p_dma_config);
typedef struct{
    e_validation_t ReturnValue[UT_DMA_API];
    uint32_t ut_index;
}s_DMA_API;

extern s_DMA_API g_DMA_API;
extern e_validation_t ut_stub_DMA_API(uint16_t x, uint16_t y, const st_DMA_config_t* p_dma_config);
extern p_DMA_API g_hook_DMA_API;
e_validation_t DMA_API_stub(uint16_t x, uint16_t y, const st_DMA_config_t* p_dma_config);

extern st_config_t g_uts_p_config;

//is_DMA_Check added
typedef e_validation_t (*p_is_DMA_Check)(void);
typedef struct{
    e_validation_t ReturnValue[UT_is_DMA_Check];
    uint32_t ut_index;
}s_is_DMA_Check;
extern p_is_DMA_Check g_hook_is_DMA_Check;
extern e_validation_t ut_stub_is_DMA_Check(void);
extern s_is_DMA_Check g_is_DMA_Check;
#endif /* _MODULE_UTIL_H */