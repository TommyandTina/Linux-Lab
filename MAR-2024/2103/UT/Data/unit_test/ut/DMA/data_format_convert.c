#include "base.h"
#include "util.h"
#include "patterns/data_format_convert_PCL.h"

static bool TEST_Validate_data_format_convert(struct data_format_convert_expect *outputs, struct data_format_convert_expect *expected, bool validator[])
{
	bool b = true;
	b &= TEST_ValidateOutput(&outputs->ReturnValue, &expected->ReturnValue, sizeof(outputs->ReturnValue), "ReturnValue", TEST_VALIDATOR_I32VALUE);

	return b;
}

bool TEST_data_format_convert(const char *category, int32_t no)
{
	bool b = true;
	struct TestParams *params = TEST_CreateParam("data_format_convert", category, no);
	struct TEST_data_format_convert_Pattern *pattern = &data_format_convert_PCL[no - 1];
	struct data_format_convert_input	*inputs = &pattern->input;
	struct data_format_convert_params	func_params = {0};
	struct data_format_convert_expect	outputs = {0};

	ut_init_config(false);

	memcpy(&func_params.flow_encode, &inputs->flow_encode, sizeof(func_params.flow_encode));
	memcpy(&func_params.component, &inputs->component, sizeof(func_params.component));

	outputs.ReturnValue = data_format_convert(func_params.flow_encode, func_params.component);

	b &= TEST_Validate_data_format_convert(&outputs, &pattern->expected, NULL);

	TEST_ValidateResult(b, params);

	ut_deinit_config();

	TEST_DestroyParam(params);

	return b;
}
