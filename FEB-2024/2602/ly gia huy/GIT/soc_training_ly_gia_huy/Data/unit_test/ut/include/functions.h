#ifndef _FUNCTIONS_H_
#define _FUNCTIONS_H_

#include <stdbool.h>
#include <stdint.h>

#ifdef __cplusplus
extern "C" {
#endif /* __cplusplus */

bool TEST_DMA_API(const char *category, int32_t no);
bool TEST_data_format_convert(const char *category, int32_t no);
bool TEST_data_pre_check_config(const char *category, int32_t no);

#ifdef __cplusplus
}
#endif
#endif
