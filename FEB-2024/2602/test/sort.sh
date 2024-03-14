# Create a script to read a log file and count the number of "FAILED" and "OK" log,
# then print out the result to monitor console.

#!/bin/bash

file="99_exercise_00_BASH_New_Training_TCODE_SampleApp_cdf_App_ADC_U2AEVA1_BGA516.arxml"

# Use grep to find lines containing UUID and then use sed to extract the UUID
grep -o 'UUID="[0-9a-f\-]*"' "$file" | sed 's/UUID="\([0-9a-f\-]*\)"/\1/'
