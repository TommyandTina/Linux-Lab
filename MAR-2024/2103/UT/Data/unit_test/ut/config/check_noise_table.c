#include "testenv.h"

TEST_CASE_F(UT, check_noise, RPI3, check_noise_0001) { EXPECT_EQ( true, TEST_check_noise("PCL", 1)); }
TEST_CASE_F(UT, check_noise, RPI3, check_noise_0002) { EXPECT_EQ( true, TEST_check_noise("PCL", 2)); }
TEST_CASE_F(UT, check_noise, RPI3, check_noise_0003) { EXPECT_EQ( true, TEST_check_noise("PCL", 3)); }
TEST_CASE_F(UT, check_noise, RPI3, check_noise_0004) { EXPECT_EQ( true, TEST_check_noise("PCL", 4)); }
TEST_CASE_F(UT, check_noise, RPI3, check_noise_0005) { EXPECT_EQ( true, TEST_check_noise("PCL", 5)); }
struct TestCase UT_check_noise_All_Tests[] = {
	TEST_CASE_T(UT, check_noise, RPI3, check_noise_0001, check_noise_0001),
	TEST_CASE_T(UT, check_noise, RPI3, check_noise_0002, check_noise_0002),
	TEST_CASE_T(UT, check_noise, RPI3, check_noise_0003, check_noise_0003),
	TEST_CASE_T(UT, check_noise, RPI3, check_noise_0004, check_noise_0004),
	TEST_CASE_T(UT, check_noise, RPI3, check_noise_0005, check_noise_0005),
	TEST_CASE_END
};