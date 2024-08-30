for file in BSPv5.3.3_USB3F_E3v1.1_No2427_Perf*.log; do
    if [[ $file != "BSPv5.3.3_USB3F_E3v1.1_No2432_Normal_1_20240808.log" ]]; then
        cat BSPv5.3.3_USB3F_E3v1.1_No2432_Normal_1_20240808.log $file > temp && mv temp $file
		echo $file done.
    fi
done

read -p "Nhấn Enter để kết thúc..."