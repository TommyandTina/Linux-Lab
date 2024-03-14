#include <linux/module.h>
#include <linux/init.h>
#include <linux/fs.h>
#include <linux/cdev.h>
#include <linux/uaccess.h>

/* Meta Information */
MODULE_LICENSE("GPL");
MODULE_AUTHOR("long.trinh-tien/Linux");
MODULE_DESCRIPTION("Ex2");

/* Buffer for data */
static char buffer[255];
static int buffer_pointer = 0;

/* Variables for device and device class */
static dev_t my_device_major_minor_number;
static struct class *my_class;
static struct cdev my_device;

#define DRIVER_NAME "mydriverex2"
#define DRIVER_CLASS "MyModuleClass"

/* Read data out of the buffer*/
static ssize_t driver_read(struct file *File, char *user_buffer, size_t count, loff_t *offs) {
	int to_copy, not_copied, delta;

	/* Get amount of data to copy */
	to_copy = min(count, buffer_pointer);

	/* Copy data to user */
	not_copied = copy_to_user(user_buffer, buffer, to_copy);

	/* Calculate data */
	delta = to_copy - not_copied;

	return delta;
}

/* Write data to buffer*/
static ssize_t driver_write(struct file *File, const char *user_buffer, size_t count, loff_t *offs) {
	int to_copy, not_copied, delta;

	/* Get amount of data to copy */
	to_copy = min(count, sizeof(buffer));

	/* Copy data to user */
	not_copied = copy_from_user(buffer, user_buffer, to_copy);
	buffer_pointer = to_copy;

	/* Calculate data */
	delta = to_copy - not_copied;

	return delta;
}

/* This function is called, when the device file is opened*/
static int driver_open(struct inode *device_file, struct file *instance) {
	printk("Device ex2 - open was called!\n");
	return 0;
}

/* This function is called, when the device file is opened*/
static int driver_close(struct inode *device_file, struct file *instance) {
	printk("Device ex2 - close was called!\n");
	return 0;
}

static struct file_operations fops = {
	.owner = THIS_MODULE,
	.open = driver_open,
	.release = driver_close,
	.read = driver_read,
	.write = driver_write
};

/* This function is called, when the module is loaded into the kernel*/
static int __init ModuleInit(void) {
	printk("Module ex2 imported!\n");

	/* Allocate a Device ex2 see result by cat /proc/devices*/
	if( alloc_chrdev_region(&my_device_major_minor_number, 0, 1, DRIVER_NAME) < 0) {
		printk("Device ex2. could not be allocated!\n");
		return -1;
	}
	printk("read_write - Device ex2. Major: %d, Minor: %d was registered!\n", my_device_major_minor_number >> 20, my_device_major_minor_number & 0xfffff);

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


