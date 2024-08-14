for file in *.log; do
    if [[ $file != "BSPv5.3.3_USB3F_M3Nv1.1_No3203_Normal_1_20240809.log" ]]; then
        cat BSPv5.3.3_USB3F_M3Nv1.1_No3203_Normal_1_20240809.log $file > temp && mv temp $file
		echo $file done.
    fi
done

read -p "Nhấn Enter để kết thúc..."