- Đổi tên rootfs cho giống với config.PLATFORM
	sudo nano /etc/hostname
	sudo nano /etc/hosts

- Vào common/s2ram.py để đổi lại i2cset
	i2cset -f -y 8 0x30 0x20 0x0f -> i2cset -f -y 7 0x30 0x20 0x0f

- Sửa file config.py với tên board cho phù hợp

- Đổi PLATFORM trong conserial nếu ko tiện đổi trong host

- Vào common_index.py để đổi tên folder log