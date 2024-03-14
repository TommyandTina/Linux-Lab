#ifndef DATA_FORMAT_CONVERT_H_
#define DATA_FORMAT_CONVERT_H_

struct data_format_convert_input {
	uint8_t flow_encode;
	uint16_t component;
};

struct data_format_convert_expect {
	double ReturnValue;
};

struct data_format_convert_params {
	uint8_t flow_encode;
	uint16_t component;
};

struct TEST_data_format_convert_Pattern {
	struct data_format_convert_input input;
	struct data_format_convert_expect expected;
};

#endif /* DATA_FORMAT_CONVERT_H_ */
