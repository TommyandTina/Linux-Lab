#include <stdio.h>
#include <stdint.h>
#include <stdbool.h>
#include <string.h>
#include "testenv.h"

#if defined(TEST_ENV_UT)
extern void TEST_UT_main(int argc, char *argv[]);
#define TEST_MAIN	TEST_UT_main

#else
#error "TEST_ENV Not Specified !!"
#endif

#ifdef CHECK_COVERAGE
#define ANSI_COLOR_RED     "\x1b[31m"
#define ANSI_COLOR_GREEN   "\x1b[32m"
#define ANSI_COLOR_MAGENTA "\x1b[35m"
#define ANSI_COLOR_RESET   "\x1b[0m"

#define DMA_API_TOTAL_STATEMENT 14
#define DATA_FORMAT_CONVERT_TOTAL_STATEMENT 36
#define PRE_CHECK_CONFIG_TOTAL_STATEMENT 12
#define CHECK_IMAGE_AND_SQUARE_TOTAL_STATEMENT 13
#define CHECK_NOISE_TOTAL_STATEMENT 6
#define CROP_IMAGE_AND_DIVIDE_TOTAL_STATEMENT 13

#define DMA_API_TOTAL_SUBEXPRESSION 9
#define DATA_FORMAT_CONVERT_TOTAL_SUBEXPRESSION 2
#define PRE_CHECK_CONFIG_TOTAL_SUBEXPRESSION 9
#define CHECK_IMAGE_AND_SQUARE_TOTAL_SUBEXPRESSION 7
#define CHECK_NOISE_TOTAL_SUBEXPRESSION 5
#define CROP_IMAGE_AND_DIVIDE_TOTAL_SUBEXPRESSION 14

#define SIZE_OF_LIST 100

/* C0C1 */
bool DMA_API_C0C1_line_activate_list[SIZE_OF_LIST];
bool data_format_convert_C0C1_line_activate_list[SIZE_OF_LIST];
bool pre_check_config_C0C1_line_activate_list[SIZE_OF_LIST];
bool check_image_and_square_C0C1_line_activate_list[SIZE_OF_LIST];
bool check_noise_C0C1_line_activate_list[SIZE_OF_LIST];
bool crop_image_and_divide_C0C1_line_activate_list[SIZE_OF_LIST];

uint8_t DMA_API_C0C1_list[SIZE_OF_LIST] = {0};
uint8_t data_format_convert_C0C1_list[SIZE_OF_LIST] = {0};
uint8_t pre_check_config_C0C1_list[SIZE_OF_LIST] = {0};
uint8_t check_image_and_square_C0C1_list[SIZE_OF_LIST] = {0};
uint8_t check_noise_C0C1_list[SIZE_OF_LIST] = {0};
uint8_t crop_image_and_divide_C0C1_list[SIZE_OF_LIST] = {0};

uint32_t DMA_API_C0C1_count = 0;
uint32_t data_format_convert_C0C1_count = 0;
uint32_t pre_check_config_C0C1_count = 0;
uint32_t check_image_and_square_C0C1_count = 0;
uint32_t check_noise_C0C1_count = 0;
uint32_t crop_image_and_divide_C0C1_count = 0;

/* C2 */
bool DMA_API_C2_subexpression_activate_list[SIZE_OF_LIST];
bool data_format_convert_C2_subexpression_activate_list[SIZE_OF_LIST];
bool pre_check_config_C2_subexpression_activate_list[SIZE_OF_LIST];
bool check_image_and_square_C2_subexpression_activate_list[SIZE_OF_LIST];
bool check_noise_C2_subexpression_activate_list[SIZE_OF_LIST];
bool crop_image_and_divide_C2_subexpression_activate_list[SIZE_OF_LIST];

uint8_t DMA_API_C2_list_true[SIZE_OF_LIST] = {0};
uint8_t data_format_convert_C2_list_true[SIZE_OF_LIST] = {0};
uint8_t pre_check_config_C2_list_true[SIZE_OF_LIST] = {0};
uint8_t check_image_and_square_C2_list_true[SIZE_OF_LIST] = {0};
uint8_t check_noise_C2_list_true[SIZE_OF_LIST] = {0};
uint8_t crop_image_and_divide_C2_list_true[SIZE_OF_LIST] = {0};

uint8_t DMA_API_C2_list_false[SIZE_OF_LIST] = {0};
uint8_t data_format_convert_C2_list_false[SIZE_OF_LIST] = {0};
uint8_t pre_check_config_C2_list_false[SIZE_OF_LIST] = {0};
uint8_t check_image_and_square_C2_list_false[SIZE_OF_LIST] = {0};
uint8_t check_noise_C2_list_false[SIZE_OF_LIST] = {0};
uint8_t crop_image_and_divide_C2_list_false[SIZE_OF_LIST] = {0};

uint32_t DMA_API_C2_count = 0;
uint32_t data_format_convert_C2_count = 0;
uint32_t pre_check_config_C2_count = 0;
uint32_t check_image_and_square_C2_count = 0;
uint32_t check_noise_C2_count = 0;
uint32_t crop_image_and_divide_C2_count = 0;

