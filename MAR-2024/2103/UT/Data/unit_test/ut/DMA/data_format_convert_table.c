#include "testenv.h"


TEST_CASE_F(UT, data_format_convert, RPI3, data_format_convert_0001) { EXPECT_EQ( true, TEST_data_format_convert("PCL", 1)); }
TEST_CASE_F(UT, data_format_convert, RPI3, data_format_convert_0002) { EXPECT_EQ( true, TEST_data_format_convert("PCL", 2)); }
TEST_CASE_F(UT, data_format_convert, RPI3, data_format_convert_0003) { EXPECT_EQ( true, TEST_data_format_convert("PCL", 3)); }
TEST_CASE_F(UT, data_format_convert, RPI3, data_format_convert_0004) { EXPECT_EQ( true, TEST_data_format_convert("PCL", 4)); }
TEST_CASE_F(UT, data_format_convert, RPI3, data_format_convert_0005) { EXPECT_EQ( true, TEST_data_format_convert("PCL", 5)); }
TEST_CASE_F(UT, data_format_convert, RPI3, data_format_convert_0006) { EXPECT_EQ( true, TEST_data_format_convert("PCL", 6)); }
TEST_CASE_F(UT, data_format_convert, RPI3, data_format_convert_0007) { EXPECT_EQ( true, TEST_data_format_convert("PCL", 7)); }

struct TestCase UT_data_format_convert_All_Tests[] = {
	TEST_CASE_T(UT, data_format_convert, RPI3, data_format_convert_0001, data_format_convert_0001),
	TEST_CASE_T(UT, data_format_convert, RPI3, data_format_convert_0002, data_format_convert_0002),
	TEST_CASE_T(UT, data_format_convert, RPI3, data_format_convert_0003, data_format_convert_0003),
	TEST_CASE_T(UT, data_format_convert, RPI3, data_format_convert_0004, data_format_convert_0004),
	TEST_CASE_T(UT, data_format_convert, RPI3, data_format_convert_0005, data_format_convert_0005),
	TEST_CASE_T(UT, data_format_convert, RPI3, data_format_convert_0006, data_format_convert_0006),
	TEST_CASE_T(UT, data_format_convert, RPI3, data_format_convert_0007, data_format_convert_0007),
	TEST_CASE_END
};
