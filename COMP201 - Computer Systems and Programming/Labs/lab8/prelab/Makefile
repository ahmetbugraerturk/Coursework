all: clean install run

clean:
	rm -rf main
	rm -rf main.dSYM

install: main.c
	gcc -g -ggdb main.c -o main

run: main
	./main
