#include <linux/module.h>
#include <linux/init.h>
#include <linux/fs.h>
#include <linux/cdev.h>
#include <linux/uaccess.h>

/* Meta Information */
MODULE_LICENSE("GPL");
MODULE_AUTHOR("long.trinh-tien/Linux");
MODULE_DESCRIPTION("Ex1");


/* Variables for device and device class */
static dev_t my_device_major_minor_number;
static struct class *my_class;
static struct cdev my_device;

#define DRIVER_NAME "mydriverex1"
#define DRIVER_CLASS "MyModuleClass"


/* This function is called, when the device file is opened*/
static int driver_open(struct inode *device_file, struct file *instance) {
	printk("Device ex1 - open was called!\n");
	return 0;
}

/* This function is called, when the device file is opened*/
static int driver_close(struct inode *device_file, struct file *instance) {
	printk("Device ex1 - close was called!\n");
	return 0;
}

static struct file_operations fops = {
	.owner = THIS_MODULE,
	.open = driver_open,
	.release = driver_close,
};

/* This function is called, when the module is loaded into the kernel*/
static int __init ModuleInit(void) {
	printk("Module ex1 imported!\n");

	/* Allocate a Device ex1 see result by cat /proc/devices*/
	if( alloc_chrdev_region(&my_device_major_minor_number, 0, 1, DRIVER_NAME) < 0) {
		printk("Device ex1. could not be allocated!\n");
		return -1;
	}

	/*First 20bit is major, last 20bit is minor ->printk it out*/
	printk("Device ex1. Major: %d, Minor: %d was registered!\n", my_device_major_minor_number >> 20, my_device_major_minor_number & 0xfffff); 

	/* Create device class */
	if((my_class = class_create(THIS_MODULE, DRIVER_CLASS)) == NULL) {
		printk("Device class can not be created!\n");
		goto ClassError;
	}

	/* create device file */
	if(device_create(my_class, NULL, my_device_major_minor_number, NULL, DRIVER_NAME) == NULL) {
		printk("Can not create device file!\n");
		goto FileError;
	}

	/* Initialize device file */
	cdev_init(&my_device, &fops);

	/* Regisering device to kernel, use 'ls /dev/mydriverex2' to check */
	if(cdev_add(&my_device, my_device_major_minor_number, 1) == -1) {
		printk("Registering of device to kernel failed!\n");
		goto AddError;
	}

	return 0;
AddError:
	device_destroy(my_class, my_device_major_minor_number);
FileError:
	class_destroy(my_class);
ClassError:
	unregister_chrdev_region(my_device_major_minor_number, 1);
	return -1;
}

/* This function is called, when the module is removed from the kernel*/
static void __exit ModuleExit(void) {
	cdev_del(&my_device);
	device_destroy(my_class, my_device_major_minor_number);
	class_destroy(my_class);
	unregister_chrdev_region(my_device_major_minor_number, 1);
	printk("Goodbye, Kernel\n");
}

module_init(ModuleInit);
module_exit(ModuleExit);


