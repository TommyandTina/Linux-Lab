for file in BSPv5.3.3_USB3F_H3v3.0_No3258_S2R*.log; do
    if [[ $file != "BSPv5.3.3_USB3F_H3v3.0_No3258_Normal_1_20240808.log" ]]; then
        cat BSPv5.3.3_USB3F_H3v3.0_No3258_Normal_1_20240808.log $file > temp && mv temp $file
		echo $file done.
    fi
done

read -p "Nhấn Enter để kết thúc..."