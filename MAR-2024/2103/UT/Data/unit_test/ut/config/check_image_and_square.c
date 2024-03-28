#include "base.h"
#include "util.h"
#include "patterns/check_image_and_square_PCL.h"
//check_image_and_square_PCL.h include check_image_and_square.h

static bool TEST_GetAddr_check_image_and_square(uint32_t *flag, struct check_image_and_square_params *func_params)
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

/*Test Return value, p_image->width_of_image and p_image->height_of_image.*/
static bool TEST_Validate_check_image_and_square(struct check_image_and_square_expect *outputs, struct check_image_and_square_expect *expected, bool validator[])
{
	bool b = true;
	uint64_t index = 0;

	b &= TEST_ValidateOutput(&outputs->ReturnValue, &expected->ReturnValue, sizeof(outputs->ReturnValue), "ReturnValue", TEST_VALIDATOR_RETCODE);

	if (TEST_CheckBitValidator(validator, index++))
	{
		b &= TEST_ValidateOutput(&outputs->p_image.width_of_image, &expected->p_image.width_of_image, sizeof(outputs->p_image.width_of_image), "p_image.width_of_image", TEST_VALIDATOR_I32VALUE);
	}

	if (TEST_CheckBitValidator(validator, index++))
	{
		b &= TEST_ValidateOutput(&outputs->p_image.height_of_image, &expected->p_image.height_of_image, sizeof(outputs->p_image.height_of_image), "p_image.height_of_image", TEST_VALIDATOR_I32VALUE);
	}

	return b;
}

bool TEST_check_image_and_square(const char *category, int32_t no)
{
    //Parameter init
	bool b = true;
	struct TestParams *params = TEST_CreateParam("check_image_and_square", category, no);
	struct TEST_check_image_and_square_Pattern *pattern = &check_image_and_square_PCL[no - 1];
	struct check_image_and_square_input	*inputs = &pattern->input;
	struct check_image_and_square_params	func_params = {0};
	struct check_image_and_square_expect	outputs = {0};

	ut_init_config(false);

    /*Copy 4 parameter in input struct to function parameter*/
    //Copy data from input to function parameters - 1 and 2
	memcpy(&func_params.p_image, &inputs->p_image, sizeof(func_params.p_image));
	memcpy(&func_params.p_square, &inputs->p_square, sizeof(func_params.p_square));

    //copy pointer for p_image - 3
    if (inputs->_p_image == TEST_ADDR_NULL)
	{
		func_params.p_image = NULL;
	}
	else
	{
		func_params.p_image = &inputs->p_image;
	}

    //copy pointer for p_square - 4 done
    if (inputs->_p_square == TEST_ADDR_NULL)
	{
		func_params.p_square = NULL;
	}
	else
	{
		func_params.p_square = &inputs->p_square;
	}

    //run function, store to outputs (3 value + 2 struct*3value_each) - 1
	outputs.ReturnValue = check_image_and_square(func_params.p_image, func_params.p_square);

    //Just check NULL/NOT_NULL or implement a specific address ? for p_image - 2 
	if (pattern->expected._p_image == TEST_ADDR_NULL || pattern->expected._p_image == TEST_ADDR_NOT_NULL)
	{
		outputs._p_image = (func_params.p_image == NULL) ? TEST_ADDR_NULL : TEST_ADDR_NOT_NULL;
	}
	else
	{
		outputs._p_image = (uint32_t)func_params.p_image;
	}
    //copy result to output - 1st struct*3value_each
	if (func_params.p_image != NULL)
	{
		memcpy(&outputs.p_image , func_params.p_image, sizeof(outputs.p_image));
	}        

    //Just check NULL/NOT_NULL or implement a specific address ? for p_square - 3
	if (pattern->expected._p_square == TEST_ADDR_NULL || pattern->expected._p_square == TEST_ADDR_NOT_NULL)
	{
		outputs._p_square = (func_params.p_square == NULL) ? TEST_ADDR_NULL : TEST_ADDR_NOT_NULL;
	}
	else
	{
		outputs._p_square = (uint32_t)func_params.p_square;
	}     
    //copy result to output - 2nd struct*3value_each DONE
	if (func_params.p_square != NULL)
	{
		memcpy(&outputs.p_square , func_params.p_square, sizeof(outputs.p_square));
	}    


    //check address and store to array
	b &= TEST_GetAddr_check_image_and_square(&pattern->expected._p_image, &func_params);
    b &= TEST_GetAddr_check_image_and_square(&pattern->expected._p_square, &func_params);

	b &= TEST_Validate_check_image_and_square(&outputs, &pattern->expected, pattern->validator);

	TEST_ValidateResult(b, params);

	ut_deinit_config();

	TEST_DestroyParam(params);

	return b;
}
