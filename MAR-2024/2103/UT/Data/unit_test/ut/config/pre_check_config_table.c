#include "testenv.h"

TEST_CASE_F(UT, pre_check_config, RPI3, pre_check_config_0001) { EXPECT_EQ( true, TEST_pre_check_config("PCL", 1)); }
TEST_CASE_F(UT, pre_check_config, RPI3, pre_check_config_0002) { EXPECT_EQ( true, TEST_pre_check_config("PCL", 2)); }
TEST_CASE_F(UT, pre_check_config, RPI3, pre_check_config_0003) { EXPECT_EQ( true, TEST_pre_check_config("PCL", 3)); }
TEST_CASE_F(UT, pre_check_config, RPI3, pre_check_config_0004) { EXPECT_EQ( true, TEST_pre_check_config("PCL", 4)); }
TEST_CASE_F(UT, pre_check_config, RPI3, pre_check_config_0005) { EXPECT_EQ( true, TEST_pre_check_config("PCL", 5)); }
struct TestCase UT_pre_check_config_All_Tests[] = {
	TEST_CASE_T(UT, pre_check_config, RPI3, pre_check_config_0001, pre_check_config_0001),
	TEST_CASE_T(UT, pre_check_config, RPI3, pre_check_config_0002, pre_check_config_0002),
	TEST_CASE_T(UT, pre_check_config, RPI3, pre_check_config_0003, pre_check_config_0003),
	TEST_CASE_T(UT, pre_check_config, RPI3, pre_check_config_0004, pre_check_config_0004),
	TEST_CASE_T(UT, pre_check_config, RPI3, pre_check_config_0005, pre_check_config_0005),
	TEST_CASE_END
};
