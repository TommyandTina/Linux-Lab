#include "base.h"
#include "util.h"
#include "patterns/pre_check_config_PCL.h"

static bool TEST_Validate_pre_check_config(struct pre_check_config_expect *outputs, struct pre_check_config_expect *expected, bool validator[])
{
	bool b = true;
	b &= TEST_ValidateOutput(&outputs->ReturnValue, &expected->ReturnValue, sizeof(outputs->ReturnValue), "ReturnValue", TEST_VALIDATOR_I32VALUE);

	return b;
}

bool TEST_pre_check_config(const char *category, int32_t no)
{
	bool b = true;
	struct TestParams *params = TEST_CreateParam("pre_check_config", category, no);
	struct TEST_pre_check_config_Pattern *pattern = &pre_check_config_PCL[no - 1];
	struct pre_check_config_input	*inputs = &pattern->input;
	struct pre_check_config_params	func_params = {0};
	struct pre_check_config_expect	outputs = {0};
	bool is_stub = !inputs->DMA_API.is_stub;

	ut_init_config(is_stub);

	if (inputs->_p_config == TEST_ADDR_NULL)
	{
		func_params.p_config = NULL;
	}
	else
	{
		func_params.p_config = &g_uts_p_config;
		func_params.p_config->image_config = inputs->image_info.image_config;//personally added
		func_params.p_config->square_config = inputs->image_info.square_config;//personally added
	}
	if (inputs->DMA_API.is_stub)
	{
		memcpy(&g_DMA_API.ReturnValue, &inputs->DMA_API.ReturnValue, sizeof(inputs->DMA_API.ReturnValue));
		g_hook_DMA_API = ut_stub_DMA_API;
	}

	outputs.ReturnValue = pre_check_config(func_params.p_config);

	b &= TEST_Validate_pre_check_config(&outputs, &pattern->expected, NULL);

	TEST_ValidateResult(b, params);

	ut_deinit_config();

	TEST_DestroyParam(params);

	return b;
}
