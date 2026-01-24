all: greet info log clean

greet:
	echo "Hello from the Makefile!"

info: greet
	echo "My name is Ahmet Buğra Ertürk from Lab Section A. I am writing to a log file."

log: info
	echo "This is a COMP201 log entry." > comp201_log.txt

clean: log
	rm -f comp201_log.txt
