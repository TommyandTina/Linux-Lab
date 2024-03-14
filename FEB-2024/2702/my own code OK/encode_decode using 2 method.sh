#!/bin/bash

encode() {
    echo "$1" | awk '
    {
        chars = $0
        count = 1
        for (i = 2; i <= length($0) + 1; i++) {
            if (substr(chars, i, 1) == substr(chars, i-1, 1)) {
                count++
            } else {
                if (count > 1) printf count
                printf substr(chars, i-1, 1)
                count = 1
            }
        }
        print ""
    }'
}
encodebasic() {
    echo -n "$1" | awk '
    BEGIN{ORS=""}
    {
        split($0, chars, "")
        count = 1
        for (i = 2; i <= length($0) + 1; i++) {
            if (chars[i] == chars[i-1]) {
                count++
            } else {
                if (count > 1) printf count
                printf chars[i-1]
                count = 1
            }
        }
        print ""
    }'
}

decodebasic() {
    echo -n "$1" | awk '
    BEGIN{ORS=""}
    {
        split($0, chars, "")
        count = ""
        for (i = 1; i <= length($0); i++) {
            if (chars[i] ~ /[0-9]/) {
                count = count chars[i]
            } else {
                if (count == "") count = 1
                for (j = 1; j <= count; j++) {
                    printf chars[i]
                }
                count = ""
            }
        }
        print ""
    }'
    echo ""
}

decode() {
    echo -n "$1" | awk '
    {
        split($0, chars, "")
        count = ""
        for (i = 1; i <= length($0); i++) {
            if (chars[i] ~ /[0-9]/) {
                count = count chars[i]
            } else {
                if (count == "") count = 1
                for (j = 1; j <= count; j++) {
                    printf chars[i]
                }
                count = ""
            }
        }
        print ""
    }'
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
