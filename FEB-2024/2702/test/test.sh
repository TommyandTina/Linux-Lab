#!/bin/bash

# Kiểm tra số lượng argument
if [ $# -lt 1 ]; then
    echo "Lỗi: Script cần ít nhất 1 argument."
    echo "Cách sử dụng: $0 <argument_1> [<argument_2>]"
    exit 1
fi

# Gán giá trị cho biến
local arg1=$1
arg2=${2:-""}

# Xuất kết quả
echo "Text = $arg1 $arg2"

# Ví dụ:
# ./script.sh "Hello" "World"
# Text = Hello World

# ./script.sh "This"
# Text = This