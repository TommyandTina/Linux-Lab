#include <stdio.h>
#include <string.h>
#include "testenv.h"
#include "testfw.h"

#include "file.h"
#include "test_case.h"

extern void TEST_UT_main(int argc, char *argv[])
{
	TEST_main(argc, argv, "UT", "MODULE_TEST", TEST_UT_Info);
}

extern void TEST_run(const char *target)
{
	TEST_RunTestByName(TEST_UT_Info, target);
}

/******************** dummy functions ********************/

