#Compiler
CC = gcc
CFLAGS = -I.
#The -I. is included so that gcc will look in the current directory (.) for the include file
# Object and Dependencies
DEPS = lab2.h
OBJ = lab2.o lab2_func.o

# Object-file-making Rule
%.o: %.c $(DEPS)
	$(CC) -c -o $@ $< $(CFLAGS)

# Target file making rule
lab2: $(OBJ)
	$(CC) -o $@ $^ $(CFLAGS)

# PHONY to separate clean command with clean folder
.PHONY: clean
clean:
	rm -f $(OBJ) lab2
