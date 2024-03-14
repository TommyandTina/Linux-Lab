#!/bin/bash

# Hàm in thanh tiến trình
print_progress() {
    local iteration=0
    local total=0
    local decimals=1
    local length=100
    local fill='█'

    # Process command-line arguments using a while loop
    while [[ "$#" -gt 0 ]]; do
        case "$1" in
            -i) iteration="$2"; shift 2;;
            -t) total="$2"; shift 2;;
            -d) decimals="$2"; shift 2;;
            -l) length="$2"; shift 2;;
            -f) fill="$2"; shift 2;;
            *) echo "Invalid argument: $1"; exit 1;;
        esac
    done

    percent=$(bc -l <<< "scale=2; $iteration/$total*100.00")
    filledLength=$(bc <<< "$length*$iteration/$total")
    bar=$(printf "%${filledLength}s" | tr ' ' "$fill")
    empty=$(printf "%$(bc <<< "$length-$filledLength")s"| tr ' ' '-')
    printf "|%s%s| %s%%\r" "$bar" "$empty" "$percent"

}

write_large_file(){
    
    file_name="sample_file.txt"
    file_size=$((1 * 1024 * 1024)) # 30MB
    file_smallest_part=$((1024 * 1024)) # 1MB = 1024 KBs * 1024 bytes
    total_step=$(($file_size / $file_smallest_part))
    
    #Delete exist file (if any)
    if [ -f "$file_name" ]; then
        rm $file_name
    fi

    echo "Creating a file name \"sample_file.txt\" with random contents (size is $((file_size/(1024*1024))) MB)"

    for i in $(seq 1 $total_step); do
        # Generate random content and append to file
        head -c $file_smallest_part /dev/urandom >> "$file_name"

        # Update progress bar
        print_progress -i $i -t $total_step -d 1 -l 50 -f '█'
    done

    echo -ne '\n' # Move to a new line after completion

    # Check if the file exists and its size
    if [ -f "$file_name" ]; then
        echo "$file_name has been created."
        file_result_size=$(stat -c%s "$file_name")
        echo "Size: $((file_result_size/(1024*1024))) MB"
    else
        echo "Failed to create the file."
    fi
}

#TODO
write_large_file