#include "base.h"
#include "util.h"
#include "patterns/check_noise_PCL.h"

static bool TEST_Validate_check_noise(struct check_noise_expect *outputs, struct check_noise_expect *expected, bool validator[])
{
	bool b = true;
	b &= TEST_ValidateOutput(&outputs->ReturnValue, &expected->ReturnValue, sizeof(outputs->ReturnValue), "ReturnValue", TEST_VALIDATOR_I32VALUE);

	return b;
}

bool TEST_check_noise(const char *category, int32_t no)
{
	bool b = true;
	struct TestParams *params = TEST_CreateParam("check_noise", category, no);
	struct TEST_check_noise_Pattern *pattern = &check_noise_PCL[no - 1];
	struct check_noise_input	*inputs = &pattern->input;
	struct check_noise_params	func_params = {0};
	struct check_noise_expect	outputs = {0};
	bool is_stub = !inputs->is_DMA_Check.is_stub;

	ut_init_config(is_stub);

	memcpy(&func_params.noise.noise_1, &inputs->noise.noise_1,sizeof(inputs->noise.noise_1));
    memcpy(&func_params.noise.noise_2, &inputs->noise.noise_2,sizeof(inputs->noise.noise_2));
    memcpy(&func_params.noise.noise_3, &inputs->noise.noise_3,sizeof(inputs->noise.noise_3));
    memcpy(&func_params.noise.noise_4, &inputs->noise.noise_4,sizeof(inputs->noise.noise_4));

    
    if (inputs->is_DMA_Check.is_stub)
	{
		memcpy(&g_is_DMA_Check.ReturnValue, &inputs->is_DMA_Check.ReturnValue, sizeof(inputs->is_DMA_Check.ReturnValue));
		g_hook_is_DMA_Check = ut_stub_is_DMA_Check;
	}

	outputs.ReturnValue = check_noise(func_params.noise);

	b &= TEST_Validate_check_noise(&outputs.ReturnValue, &pattern->expected.ReturnValue, NULL);

	TEST_ValidateResult(b, params);

	ut_deinit_config();

	TEST_DestroyParam(params);

	return b;
}
