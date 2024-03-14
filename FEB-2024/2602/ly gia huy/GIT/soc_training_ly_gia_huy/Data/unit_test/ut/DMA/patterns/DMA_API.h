#ifndef DMA_API_H_
#define DMA_API_H_

struct DMA_API_input {
	uint16_t x;
	uint16_t y;
	uint32_t _p_dma_config;
	st_DMA_config_t p_dma_config;
};

struct DMA_API_expect {
	e_validation_t ReturnValue;
	uint32_t _p_dma_config;
	st_DMA_config_t p_dma_config;
};

struct DMA_API_params {
	uint16_t x;
	uint16_t y;
	st_DMA_config_t *p_dma_config;
};

struct TEST_DMA_API_Pattern {
	struct DMA_API_input input;
	struct DMA_API_expect expected;
	bool validator[7];
};

#endif /* DMA_API_H_ */
