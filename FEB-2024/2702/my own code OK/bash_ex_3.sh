#!/bin/bash

encode() {
    input="$1"
    length=${#input}

    result=""

    #count same character: take current_char and compare with next_char, if they are identify -> keep checking. When they are not the same -> print [num][char] (dont print num =1)
    count=1 
    for ((i = 0; i < length; i++)); do
        current_char="${input:i:1}" 
        next_char="${input:i+1:1}"
        if [[ $current_char == $next_char ]]; then
            ((count++))
        else
            if ((count > 1)); then
                result="$result$count$current_char"
            else
                result="$result$current_char"
            fi
            count=1
        fi
    done
    echo "$result"
}


decode() {
    input="$1"
    length=${#input}
    result="" #create empty var

    #extract char base on num to result:
    char_buffer="" #3E -> EEE -> store to char_buffer -> concatnate with result
    for ((i = 0; i < length; i++)); do
        char="${input:i:1}"
        if [[ $char =~ [0-9] ]]; then
            char_buffer="$char_buffer$char"
        else
            if [[ -z $char_buffer ]]; then
                char_buffer=1 #keep our result because there is no number before this char
            fi
            for ((j = 0; j < char_buffer; j++)); do
                result="$result$char" #transfer char_buffer into result
            done
            char_buffer="" #reset char buffer
        fi
    done
    echo "$result"
}



mode=$1
input=$2

if [[ $mode == "encode" ]]; then
    encode "$input"
elif [[ $mode == "decode" ]]; then
    decode "$input"
else
    echo "Invalid mode. Please use 'encode' or 'decode'."
fi
