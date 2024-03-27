#ifndef PRE_CHECK_CONFIG_H_
#define PRE_CHECK_CONFIG_H_

struct DMA_API_info {
	e_validation_t ReturnValue;
	bool is_stub;
};

struct pre_check_config_input {
	uint32_t _p_config;
	struct DMA_API_info DMA_API;
	st_config_t image_info; //add info of image, personally added
};

struct pre_check_config_expect {
	e_validation_t ReturnValue;
};

struct pre_check_config_params {
	st_config_t *p_config;
};

struct TEST_pre_check_config_Pattern {
	struct pre_check_config_input input;
	struct pre_check_config_expect expected;
};

/*
struct TEST_pre_check_config_Pattern {
	struct pre_check_config_input 
	{
		uint32_t _p_config;
		struct DMA_API_info 
		{
			e_validation_t ReturnValue;
			bool is_stub;
		} DMA_API;
		typedef struct 
		{
			typedef struct
			{
				uint32_t width_of_image;
				uint32_t height_of_image;
				uint32_t crop_size;
			}st_image_size_t image_config;
			typedef struct
			{
				uint8_t square_width;
				uint8_t square_height;
				uint8_t square_shift;
			}st_square_t; square_config;
			typedef struct
			{
				uint32_t offset_x;
				uint32_t offset_y;
				uint32_t width;
				uint32_t height;
				bool enable;
				bool exclude;
			} st_DMA_config_t; dma_config;  
		}st_config_t image_info;
	} input;
	struct pre_check_config_expect{
		e_validation_t ReturnValue;
	} expected;
};
*/

#endif /* PRE_CHECK_CONFIG_H_ */
