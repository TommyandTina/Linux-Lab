#include "base.h"
#include "util.h"
#include "patterns/crop_image_and_divide_PCL.h"

static bool TEST_GetAddr_crop_image_and_divide(uint32_t *flag, struct crop_image_and_divide_params *func_params)
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

static bool TEST_Validate_crop_image_and_divide(struct crop_image_and_divide_expect *outputs, struct crop_image_and_divide_expect *expected, bool validator[])
{
	bool b = true;
	uint64_t index = 0;

	b &= TEST_ValidateOutput(&outputs->ReturnValue, &expected->ReturnValue, sizeof(outputs->ReturnValue), "ReturnValue", TEST_VALIDATOR_RETCODE);

	if (TEST_CheckBitValidator(validator, index++))
	{
		b &= TEST_ValidateOutput(&outputs->_p_image, &expected->_p_image, sizeof(outputs->_p_image), "*p_image", TEST_VALIDATOR_ADDR);
	}

	if (TEST_CheckBitValidator(validator, index++))
	{
		b &= TEST_ValidateOutput(&outputs->p_image.width_of_image, &expected->p_image.width_of_image, sizeof(outputs->p_image.width_of_image), "*p_image.width_of_image", TEST_VALIDATOR_I32VALUE);
	}
    
    if (TEST_CheckBitValidator(validator, index++))
	{
		b &= TEST_ValidateOutput(&outputs->p_image.crop_size, &expected->p_image.crop_size, sizeof(outputs->p_image.crop_size), "*p_image.crop_size", TEST_VALIDATOR_I32VALUE);
	}

	return b;
}

bool TEST_crop_image_and_divide(const char *category, int32_t no)
{
	bool b = true;
	struct TestParams *params = TEST_CreateParam("crop_image_and_divide", category, no);
	struct TEST_crop_image_and_divide_Pattern *pattern = &crop_image_and_divide_PCL[no - 1];
	struct crop_image_and_divide_input	*inputs = &pattern->input;
	struct crop_image_and_divide_params	func_params = {0};
	struct crop_image_and_divide_expect	outputs = {0};

	ut_init_config(false);

	if (inputs->_p_image == TEST_ADDR_NULL)
	{
		func_params.p_image = NULL;
	}
	else
	{
		func_params.p_image = &inputs->p_image;
	}
	memcpy(&func_params.divisor, &inputs->divisor, sizeof(func_params.divisor));

	outputs.ReturnValue = crop_image_and_divide(func_params.p_image, func_params.divisor);

	if (pattern->expected._p_image == TEST_ADDR_NULL || pattern->expected._p_image == TEST_ADDR_NOT_NULL)
	{
		outputs._p_image = (func_params.p_image == NULL) ? TEST_ADDR_NULL : TEST_ADDR_NOT_NULL;
	}
	else
	{
		outputs._p_image = (uint32_t)func_params.p_image;
	}
	if (func_params.p_image != NULL)
	{
		memcpy(&outputs.p_image , func_params.p_image, sizeof(outputs.p_image));
	}
	b &= TEST_GetAddr_crop_image_and_divide(&pattern->expected._p_image, &func_params);

	b &= TEST_Validate_crop_image_and_divide(&outputs, &pattern->expected, pattern->validator);

	TEST_ValidateResult(b, params);

	ut_deinit_config();

	TEST_DestroyParam(params);

	return b;
}
