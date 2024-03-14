#!/bin/bash

LENGTH=50
FILLED_LENGTH=10
FILL='#'
PERCENT=10

# for i in $(seq 1 $FILLED_LENGTH); do
#     # Calculate the number of filled and empty characters
#     FILLED_COUNT=$((i > FILLED_LENGTH ? FILLED_LENGTH : i))
#     EMPTY_COUNT=$((LENGTH - FILLED_COUNT))

#     # Create the filled and empty portions of the bar
#     FILLED_BAR=$(printf "%-${FILLED_COUNT}s" | tr ' ' "$FILL")
#     EMPTY_BAR=$(printf "%-${EMPTY_COUNT}s" | tr ' ' '-')

#     # Combine the filled and empty portions to create the progress bar
#     PROGRESS_BAR="${FILLED_BAR}${EMPTY_BAR}"

#     echo -ne "|${PROGRESS_BAR}| ${PERCENT}%\r"
#     sleep 1
# done
ITERATION=1
TOTAL=30
FILLED_LENGTH=$(( ($ITERATION * $LENGTH) / $TOTAL ))
echo $ITERATION