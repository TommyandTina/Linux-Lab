#include "base.h"
#include "util.h"
#include "patterns/DMA_API_PCL.h"

static bool TEST_GetAddr_DMA_API(uint32_t *flag, struct DMA_API_params *func_params)
{
	bool ret = true;

	switch (*flag)
	{
	case TEST_ADDR_NOT_NULL:
		ret = Test_set_validate_pointer_info((uint32_t)TEST_ADDR_NOT_NULL, "not null\0");
		break;
	default:
		break;
	}

	return ret;
}

static bool TEST_Validate_DMA_API(struct DMA_API_expect *outputs, struct DMA_API_expect *expected, bool validator[])
{
	bool b = true;
	uint64_t index = 0;

	b &= TEST_ValidateOutput(&outputs->ReturnValue, &expected->ReturnValue, sizeof(outputs->ReturnValue), "ReturnValue", TEST_VALIDATOR_RETCODE);

	if (TEST_CheckBitValidator(validator, index++))
	{
		b &= TEST_ValidateOutput(&outputs->_p_dma_config, &expected->_p_dma_config, sizeof(outputs->_p_dma_config), "*p_dma_config", TEST_VALIDATOR_ADDR);
	}

	if (TEST_CheckBitValidator(validator, index++))
	{
		b &= TEST_ValidateOutput(&outputs->p_dma_config.offset_x, &expected->p_dma_config.offset_x, sizeof(outputs->p_dma_config.offset_x), "*p_dma_config.offset_x", TEST_VALIDATOR_I32VALUE);
	}

	if (TEST_CheckBitValidator(validator, index++))
	{
		b &= TEST_ValidateOutput(&outputs->p_dma_config.offset_y, &expected->p_dma_config.offset_y, sizeof(outputs->p_dma_config.offset_y), "*p_dma_config.offset_y", TEST_VALIDATOR_I32VALUE);
	}

	if (TEST_CheckBitValidator(validator, index++))
	{
		b &= TEST_ValidateOutput(&outputs->p_dma_config.width, &expected->p_dma_config.width, sizeof(outputs->p_dma_config.width), "*p_dma_config.width", TEST_VALIDATOR_I32VALUE);
	}

	if (TEST_CheckBitValidator(validator, index++))
	{
		b &= TEST_ValidateOutput(&outputs->p_dma_config.height, &expected->p_dma_config.height, sizeof(outputs->p_dma_config.height), "*p_dma_config.height", TEST_VALIDATOR_I32VALUE);
	}

	if (TEST_CheckBitValidator(validator, index++))
	{
		b &= TEST_ValidateOutput(&outputs->p_dma_config.enable, &expected->p_dma_config.enable, sizeof(outputs->p_dma_config.enable), "*p_dma_config.enable", TEST_VALIDATOR_I32VALUE);
	}

	if (TEST_CheckBitValidator(validator, index++))
	{
		b &= TEST_ValidateOutput(&outputs->p_dma_config.exclude, &expected->p_dma_config.exclude, sizeof(outputs->p_dma_config.exclude), "*p_dma_config.exclude", TEST_VALIDATOR_I32VALUE);
	}

	return b;
}

bool TEST_DMA_API(const char *category, int32_t no)
{
	bool b = true;
	struct TestParams *params = TEST_CreateParam("DMA_API", category, no);
	struct TEST_DMA_API_Pattern *pattern = &DMA_API_PCL[no - 1];
	struct DMA_API_input	*inputs = &pattern->input;
	struct DMA_API_params	func_params = {0};
	struct DMA_API_expect	outputs = {0};

	ut_init_config(false);

	memcpy(&func_params.x, &inputs->x, sizeof(func_params.x));
	memcpy(&func_params.y, &inputs->y, sizeof(func_params.y));
	if (inputs->_p_dma_config == TEST_ADDR_NULL)
	{
		func_params.p_dma_config = NULL;
	}
	else
	{
		func_params.p_dma_config = &inputs->p_dma_config;
	}

	outputs.ReturnValue = DMA_API(func_params.x, func_params.y, func_params.p_dma_config);

	if (pattern->expected._p_dma_config == TEST_ADDR_NULL || pattern->expected._p_dma_config == TEST_ADDR_NOT_NULL)
	{
		outputs._p_dma_config = (func_params.p_dma_config == NULL) ? TEST_ADDR_NULL : TEST_ADDR_NOT_NULL;
	}
	else
	{
		outputs._p_dma_config = (uint32_t)func_params.p_dma_config;
	}
	if (func_params.p_dma_config != NULL)
	{
		memcpy(&outputs.p_dma_config , func_params.p_dma_config, sizeof(outputs.p_dma_config));
	}
	b &= TEST_GetAddr_DMA_API(&pattern->expected._p_dma_config, &func_params);

	b &= TEST_Validate_DMA_API(&outputs, &pattern->expected, pattern->validator);

	TEST_ValidateResult(b, params);

	ut_deinit_config();

	TEST_DestroyParam(params);

	return b;
}
