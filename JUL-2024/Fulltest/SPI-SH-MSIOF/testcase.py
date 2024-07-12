#!/usr/bin/python

import threading
import serial
import sys
import time
import re
import datetime
import os

list_TC = { 1:'Runtime PM confirmation', \
            2:'003_004_Communication_test_Master_transmission_DMA_mode', \
            5:'006_007_Communication_test_Master_transmission_PIO_mode', \
            8:'009_010_Communication_test_Master_reception_DMA_mode', \
            11:'012_013_Communication_test_Master_reception_PIO_mode', \
            14:'015_016_Communication_test_Master_Send_and_receive_DMA_mode', \
            17:'018_019_Communication_test_Master_Send_and_receive_PIO_mode', \
            20:'021_022_Communication_test_Slave_reception_DMA_mode', \
            23:'024_025_Communication_test_Slave_reception_PIO_mode', \
            26:'027_028_Communication_test_Slave_transmission_DMA_mode', \
            29:'030_031_Communication_test_Slave_transmission_PIO_mode', \
            32:'033_034_Communication_test_Slave_Send_and_receive_DMA_mode', \
            35:'036_037_Communication_test_Slave_Send_and_receive_PIO_mode', \
            381:'Memory_leak_detection_DMA_Master', \
            382:'Memory_leak_detection_DMA_Slave', \
            391:'System_deadlock_detection_DMA_Master', \
            392:'System_deadlock_detection_DMA_Slave', \
            40:'042_044_Abnormal_Communication_test_master_DMA_mode', \
            41:'043_045_Abnormal_Communication_test_master_PIO_mode', \
            46:'048_050_Abnormal_Communication_test_slave_DMA_mode', \
            47:'049_051_Abnormal_Communication_test_slave_PIO_mode', \
            52:'Abnormal_Inspection_of_the_word_size_master', \
            53:'Abnormal_Inspection_of_the_word_size_slave', \
            54:'056_058_Boundary_Communication_test_master_DMA_mode', \
            55:'057_059_Boundary_Communication_test_master_PIO_mode', \
            60:'062_064_Boundary_Communication_test_slave_DMA_mode', \
            61:'063_065_Boundary_Communication_test_slave_PIO_mode', \
            66:'Boundary_Inspection_of_the_word_size_master', \
            67:'Boundary_Inspection_of_the_word_size_slave', \
            68:'SMP_concurrent_access_test', \
            69:'SMP_multi-port_access_test', \
            70:'Multi-instance_test', \
            71:'Load_durability_test_DMA', \
            72:'Load_durability_test_PIO', \
}

