#ifndef _TEST_CASE_H_
#define _TEST_CASE_H_

#ifdef __cplusplus
extern "C" {
#endif /* __cplusplus */

#define DECLARE_TESTCASE_TABLE(func)	extern struct TestCase UT_##func##_All_Tests[]
#define TESTCASE_TABLE(category,func) { #func,	category,	UT_##func##_All_Tests	}

DECLARE_TESTCASE_TABLE(DMA_API);
DECLARE_TESTCASE_TABLE(data_format_convert);
DECLARE_TESTCASE_TABLE(pre_check_config);

static const struct TestInfo TEST_UT_Info[] = 
{
	TESTCASE_TABLE("DMA", DMA_API),
	// TESTCASE_TABLE("DMA", data_format_convert),
	// TESTCASE_TABLE("config", pre_check_config),
	{ NULL, "", NULL }
};

#ifdef __cplusplus
}
#endif
#endif
