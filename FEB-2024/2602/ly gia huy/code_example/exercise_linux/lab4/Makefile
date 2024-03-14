obj-m += main.o

TARGET = enter
SRC = enter.c
CC = gcc
CFLAGS = -Wall -g

KERNEL := /lib/modules/$(shell uname -r)/build
KMOD_DIR := $(shell pwd)

all: $(TARGET) main.ko

$(TARGET): $(SRC)
	$(CC) $(CFLAGS) -o $(TARGET) $(SRC)

main.ko:
	make -C $(KERNEL) M=$(KMOD_DIR) modules

clean:
	make -C $(KERNEL) M=$(KMOD_DIR) clean
	rm -f $(TARGET)
