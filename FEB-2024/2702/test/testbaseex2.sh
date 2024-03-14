#!/bin/bash
# Hàm để in ra thanh tiến trình
progress_bar() {
    # Tham số đầu tiên là tổng số lần lặp
    local total=$1
    # Tham số thứ hai là số lần lặp hiện tại
    local current=$2
    # Tham số thứ ba là số thập phân trong phần trăm hoàn thành (mặc định là 1)
    local decimals=${3:-1}
    # Tham số thứ tư là chiều dài của thanh tiến trình (mặc định là 100)
    local length=${4:-100}
    # Tham số thứ năm là ký tự để lấp đầy thanh tiến trình (mặc định là '█')
    local fill=${5:-'█'}
    # Tính toán phần trăm hoàn thành
    local percent=$(printf "%.${decimals}f" "$(echo "$current/$total*100" | bc -l)")
    # Tính toán số lượng ký tự đã hoàn thành và chưa hoàn thành
    local filled=$(printf "%.0f" "$(echo "$current/$total*$length" | bc -l)")
    local empty=$((length - filled))
 # In ra thanh tiến trình với định dạng mong muốn
printf "["
    printf "%0.s$fill" $(seq 1 $filled)
    printf "%0.s " $(seq 1 $empty)
    printf "] $percent%%\r"
}
# Hàm để tạo một tệp lớn với nội dung ngẫu nhiên
write_large_file() {
    # Tham số đầu tiên là tên của tệp
    local filename=$1
    # Tham số thứ hai là kích thước tối thiểu của tệp (tính bằng MB)
    local size=$2
    # Tạo một tệp trống
    touch $filename
    # Tính toán số lượng byte cần ghi
    local bytes=$((size * 1024 * 1024))
    # Thiết lập biến để theo dõi số lượng byte đã ghi và số lần lặp
    local written=0
    local count=0
    # Thiết lập một số hằng số cho việc ghi tệp
    # Số lượng byte tối đa cho mỗi lần ghi
    local max_chunk=65536
    # Số lượng lần lặp tối đa cho mỗi lần cập nhật thanh tiến trình
    local max_iter=1000
    # Số lượng lần lặp tối thiểu để cập nhật thanh tiến trình ít nhất một lần
    local min_iter=$((bytes / max_chunk / 100))
    # Bắt đầu vòng lặp để ghi tệp
 while [ $written -lt $bytes ]; do
    # Tăng số lần lặp lên 1
    count=$((count + 1))
    # Sinh ra một số ngẫu nhiên trong khoảng từ 1 đến max_chunk
    local chunk=$(shuf -i 1-$max_chunk -n 1)
    # Ghi số lượng byte tương ứng với số ngẫu nhiên đó vào tệp
    head -c $chunk /dev/urandom >> $filename
    # Cộng số lượng byte đã ghi vào biến written
    written=$((written + chunk))
    # Nếu số lần lặp chia hết cho max_iter hoặc min_iter, hoặc nếu đã ghi xong tất cả các byte
    # thì cập nhật thanh tiến trình
    if [ $((count % max_iter)) -eq 0 ] || [ $((count % min_iter)) -eq 0 ] || [ $written -eq $bytes ]; then
        progress_bar $bytes $written
    fi
 done
 # In ra một dòng mới khi hoàn thành
    printf "\n"
}
# Gọi hàm write_large_file với tên tệp và kích thước mong muốn
write_large_file "large_file.txt" 30