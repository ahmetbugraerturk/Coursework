CC = gcc
CFLAGS = -std=c99
TARGET = lab6_test
OBJS = tester.o

all: $(TARGET)
	./$(TARGET)

$(TARGET): puzzles.c $(OBJS)
	$(CC) $(CFLAGS) puzzles.c $(OBJS) -o $(TARGET)

clean:
	rm -f $(TARGET)