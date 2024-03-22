#include "testenv.h"

TEST_CASE_F(UT, data_format_convert, RPI3, data_format_convert_0001) { EXPECT_EQ( true, TEST_data_format_convert("PCL", 1)); }

struct TestCase UT_data_format_convert_All_Tests[] = {
	TEST_CASE_T(UT, data_format_convert, RPI3, data_format_convert_0001, data_format_convert_0001),
	TEST_CASE_END
};
