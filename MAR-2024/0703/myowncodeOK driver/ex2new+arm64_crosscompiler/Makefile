PWD = $(shell pwd)
CROSS_COMPILE = aarch64-linux-gnu-
ARCH=arm64
#KERNEL_SRC=/home/quang.nguyen-thanh/finalTestex2/linux_kernel_src/kernelsource-5.10.110
#KERNEL_SRC=/home/huy.pham-manh/Kernel_5_10/linux
KERNEL_SRC=/home/long.trinh-tien/Kernel_5_10/linux
obj-m += ex2.o

all:
	make ARCH=$(ARCH) CROSS_COMPILE=$(CROSS_COMPILE) -C $(KERNEL_SRC) M=$(PWD) modules

clean:
	make ARCH=$(ARCH) CROSS_COMPILE=$(CROSS_COMPILE) -C $(KERNEL_SRC) M=$(PWD) clean