CC=gcc

all: clean install run

install: program

clean:
	rm -f linkedlist.o main.o program

run: program
	./program

program: main.o linkedlist.o
	$(CC) -o program main.o linkedlist.o

main.o: main.c
	$(CC) -c main.c

linkedlist.o: linkedlist.c
	$(CC) -c linkedlist.c
