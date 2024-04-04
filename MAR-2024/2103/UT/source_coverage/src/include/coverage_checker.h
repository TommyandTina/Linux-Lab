#ifndef COVERAGE_CHECKER_H
#define COVERAGE_CHECKER_H

#define STRINGIFY(x) #x

#define ANSI_COLOR_RED     "\x1b[31m"
#define ANSI_COLOR_GREEN   "\x1b[32m"
#define ANSI_COLOR_RESET   "\x1b[0m"
#define ANSI_COLOR_YELLOW  "\x1b[101m" //Light Red background, not yellow
 
#define C0C1_checker(line_C0C1_is_activated, function_count_C0C1) \
    if (line_C0C1_is_activated) {\
        function_count_C0C1 = 1; \
        printf(ANSI_COLOR_YELLOW "[V] The function_count: %s passed C0C1 coverage check (from coverage_checker.h)\n" ANSI_COLOR_RESET, STRINGIFY(function_count_C0C1)); \
        line_C0C1_is_activated = false;}

#define C2_checker(subexpression_C2_is_activated, subexpression, function_count_C2_true, function_count_C2_false) \
    if (subexpression_C2_is_activated) {\
        if (subexpression) {\
            function_count_C2_true = 1;} \
        if (!(subexpression)) {\
            function_count_C2_false = 1;} \
        if (function_count_C2_true == 1 && function_count_C2_false == 1) {\
            printf(ANSI_COLOR_GREEN "[V] The subexpression: %s passed C2 coverage check (from coverage_checker.h)\n" ANSI_COLOR_RESET, STRINGIFY(subexpression)); \
            subexpression_C2_is_activated = false;}}

// void C2_PATH_Checker

// #define C2_PATH_Checker(total_subexpression,...) MACRO_FUNC(__VA_ARGS__)
#endif