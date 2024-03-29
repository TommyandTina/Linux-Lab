#define DMA_API             DMA_API_(__LINE__)
#define DMA_API_(line)      DMA_API__(line)
#define DMA_API__(line)     DMA_API_ut_##line
#define is_DMA_Check         is_DMA_Check_(__LINE__)
#define is_DMA_Check_(line)  is_DMA_Check__(line)
#define is_DMA_Check__(line) is_DMA_Check_ut_##line

#ifndef CHECK_COVERAGE
    /* "7" is the line number where DMA_API is called in function pre_check_config in file config.c
       Update this number if the DMA_API is no longer in line 7 */
    #define DMA_API_ut_7        DMA_API_stub
    #define is_DMA_Check_ut_70    is_DMA_Check_stub
#else
    /* "34" is the line number where DMA_API is called in function pre_check_config in file config.c (source_coverage)
       Update this number if the DMA_API is no longer in line 34 */
    #define DMA_API_ut_34       DMA_API_stub
    #define DMA_API_ut_33       DMA_API_stub
    #define is_DMA_Check_ut_107 is_DMA_Check_stub
    #define is_DMA_Check_ut_108 is_DMA_Check_stub
#endif

#include "config.c"
#undef DMA_API
#undef is_DMA_Check