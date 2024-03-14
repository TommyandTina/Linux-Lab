    # local encoded="$1"
    # local decoded=""
    # local current_char=""
    # local count=""
    
    # # Loop through each character in the encoded string
    # for ((i = 0; i < ${#encoded}; i++)); do
    #     if [[ "${encoded:$i:1}" =~ [0-9] ]]; then
    #         # Accumulate digits to get the count
    #         count="${count}${encoded:$i:1}"
    #     else
    #         # Append the character(s) based on the count
    #         if [ -n "$count" ] && [ "$count" -gt 1 ]; then
    #             decoded="${decoded}$(printf "%0.s${encoded:$i:1}" $(seq 1 $count))"
    #             count=""
    #         else
    #             decoded="${decoded}${encoded:$i:1}"
    #         fi
    #     fi
    # done
count=5
i=$((count + 1))
echo $i