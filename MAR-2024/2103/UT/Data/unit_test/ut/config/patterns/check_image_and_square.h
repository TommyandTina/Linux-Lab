#ifndef CHECK_IMAGE_AND_SQUARE_H_
#define CHECK_IMAGE_AND_SQUARE_H_

struct check_image_and_square_input {
	uint32_t _p_image;
    uint32_t _p_square;
    st_image_size_t p_image;
	st_square_t p_square;
};

struct check_image_and_square_expect {
	e_validation_t ReturnValue;
	uint32_t _p_image;
	uint32_t _p_square;
    st_image_size_t p_image;
	st_square_t p_square;
};

struct check_image_and_square_params {
	st_image_size_t *p_image;
	st_square_t *p_square;
};

struct TEST_check_image_and_square_Pattern {
	struct check_image_and_square_input input;
	struct check_image_and_square_expect expected;
	bool validator[3];
};

#endif /* CHECK_IMAGE_AND_SQUARE_H_ */