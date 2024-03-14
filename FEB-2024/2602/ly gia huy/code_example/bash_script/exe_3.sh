#Create a script to encode and decode the length of the string
# 1. There are two mode: encode and decode
# 2. The unencoded string will only contain the letters A through Z (either lower or upper case) and whitespace.
# 3. The encoded string will only contain the letters A through Z (either lower or upper case), numbers and whitespace.
# Examples:
# "AABCCCDEEEE"  => encode => "2AB3CD4E" => decode =>  "AABCCCDEEEE"

#!bin/bash

encode_string(){
    echo "Encoding..."
    local input="$1"
    echo "Input: \"$input\" "

    # Loop through each character in the input string
    for ((i = 0; i < ${#input}; i++)); do
        if [ "$current_char" == "${input:$i:1}" ]; then
            count=$((count + 1))
        else
            if [ -n "$count" ] && [ "$count" -gt 1 ]; then
                encoded="${encoded}${count}${current_char}"
            else
                encoded="${encoded}${current_char}"
            fi
            current_char="${input:$i:1}"
            count=1
        fi
    done

    if [ "$count" -gt 1 ]; then
        encoded="${encoded}${count}${current_char}"
    else
        encoded="${encoded}${current_char}"
    fi
    echo "Output: \"$encoded\" "    
}

decode_string(){
    echo "Decoding..."
    local input="$1"
    local count=1
    local decoded=""
    
    echo "Input: \"$input\" "

    # Loop through each character in the input string
    for ((i = 0; i < ${#input}; i++)); do
        if [[ "${input:$i:1}" =~ [0-9] ]]; then
            count="${input:$i:1}"
        else
            for((j = 0; j < $count; j++));do
            decoded="${decoded}${input:$i:1}"
            done
            count=1
        fi
    done
    echo "Output: \"$decoded\" "
}

string_input="$1"
mode=0

while [[ "$#" -gt 0 ]]; do
    if [ "$1" == '-m' ]; then
        mode="$2"
        break
    fi
    shift 1;
done

if [ "$mode" == "en" ]; then
    encoded_string=$(encode_string "$string_input")
    echo "$encoded_string"
elif [ "$mode" == "de" ]; then
    decode_string=$(decode_string "$string_input")
    echo "$decode_string"
else
    echo "Invalid mode..."
    echo "Please enter the following format: $0 \"<string>\" -m en/de."
    exit 1
fi
