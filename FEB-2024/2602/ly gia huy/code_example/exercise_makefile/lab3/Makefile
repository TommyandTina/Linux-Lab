CC = gcc
CFLAGS = -Wall -g

DEPDIR = ./include
LIBDIR = ./lib
SRCDIR = ./src
OBJDIR = ./src/obj

OBJ = $(OBJDIR)/lab3.o $(OBJDIR)/lab3_func.o
LIBS = $(LIBDIR)/lib_socfun.a 
DEPS = $(wildcard $(DEPDIR)/*.h)

TARGET = lab3
.PHONY: all clean

all: $(TARGET)

$(TARGET): $(OBJ)
	$(CC) $(CFLAGS) -o $@ $^ $(LIBS)

$(OBJDIR)/%.o: $(SRCDIR)/%.c $(DEPS)
	$(CC) $(CFLAGS) -c -o $@ $<

clean:
	rm -rf $(OBJDIR)/*.o $(TARGET)


