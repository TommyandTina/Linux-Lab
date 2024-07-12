start=100
stop=$((start + 28))
for ((i=$start; i<=$stop; i++))
do
    mv "0$i.py" "$i.py"
done