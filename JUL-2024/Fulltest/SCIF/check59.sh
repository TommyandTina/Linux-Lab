while true
do
	cat 59.log | grep DONE
	cat 59.log | wc -l
	sleep 1
done