void log_C0C1(char* function_name, uint32_t C0C1_count, uint8_t* C0C1_list, uint32_t total) {
	for (uint32_t i = 0; i < SIZE_OF_LIST; i++) {
		C0C1_count += C0C1_list[i];
	}
	if(C0C1_count < total) {
		printf(ANSI_COLOR_RED "[V][RESULT][%3d%%] C0C1 coverage of %-23s, statements covered: [ACTUAL] %d <==> [EXPECTED] %d\n" ANSI_COLOR_RESET, (C0C1_count*100/total), function_name, C0C1_count, total);
	}
	else {
		printf(ANSI_COLOR_GREEN "[V][RESULT][%3d%%] C0C1 coverage of %-23s, statements covered: [ACTUAL] %d <==> [EXPECTED] %d\n" ANSI_COLOR_RESET, (C0C1_count*100/total), function_name, C0C1_count, total);
	}
}

void log_C2(char* function_name, uint32_t C2_count, uint8_t* C2_list_true, uint8_t* C2_list_false, uint32_t total) {
	for (uint32_t i = 0; i < SIZE_OF_LIST; i++) {
		if (C2_list_true[i] == 1 && C2_list_false[i] == 1) {
			C2_count++;
		}
	}
	if(C2_count < total) {
		printf(ANSI_COLOR_RED "[V][RESULT][%3d%%] C2 coverage of %-23s, subexpressions covered: [ACTUAL] %d <==> [EXPECTED] %d\n" ANSI_COLOR_RESET, (C2_count*100/total), function_name, C2_count, total);
	}
	else {
		printf(ANSI_COLOR_GREEN "[V][RESULT][%3d%%] C2 coverage of %-23s, subexpressions covered: [ACTUAL] %d <==> [EXPECTED] %d\n" ANSI_COLOR_RESET, (C2_count*100/total), function_name, C2_count, total);
	}
}

#endif

int main(int argc, char *argv[])
{
	setvbuf(stdout, NULL, _IONBF, BUFSIZ);
	#ifdef CHECK_COVERAGE
	for (uint32_t i = 0; i < 100; i++) {
		DMA_API_C0C1_line_activate_list[i] = true;
		data_format_convert_C0C1_line_activate_list[i] = true;
		pre_check_config_C0C1_line_activate_list[i] = true;
		check_image_and_square_C0C1_line_activate_list[i] = true;
		check_noise_C0C1_line_activate_list[i] = true;
		crop_image_and_divide_C0C1_line_activate_list[i] = true;

		DMA_API_C2_subexpression_activate_list[i] = true;
		data_format_convert_C2_subexpression_activate_list[i] = true;
		pre_check_config_C2_subexpression_activate_list[i] = true;
		check_image_and_square_C2_subexpression_activate_list[i] = true;
		check_noise_C2_subexpression_activate_list[i] = true;
		crop_image_and_divide_C2_subexpression_activate_list[i] = true;
	}
	#endif
	TEST_MAIN(argc, argv);
	#ifdef CHECK_COVERAGE
	printf(ANSI_COLOR_MAGENTA "\n[I][==========] C0C1 coverage check SUMMARY\n" ANSI_COLOR_RESET);
	log_C0C1("DMA_API", DMA_API_C0C1_count, DMA_API_C0C1_list, DMA_API_TOTAL_STATEMENT);
	log_C0C1("data_format_convert", data_format_convert_C0C1_count, data_format_convert_C0C1_list, DATA_FORMAT_CONVERT_TOTAL_STATEMENT);
	log_C0C1("pre_check_config", pre_check_config_C0C1_count, pre_check_config_C0C1_list, PRE_CHECK_CONFIG_TOTAL_STATEMENT);
	log_C0C1("check_image_and_square", check_image_and_square_C0C1_count, check_image_and_square_C0C1_list, CHECK_IMAGE_AND_SQUARE_TOTAL_STATEMENT);
	log_C0C1("check_noise", check_noise_C0C1_count, check_noise_C0C1_list, CHECK_NOISE_TOTAL_STATEMENT);
	log_C0C1("crop_image_and_divide", crop_image_and_divide_C0C1_count, crop_image_and_divide_C0C1_list, CROP_IMAGE_AND_DIVIDE_TOTAL_STATEMENT);
	
	printf(ANSI_COLOR_MAGENTA "\n[I][==========] C2 coverage check SUMMARY\n" ANSI_COLOR_RESET);
	log_C2("DMA_API", DMA_API_C2_count, DMA_API_C2_list_true, DMA_API_C2_list_false, DMA_API_TOTAL_SUBEXPRESSION);
	log_C2("data_format_convert", data_format_convert_C2_count, data_format_convert_C2_list_true, data_format_convert_C2_list_false, DATA_FORMAT_CONVERT_TOTAL_SUBEXPRESSION);
	log_C2("pre_check_config", pre_check_config_C2_count, pre_check_config_C2_list_true, pre_check_config_C2_list_false, PRE_CHECK_CONFIG_TOTAL_SUBEXPRESSION);
	log_C2("check_image_and_square", check_image_and_square_C2_count, check_image_and_square_C2_list_true, check_image_and_square_C2_list_false, CHECK_IMAGE_AND_SQUARE_TOTAL_SUBEXPRESSION);
	log_C2("check_noise", check_noise_C2_count, check_noise_C2_list_true, check_noise_C2_list_false, CHECK_NOISE_TOTAL_SUBEXPRESSION);
	log_C2("crop_image_and_divide", crop_image_and_divide_C2_count, crop_image_and_divide_C2_list_true, crop_image_and_divide_C2_list_false, CROP_IMAGE_AND_DIVIDE_TOTAL_SUBEXPRESSION);
	#endif
}

