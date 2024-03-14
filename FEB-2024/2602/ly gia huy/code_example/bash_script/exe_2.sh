# Create a function to print progress bar to monitor console and using this function in script
#to get progress for user while writting a large file.


print_progress_bar() {
    # Initialize variables with default values
    local ITERATION=0
    local TOTAL=1
    local DECIMALS=1
    local LENGTH=100
    local FILL='█'
    
    # Process command-line arguments using a while loop
    while [[ "$#" -gt 0 ]]; do
        case "$1" in
            -i|--iteration) ITERATION="$2"; shift 2;;
            -t|--total) TOTAL="$2"; shift 2;;
            -d|--decimals) DECIMALS="$2"; shift 2;;
            -l|--length) LENGTH="$2"; shift 2;;
            -f|--fill) FILL="$2"; shift 2;;
            *) echo "Invalid argument: $1"; exit 1;;
        esac
    done

    # Calculate the width of the percent based on the decimals
    local PERCENT=$(awk "BEGIN {printf \"%.${DECIMALS}f\", ($ITERATION/$TOTAL)*100}")

    # Calculate how many fills should be shown
    local FILLED_LENGTH=$(echo "scale=0; ($ITERATION * $LENGTH) / $TOTAL" | bc)
    local ITERATION=$(echo "scale=0; ($PERCENT * $LENGTH) / 100" | bc)

    # Calculate the number of filled and empty characters
    FILLED_COUNT=$((ITERATION > LENGTH ? LENGTH : ITERATION))
    EMPTY_COUNT=$((LENGTH - FILLED_COUNT))

    # Create the filled and empty portions of the bar
    FILLED_BAR=$(printf "%-${FILLED_COUNT}s" | tr ' ' "$FILL")
    EMPTY_BAR=$(printf "%-${EMPTY_COUNT}s" | tr ' ' '-')

    # Combine the filled and empty portions to create the progress bar
    PROGRESS_BAR="${FILLED_BAR}${EMPTY_BAR}"

    # Print the progress bar with the calculated percent
    echo -ne "|${PROGRESS_BAR}| ${PERCENT}%\r"
}

#!/bin/bash

FILE_NAME="written_file.txt"
TARGET_SIZE=$((30 * 1024 * 1024)) # 30MB
BUFFER_SIZE=$((1024 * 1024)) # 1MB buffer size
TOTAL_ITERATIONS=$(($TARGET_SIZE / $BUFFER_SIZE))

echo "Creating a file name \"written_file.txt\" with random contents (size is 30MB)"

for i in $(seq 1 $TOTAL_ITERATIONS); do
    # Generate random content and append to file
    head -c $BUFFER_SIZE /dev/urandom >> "$FILE_NAME"

    # Update progress bar
    print_progress_bar -i $i -t $TOTAL_ITERATIONS -d 1 -l 50 -f '#'
done

echo -ne '\n' # Move to a new line after completion

# Check if the file exists and its size
if [ -f "$FILE_NAME" ]; then
    echo "File $FILE_NAME has been created successfully."
    FILE_SIZE=$(stat -c%s "$FILE_NAME")
    echo "File Size: $FILE_SIZE bytes"
else
    echo "Failed to create the file."
fi
