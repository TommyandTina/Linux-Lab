CC = gcc
CFLAGS = -Wall -g
DEPS = lab2.h
OBJS = lab2.o lab2_func.o
TARGET = lab2

.PHONY: all clean

all: $(TARGET)

$(TARGET): $(OBJS)
	$(CC) $(CFLAGS) -o $@ $^

%.o: %.c $(DEPS)
	$(CC) $(CFLAGS) -c -o $@ $<

clean:
	rm -f $(OBJS) $(TARGET)