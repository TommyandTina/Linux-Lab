#include <linux/build-salt.h>
#include <linux/module.h>
#include <linux/vermagic.h>
#include <linux/compiler.h>

BUILD_SALT;

MODULE_INFO(vermagic, VERMAGIC_STRING);
MODULE_INFO(name, KBUILD_MODNAME);

__visible struct module __this_module
__section(.gnu.linkonce.this_module) = {
	.name = KBUILD_MODNAME,
	.init = init_module,
#ifdef CONFIG_MODULE_UNLOAD
	.exit = cleanup_module,
#endif
	.arch = MODULE_ARCH_INIT,
};

#ifdef CONFIG_RETPOLINE
MODULE_INFO(retpoline, "Y");
#endif

static const struct modversion_info ____versions[]
__used __section(__versions) = {
	{ 0xa4b86400, "module_layout" },
	{ 0x725a8218, "cdev_del" },
	{ 0x6091b333, "unregister_chrdev_region" },
	{ 0x74007fb7, "class_destroy" },
	{ 0xf6cb2bfb, "device_destroy" },
	{ 0xd2198226, "cdev_add" },
	{ 0xb5739c63, "cdev_init" },
	{ 0x8b58c8f8, "device_create" },
	{ 0xcaed4f8, "__class_create" },
	{ 0xe3ec2f2b, "alloc_chrdev_region" },
	{ 0x56470118, "__warn_printk" },
	{ 0xb44ad4b3, "_copy_to_user" },
	{ 0x362ef408, "_copy_from_user" },
	{ 0x88db9f48, "__check_object_size" },
	{ 0xc5850110, "printk" },
	{ 0xbdfb6dbb, "__fentry__" },
};

MODULE_INFO(depends, "");


MODULE_INFO(srcversion, "C9BEC63167D5FA0206516AC");
