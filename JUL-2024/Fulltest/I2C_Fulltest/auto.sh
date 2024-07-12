#!/bin/bash

for ((i=1; i<=100; i++)); do
    python _index.py 13
    mv "logs/013_I2C-Normal-2.1.13-I2C_UNBIND_BIND_DEVICE_TEST.log" 13/$i"_013_I2C-Normal-2.1.13-I2C_UNBIND_BIND_DEVICE_TEST.log"
done
