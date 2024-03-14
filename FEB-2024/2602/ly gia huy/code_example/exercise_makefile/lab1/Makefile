CC=gcc
CFLAGS=-Wall -g
TARGET=lab1
OBJS=lab1.o lab1_func.o

all: $(TARGET)

$(TARGET): $(OBJS)
	$(CC) $(CFLAGS) -o $(TARGET) $(OBJS)

lab1.o: lab1.c lab1.h
	$(CC) $(CFLAGS) -c lab1.c -o lab1.o

lab1_func.o: lab1_func.c
	$(CC) $(CFLAGS) -c lab1_func.c -o lab1_func.o
clean:
	rm -f $(TARGET) $(OBJS)