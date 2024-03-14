#ifndef DMA_H
#define DMA_H
 
#include <stdio.h>
#include <stdint.h>
#include <stdbool.h>
#include <string.h>
 
typedef struct
{
    uint32_t width_of_image;
    uint32_t height_of_image;
    uint32_t crop_size;
}st_image_size_t;
 
typedef struct
{
    uint8_t square_width;
    uint8_t square_height;
    uint8_t square_shift;
}st_square_t;
 
typedef struct
{
    uint32_t offset_x;
    uint32_t offset_y;
    uint32_t width;
    uint32_t height;
    bool enable;
    bool exclude;
} st_DMA_config_t;
 
typedef enum
{
    E_VALIDATION_FAILURE = -2,
    E_FAILURE = -1,
    E_SUCCESS = 0,
}e_validation_t;
 
typedef struct 
{
  st_image_size_t image_config;
  st_square_t square_config;
  st_DMA_config_t dma_config;  
}st_config_t;

typedef struct 
{
  uint8_t noise_1;
  uint8_t noise_2;
  uint8_t noise_3;
  uint8_t noise_4;  
}st_noise_t;
 
 
double data_format_convert(uint8_t flow_encode, uint16_t component);
e_validation_t DMA_API(uint16_t x, uint16_t y, const st_DMA_config_t* p_dma_config);
bool is_DMA_Check(void);
 
#endif // DMA_H