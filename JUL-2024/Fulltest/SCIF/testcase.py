#!/usr/bin/python

import threading
import serial
import sys
import time
import re
import datetime
import os

list_TC = { 1:'SCIF-Normal 2.1.1_DMESG_CONFIRMATION', \
            2:'SCIF-Normal 2.1.2_INTERRUPT_CONFIRMATION',\
            3:'SCIF-Normal-2.1.3_ttySC0_115200_8_none_1',\
            4:'SCIF-Normal-2.1.4_ttySC0_9600_8_none_1',\
            5:'SCIF-Normal-2.1.5_ttySC0_38400_8_none_1',\
            6:'SCIF-Normal 2.1.6_ttySC0_230400_8_none_1',\
            7:'SCIF-Normal 2.1.7_ttySC0_921600_8_none_1',\
            8:'SCIF-Normal 2.1.8_ttySC0_115200_8_E_1',\
            9:'SCIF-Normal 2.1.9_ttySC0_115200_8_O_1',\
            10:'SCIF-Normal 2.1.10_ttySC0_115200_7_none_1',\
            11:'SCIF-Normal 2.1.11_ttySC0_115200_8_none_2',\
            12:'SCIF-Normal 2.1.12_ttySC0_115200_8_O_1',\
            13:'SCIF-Normal 2.1.13_ttySC0_115200_8_E_1',\
            15:'SCIF-Normal 2.1.15_ttySC0_57600_7_none_1',\
            16:'SCIF-Normal 2.1.16-TRANSFER_TTYSC1_PIO_9600_8_none_1',\
            17:'SCIF-Normal 2.1.17-TRANSFER_TTYSC1_PIO_38400_8_none_1',\
            18:'SCIF-Normal 2.1.18-TRANSFER_TTYSC1_PIO_115200_8_none_1',\
	    19:'SCIF-Normal 2.1.19-TRANSFER_TTYSC1_PIO_230400_8_none_1',\
            20:'SCIF-Normal 2.1.20-TRANSFER_TTYSC1_PIO_921600_8_none_1',\
            21:'SCIF-Normal 2.1.21-TRANSFER_TTYSC1_PIO_HSCIF_9600_8_none_1',\
            22:'SCIF-Normal 2.1.22-TRANSFER_TTYSC1_PIO_HSCIF_38400_8_none_1',\
            23:'SCIF-Normal 2.1.23-TRANSFER_TTYSC1_PIO_HSCIF_115200_8_none_1',\
            24:'SCIF-Normal 2.1.24-TRANSFER_TTYSC1_PIO_HSCIF_230400_8_none_1',\
            25:'SCIF-Normal 2.1.25-TRANSFER_TTYSC1_PIO_HSCIF_921600_8_none_1',\
            26:'SCIF-Normal 2.1.26-TRANSFER_TTYSC1_DMA_9600_8_none_1',\
            27:'SCIF-Normal 2.1.27-TRANSFER_TTYSC1_DMA_38400_8_none_1',\
            28:'SCIF-Normal 2.1.28-TRANSFER_TTYSC1_DMA_57600_8_none_1',\
            29:'SCIF-Normal 2.1.29-TRANSFER_TTYSC1_DMA_115200_8_none_1',\
            30:'SCIF-Normal 2.1.30-TRANSFER_TTYSC1_DMA_230400_8_none_1',\
            31:'SCIF-Normal 2.1.31-TRANSFER_TTYSC1_DMA_921600_8_none_1',\
            32:'SCIF-Normal 2.1.32-TRANSFER_TTYSC1_DMA_HSCIF_9600_8_none_1',\
            33:'SCIF-Normal 2.1.33-TRANSFER_TTYSC1_DMA_HSCIF_38400_8_none_1',\
            34:'SCIF-Normal 2.1.34-TRANSFER_TTYSC1_DMA_HSCIF_57600_8_none_1',\
            35:'SCIF-Normal 2.1.35-TRANSFER_TTYSC1_DMA_HSCIF_115200_8_none_1',\
            36:'SCIF-Normal 2.1.36-TRANSFER_TTYSC1_DMA_HSCIF_230400_8_none_1',\
            37:'SCIF-Normal 2.1.37-TRANSFER_TTYSC1_DMA_HSCIF_921600_8_none_1',\
            38:'SCIF-Normal 2.1.38-TRANSFER_TTYSC1_DMA_9600_8_none_1',\
            39:'SCIF-Normal 2.1.39-TRANSFER_TTYSC1_DMA_38400_8_none_1',\
            40:'SCIF-Normal 2.1.40-TRANSFER_TTYSC1_DMA_57600_8_none_1',\
            41:'SCIF-Normal 2.1.41-TRANSFER_TTYSC1_DMA_115200_8_none_1', \
            42:'SCIF-Normal 2.1.42-TRANSFER_TTYSC1_DMA_230400_8_none_1',\
            43:'SCIF-Normal 2.1.43-TRANSFER_TTYSC1_DMA_926100_8_none_1',\
            44:'SCIF-Normal 2.1.44-TRANSFER_TTYSC1_DMA_HSCIF_9600_8_none_1',\
            45:'SCIF-Normal 2.1.45-TRANSFER_TTYSC1_DMA_HSCIF_38400_8_none_1',\
            46:'SCIF-Normal 2.1.46-TRANSFER_TTYSC1_DMA_HSCIF_57600_8_none_1',\
            47:'SCIF-Normal 2.1.47-TRANSFER_TTYSC1_DMA_HSCIF_115200_8_none_1',\
            48:'SCIF-Normal 2.1.48-TRANSFER_TTYSC1_DMA_HSCIF_230400_8_none_1',\
            49:'SCIF-Normal 2.1.49-TRANSFER_TTYSC1_DMA_HSCIF_921600_8_none_1',\
            50:'SCIF-Normal 2.1.50-TRANSFER_TTYSC1_PIO_38400_8_none_1_AFTER S2RAM',\
            51:'SCIF-Normal 2.1.51-S2RAM_WHILE_TRANSFERRING_TTYSC1_PIO_38400_8_none_1',\
            52:'SCIF-Normal 2.1.52-TRANSFER_TTYSC1_PIO_HSCIF_38400_8_none_1_AFTER S2RAM',\
            53:'SCIF-Normal 2.1.53-S2RAM_WHILE_TRANSFERRING_TTYSC1_PIO_HSCIF_38400_8_none_1',\
            54:'SCIF-Normal 2.1.54-TRANSFER_TTYSC1_DMA_38400_8_none_1_AFTER_S2RAM',\
            55:'SCIF-Normal 2.1.55-S2RAM_WHILE_TRANSFERRING_TTYSC1_DMA_38400_8_none_1',\
            56:'SCIF-Normal 2.1.56-TRANSFER_TTYSC1_DMA_HSCIF_38400_8_none_1_AFTER_S2RAM',\
            57:'SCIF-Normal 2.1.57-S2RAM_WHILE_TRANSFERRING_TTYSC1_DMA_HSCIF_38400_8_none_1',\
            58:'SCIF-Normal 2.1.58-PULL_OUT_CABLE_WHILE_TRANSFERRING_DATA',\
            59:'SCIF-Normal 2.1.59-SMP_CONCURRENT_ACCESS_TEST',\
            60:'SCIF-Normal 2.1.60-STRESS_3600s',\
} 
