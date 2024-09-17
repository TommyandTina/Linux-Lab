#!/bin/bash

input_file="name.txt"

output_file="formatted_includes.txt"

> "$output_file"

while IFS= read -r line
do
    includetext="{INCLUDETEXT \"${line//\//\\}\" \* MERGEFORMAT}"
    
    echo "$includetext" >> "$output_file"
done < "$input_file"

echo "Đã tạo tệp với các trường INCLUDETEXT: $output_file"

