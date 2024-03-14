#ifndef PRE_CHECK_CONFIG_H_
#define PRE_CHECK_CONFIG_H_

struct DMA_API_info {
	e_validation_t ReturnValue;
	bool is_stub;
};

struct pre_check_config_input {
	uint32_t _p_config;
	struct DMA_API_info DMA_API;
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

#endif /* PRE_CHECK_CONFIG_H_ */
