TC=15

while true
do
    sudo python _index.py $TC
    cat logs/0$TC* | grep "#### Result: OK ####"
    if [ $? -eq 0 ]
    then
        break
    fi
    sleep 1
done



