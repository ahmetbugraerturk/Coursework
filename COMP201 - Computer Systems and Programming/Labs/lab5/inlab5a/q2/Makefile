CC = gcc

all: clean install run

install: program

clean:
	rm -rf *.o program

run: program
	./program

program: linkedlist.o main.o
	$(CC) -o program linkedlist.o main.o

linkedlist.o:
	$(CC) -c linkedlist.c

main.o:
	$(CC) -c main.c