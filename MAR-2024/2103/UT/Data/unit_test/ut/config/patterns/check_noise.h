#ifndef CHECK_NOISE_H_
#define CHECK_NOISE_H_
#include "DMA.h"

struct is_DMA_Check_info {
	e_validation_t ReturnValue;
	bool is_stub;
};

struct check_noise_input {
    st_noise_t noise;
	struct is_DMA_Check_info is_DMA_Check;
};

struct check_noise_expect {
	e_validation_t ReturnValue;
};

struct check_noise_params {
	st_noise_t noise;
};

struct TEST_check_noise_Pattern {
	struct check_noise_input input;
	struct check_noise_expect expected;
};



#endif /* CHECK_NOISE_H_ */