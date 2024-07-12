
start=2
stop=10
BOARD="H3"
sudo rm -rf ./*log
sudo chmod 777 *

TYPE="USB2"
CHANNEL="CN10L"
for ((i=$start; i<=$stop; i++))
do
    cp ../logs/*_USB2H_FULLTEST*${BOARD}*${TYPE}_S2R*${i}*${CHANNEL}.log BSPFullTest_PT3_${BOARD}_7064_USB2H_S2R_${i}_${TYPE}_${CHANNEL}_20240224.log
done

CHANNEL="CN10H"
for ((i=$start; i<=$stop; i++))
do
    cp ../logs/*_USB2H_FULLTEST*${BOARD}*${TYPE}_S2R*${i}*${CHANNEL}.log BSPFullTest_PT3_${BOARD}_7064_USB2H_S2R_${i}_${TYPE}_${CHANNEL}_20240224.log
done

CHANNEL="CN37"
for ((i=$start; i<=$stop; i++))
do
    cp ../logs/*_USB2H_FULLTEST*${BOARD}*${TYPE}_S2R*${i}*${CHANNEL}.log BSPFullTest_PT3_${BOARD}_7064_USB2H_S2R_${i}_${TYPE}_${CHANNEL}_20240224.log
done

CHANNEL="CN9"
for ((i=$start; i<=$stop; i++))
do
    cp ../logs/*_USB2H_FULLTEST*${BOARD}*${TYPE}_S2R*${i}*${CHANNEL}.log BSPFullTest_PT3_${BOARD}_7064_USB2H_S2R_${i}_${TYPE}_${CHANNEL}_20240224.log
done

TYPE="USB1"
CHANNEL="CN10L"
for ((i=$start; i<=$stop; i++))
do
    cp ../logs/*_USB2H_FULLTEST*${BOARD}*${TYPE}_S2R*${i}*${CHANNEL}.log BSPFullTest_PT3_${BOARD}_7064_USB2H_S2R_${i}_${TYPE}_${CHANNEL}_20240224.log
done

CHANNEL="CN10H"
for ((i=$start; i<=$stop; i++))
do
    cp ../logs/*_USB2H_FULLTEST*${BOARD}*${TYPE}_S2R*${i}*${CHANNEL}.log BSPFullTest_PT3_${BOARD}_7064_USB2H_S2R_${i}_${TYPE}_${CHANNEL}_20240224.log
done

CHANNEL="CN37"
for ((i=$start; i<=$stop; i++))
do
    cp ../logs/*_USB2H_FULLTEST*${BOARD}*${TYPE}_S2R*${i}*${CHANNEL}.log BSPFullTest_PT3_${BOARD}_7064_USB2H_S2R_${i}_${TYPE}_${CHANNEL}_20240224.log
done

CHANNEL="CN9"
for ((i=$start; i<=$stop; i++))
do
    cp ../logs/*_USB2H_FULLTEST*${BOARD}*${TYPE}_S2R*${i}*${CHANNEL}.log BSPFullTest_PT3_${BOARD}_7064_USB2H_S2R_${i}_${TYPE}_${CHANNEL}_20240224.log
done

TYPE="USB2HUB"
CHANNEL="CN10L"
for ((i=$start; i<=$stop; i++))
do
    cp ../logs/*_USB2H_FULLTEST*${BOARD}*${TYPE}_S2R*${i}*${CHANNEL}.log BSPFullTest_PT3_${BOARD}_7064_USB2H_S2R_${i}_${TYPE}_${CHANNEL}_20240224.log
done

CHANNEL="CN10H"
for ((i=$start; i<=$stop; i++))
do
    cp ../logs/*_USB2H_FULLTEST*${BOARD}*${TYPE}_S2R*${i}*${CHANNEL}.log BSPFullTest_PT3_${BOARD}_7064_USB2H_S2R_${i}_${TYPE}_${CHANNEL}_20240224.log
done

CHANNEL="CN37"
for ((i=$start; i<=$stop; i++))
do
    cp ../logs/*_USB2H_FULLTEST*${BOARD}*${TYPE}_S2R*${i}*${CHANNEL}.log BSPFullTest_PT3_${BOARD}_7064_USB2H_S2R_${i}_${TYPE}_${CHANNEL}_20240224.log
done

CHANNEL="CN9"
for ((i=$start; i<=$stop; i++))
do
    cp ../logs/*_USB2H_FULLTEST*${BOARD}*${TYPE}_S2R*${i}*${CHANNEL}.log BSPFullTest_PT3_${BOARD}_7064_USB2H_S2R_${i}_${TYPE}_${CHANNEL}_20240224.log
done

