#include "testenv.h"


TEST_CASE_F(UT, DMA_API, RPI3, DMA_API_0001) { EXPECT_EQ( true, TEST_DMA_API("PCL", 1)); }
TEST_CASE_F(UT, DMA_API, RPI3, DMA_API_0002) { EXPECT_EQ( true, TEST_DMA_API("PCL", 2)); }
TEST_CASE_F(UT, DMA_API, RPI3, DMA_API_0003) { EXPECT_EQ( true, TEST_DMA_API("PCL", 3)); }
TEST_CASE_F(UT, DMA_API, RPI3, DMA_API_0004) { EXPECT_EQ( true, TEST_DMA_API("PCL", 4)); }
TEST_CASE_F(UT, DMA_API, RPI3, DMA_API_0005) { EXPECT_EQ( true, TEST_DMA_API("PCL", 5)); }
TEST_CASE_F(UT, DMA_API, RPI3, DMA_API_0006) { EXPECT_EQ( true, TEST_DMA_API("PCL", 6)); }
TEST_CASE_F(UT, DMA_API, RPI3, DMA_API_0007) { EXPECT_EQ( true, TEST_DMA_API("PCL", 7)); }
TEST_CASE_F(UT, DMA_API, RPI3, DMA_API_0008) { EXPECT_EQ( true, TEST_DMA_API("PCL", 8)); }
TEST_CASE_F(UT, DMA_API, RPI3, DMA_API_0009) { EXPECT_EQ( true, TEST_DMA_API("PCL", 9)); }
// TEST_CASE_F(UT, DMA_API, RPI3, DMA_API_0010) { EXPECT_EQ( true, TEST_DMA_API("PCL", 10)); }

struct TestCase UT_DMA_API_All_Tests[] = {
	TEST_CASE_T(UT, DMA_API, RPI3, DMA_API_0001, DMA_API_0001),//{ "UT", "DMA_API", "RPI3", "DMA_API_0001", UT_DMA_API_DMA_API_0001_RPI3_Test }
	TEST_CASE_T(UT, DMA_API, RPI3, DMA_API_0002, DMA_API_0002),
	TEST_CASE_T(UT, DMA_API, RPI3, DMA_API_0003, DMA_API_0003),
	TEST_CASE_T(UT, DMA_API, RPI3, DMA_API_0004, DMA_API_0004),
	TEST_CASE_T(UT, DMA_API, RPI3, DMA_API_0005, DMA_API_0005),
	TEST_CASE_T(UT, DMA_API, RPI3, DMA_API_0006, DMA_API_0006),
	TEST_CASE_T(UT, DMA_API, RPI3, DMA_API_0007, DMA_API_0007),
	TEST_CASE_T(UT, DMA_API, RPI3, DMA_API_0008, DMA_API_0008),
	TEST_CASE_T(UT, DMA_API, RPI3, DMA_API_0009, DMA_API_0009),
	// TEST_CASE_T(UT, DMA_API, RPI3, DMA_API_0010, DMA_API_0010),
	TEST_CASE_END
};

/*
#define TEST_CASE_F(type, func, target, id)\
	void type##_##func##_##id##_##target##_Test()

#define TEST_CASE_T(type, func, target, funcid, id)\
	{ #type, #func, #target, #id, TEST_FUNC_NAME(type##_##func, target, funcid)	}

TEST_CASE_F(UT, DMA_API, RPI3, DMA_API_0001) { EXPECT_EQ( true, TEST_DMA_API("PCL", 1)); }
can be expanded to
void UT_DMA_API_DMA_API_0001_RPI3_Test(){
	_Bool val1 = 1; 
	_Bool val2 = TEST_DMA_API("PCL", 1); // the process of testing is here
	if (val1 == val2) 
	{ 
		printf("[          OK ] %s (from testenv.h)\n\n\n\n", g_test.runningTestName);
		g_test.passed++; 
	} 
	else 
	{ 
		printf("%s:%d: Failure\n", "C:\\Users\\long.trinh-tien\\Documents\\Linux-Lab\\MAR-2024\\2103\\UT\\Data\\unit_test\\ut\\DMA\\DMA_API_table.c", 4); // 4 is the line we want to mention
		printf("\tExpected: %s\n", (val1) ? "true" : "false"); 
		printf("\tWhich is: %s\n", (val2) ? "true" : "false"); 
		printf("[          NG ] %s\n", g_test.runningTestName); 
		g_test.failed++; 
	}
}
*/