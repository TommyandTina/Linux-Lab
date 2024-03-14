CC = gcc
CFLAGS = -Wall -g

#direction of dependencies, library, source, object
DEPDIR = ./include
LIBDIR = ./lib
SRCDIR = ./src
OBJDIR = ./src/obj

#point to file/where to store file
OBJ = $(OBJDIR)/lab3.o $(OBJDIR)/lab3_func.o
LIBS = $(LIBDIR)/lib_socfun.a 
DEPS = $(wildcard $(DEPDIR)/*.h)

#set the target
TARGET = lab3

.PHONY: all clean

#note: how dependencies here are checked? makefile will go through down below to check if there is any update related to this dependencies
all: $(TARGET)

#more obj in same line if obj file is not in the same folder
$(TARGET): $(OBJ)
	$(CC) $(CFLAGS) -o $@ $^ $(LIBS)

#more line if source file is not in the same folder
#note: need to include .h in .c file, .h $(DEPS) here is only for checking its timestamp, it doesn't include for us
#this is the last dependencies so makefile only check for its update timestamp instead of checking down below 
$(OBJDIR)/%.o: $(SRCDIR)/%.c $(DEPS)
	$(CC) $(CFLAGS) -c -o $@ $<

clean:
	rm -rf $(OBJDIR)/*.o $(TARGET)


