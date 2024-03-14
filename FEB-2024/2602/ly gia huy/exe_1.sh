# Create a script to read a log file and count the number of "FAILED" and "OK" log,
# then print out the result to monitor console.

#!/bin/bash

count_log(){
    file_path="$1"
    if [ ! -f "$file_path" ]; then 
        echo "Path_file $1 doesn't exist"
        exist 1
    fi
    
    total_count=$(grep -c "OK\|FAILED" "$file_path")
    ok_count=$(grep -c "OK" "$file_path")
    failed_count=$(grep -c "FAILED" "$file_path")

    echo "Total: $total_count"
    echo -e "OK: \e[32m$ok_count\e[0m"
    echo -e "FAILED: \e[31m$failed_count\e[0m"
}

if [ "$#" -ne 1 ]; then 
    echo "Please enter: $0 <file_path>"
    exit 1
fi

count_log "$1"