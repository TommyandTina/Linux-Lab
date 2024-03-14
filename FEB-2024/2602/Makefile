%.o: %.c lab1.h
	gcc -c -o $@ $< -I.

lab1: lab1.o lab1_func.o
	gcc -o $@ $^ -I.