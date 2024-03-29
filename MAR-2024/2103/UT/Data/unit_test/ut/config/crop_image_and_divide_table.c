#include "testenv.h"

TEST_CASE_F(UT, crop_image_and_divide, RPI3, crop_image_and_divide_0001) { EXPECT_EQ( true, TEST_crop_image_and_divide("PCL", 1)); }
TEST_CASE_F(UT, crop_image_and_divide, RPI3, crop_image_and_divide_0002) { EXPECT_EQ( true, TEST_crop_image_and_divide("PCL", 2)); }
TEST_CASE_F(UT, crop_image_and_divide, RPI3, crop_image_and_divide_0003) { EXPECT_EQ( true, TEST_crop_image_and_divide("PCL", 3)); }
TEST_CASE_F(UT, crop_image_and_divide, RPI3, crop_image_and_divide_0004) { EXPECT_EQ( true, TEST_crop_image_and_divide("PCL", 4)); }
TEST_CASE_F(UT, crop_image_and_divide, RPI3, crop_image_and_divide_0005) { EXPECT_EQ( true, TEST_crop_image_and_divide("PCL", 5)); }
TEST_CASE_F(UT, crop_image_and_divide, RPI3, crop_image_and_divide_0006) { EXPECT_EQ( true, TEST_crop_image_and_divide("PCL", 6)); }
TEST_CASE_F(UT, crop_image_and_divide, RPI3, crop_image_and_divide_0007) { EXPECT_EQ( true, TEST_crop_image_and_divide("PCL", 7)); }
TEST_CASE_F(UT, crop_image_and_divide, RPI3, crop_image_and_divide_0008) { EXPECT_EQ( true, TEST_crop_image_and_divide("PCL", 8)); }
TEST_CASE_F(UT, crop_image_and_divide, RPI3, crop_image_and_divide_0009) { EXPECT_EQ( true, TEST_crop_image_and_divide("PCL", 9)); }

struct TestCase UT_crop_image_and_divide_All_Tests[] = {
	TEST_CASE_T(UT, crop_image_and_divide, RPI3, crop_image_and_divide_0001, crop_image_and_divide_0001),
	TEST_CASE_T(UT, crop_image_and_divide, RPI3, crop_image_and_divide_0002, crop_image_and_divide_0002),
	TEST_CASE_T(UT, crop_image_and_divide, RPI3, crop_image_and_divide_0003, crop_image_and_divide_0003),
	TEST_CASE_T(UT, crop_image_and_divide, RPI3, crop_image_and_divide_0004, crop_image_and_divide_0004),
	TEST_CASE_T(UT, crop_image_and_divide, RPI3, crop_image_and_divide_0005, crop_image_and_divide_0005),
    TEST_CASE_T(UT, crop_image_and_divide, RPI3, crop_image_and_divide_0006, crop_image_and_divide_0006),
	TEST_CASE_T(UT, crop_image_and_divide, RPI3, crop_image_and_divide_0007, crop_image_and_divide_0007),
	TEST_CASE_T(UT, crop_image_and_divide, RPI3, crop_image_and_divide_0008, crop_image_and_divide_0008),
	TEST_CASE_T(UT, crop_image_and_divide, RPI3, crop_image_and_divide_0009, crop_image_and_divide_0009),    
	TEST_CASE_END
};