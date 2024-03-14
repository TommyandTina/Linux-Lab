lab1: lab1.o lab1_func.o
	gcc -o $@ $^ -I.

%.o: %.c lab1.h
	gcc -c -o $@ $< -I.
#The -I. is included so that gcc will look in the current directory (.) for the include file
clean:
	rm -f lab1.o lab1_func.o lab1