CC = gcc
CFLAGS = -O0 -Wall -std=c99

all: clean compile run

compile: main.c
	$(CC) $(CFLAGS) -o main main.c

run: compile
	./main

clean:
	rm -f main
