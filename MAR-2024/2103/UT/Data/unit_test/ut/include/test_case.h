#ifndef _TEST_CASE_H_
#define _TEST_CASE_H_

#ifdef __cplusplus
extern "C" {
#endif /* __cplusplus */

#define DECLARE_TESTCASE_TABLE(func)	extern struct TestCase UT_##func##_All_Tests[]
#define TESTCASE_TABLE(category,func) { #func,	category,	UT_##func##_All_Tests	}

DECLARE_TESTCASE_TABLE(DMA_API); //extern struct TestCase UT_DMA_API_All_Tests[]
DECLARE_TESTCASE_TABLE(data_format_convert);
DECLARE_TESTCASE_TABLE(pre_check_config);
DECLARE_TESTCASE_TABLE(check_image_and_square);
DECLARE_TESTCASE_TABLE(check_noise);
DECLARE_TESTCASE_TABLE(crop_image_and_divide);

static const struct TestInfo TEST_UT_Info[] = 
{
	TESTCASE_TABLE("DMA", DMA_API), // { "DMA_API", "DMA", UT_DMA_API_All_Tests }
	TESTCASE_TABLE("DMA", data_format_convert),
	TESTCASE_TABLE("config", pre_check_config),
	TESTCASE_TABLE("config",check_image_and_square),
	TESTCASE_TABLE("config",check_noise),
	TESTCASE_TABLE("config",crop_image_and_divide),
	{ NULL, "", NULL }
};

#ifdef __cplusplus
}
#endif
#endif
