CC = gcc

DEPDIR = ./cleanr
SRCDIR = ./scr
OBJDIR = ./src/obj

OBJ = $(OBJDIR)/lab2.o $(OBJDIR)/lab2_func.o

DEPS = $(wildcard $(DEPDIR)/*.h)

TARGET = lab3
.PHONY: all clean

all: $(TARGET)

$(TARGET): $(OBJ)
	$(CC) -o $@ $^ 

$(OBJDIR)/%.o: $(SRCDIR)/%.c $(DEPS)
	$(CC) -c -o $@ $<

clean:
	rm -rf $(OBJDIR)/*.o $(TARGET)
