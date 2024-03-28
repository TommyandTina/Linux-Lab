#include "testenv.h"

TEST_CASE_F(UT, check_image_and_square, RPI3, check_image_and_square_0001) { EXPECT_EQ( true, TEST_check_image_and_square("PCL", 1)); }
TEST_CASE_F(UT, check_image_and_square, RPI3, check_image_and_square_0002) { EXPECT_EQ( true, TEST_check_image_and_square("PCL", 2)); }
TEST_CASE_F(UT, check_image_and_square, RPI3, check_image_and_square_0003) { EXPECT_EQ( true, TEST_check_image_and_square("PCL", 3)); }
TEST_CASE_F(UT, check_image_and_square, RPI3, check_image_and_square_0004) { EXPECT_EQ( true, TEST_check_image_and_square("PCL", 4)); }
TEST_CASE_F(UT, check_image_and_square, RPI3, check_image_and_square_0005) { EXPECT_EQ( true, TEST_check_image_and_square("PCL", 5)); }
TEST_CASE_F(UT, check_image_and_square, RPI3, check_image_and_square_0006) { EXPECT_EQ( true, TEST_check_image_and_square("PCL", 6)); }

struct TestCase UT_check_image_and_square_All_Tests[] = {
	TEST_CASE_T(UT, check_image_and_square, RPI3, check_image_and_square_0001, check_image_and_square_0001),
	TEST_CASE_T(UT, check_image_and_square, RPI3, check_image_and_square_0002, check_image_and_square_0002),
	TEST_CASE_T(UT, check_image_and_square, RPI3, check_image_and_square_0003, check_image_and_square_0003),
	TEST_CASE_T(UT, check_image_and_square, RPI3, check_image_and_square_0004, check_image_and_square_0004),
	TEST_CASE_T(UT, check_image_and_square, RPI3, check_image_and_square_0005, check_image_and_square_0005),
	TEST_CASE_T(UT, check_image_and_square, RPI3, check_image_and_square_0006, check_image_and_square_0006),
    TEST_CASE_END
};
