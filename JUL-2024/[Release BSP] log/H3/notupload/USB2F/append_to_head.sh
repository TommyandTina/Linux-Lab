for file in BSPv5.3.3*.log; do
    if [[ $file != "BSPv5.3.3_USB3F_H3v3.0_2219_Normal_BASE_DMA_240822.txt" ]]; then
        cat BSPv5.3.3_USB3F_H3v3.0_2219_Normal_BASE_DMA_240822.txt $file > temp && mv temp $file
		echo $file done.
    fi
done

read -p "Nhấn Enter để kết thúc..."