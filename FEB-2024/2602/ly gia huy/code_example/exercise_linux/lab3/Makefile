obj-m += main.o

KERNEL := /lib/modules/$(shell uname -r)/build
KMOD_DIR := $(shell pwd)

all:
	make -C $(KERNEL) M=$(KMOD_DIR) modules

clean:
	make -C $(KERNEL) M=$(KMOD_DIR) clean