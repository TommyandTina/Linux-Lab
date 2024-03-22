#include "testenv.h"

TEST_CASE_F(UT, pre_check_config, RPI3, pre_check_config_0001) { EXPECT_EQ( true, TEST_pre_check_config("PCL", 1)); }

struct TestCase UT_pre_check_config_All_Tests[] = {
	TEST_CASE_T(UT, pre_check_config, RPI3, pre_check_config_0001, pre_check_config_0001),
	TEST_CASE_END
};
