# Create a script to read a log file and count the number of "FAILED" and "OK" log,
# then print out the result to monitor console.

#!/bin/bash
if [ "$#" -ne 1 ]; then 
    echo "Please enter: $0 <file_path>"
    exit 1
fi
filename=$1
total_cases=$(grep -c 'OK\|FAILED' "$filename")
ok_cases=$(grep -c 'OK' "$filename")
failed_cases=$(grep -c 'FAILED' "$filename")

echo -e "Total cases:$total_cases"
echo -e "\e[32mOK cases:$ok_cases\e[0m"
echo -e "\e[31mFailed Cases:$failed_cases\e[0m"


