# memory addresses:
# n at 0x4004
# sum at 0x4008
# arr at 0x400C

movl 0x4004, %edi # move the n into register edi
movl 0x4008, %esi # move the sum intro register esi
mov $0x400C, %rdx # Pointer of the arr moved into rdx
movl 0x0, %rcx # i has been started in the register rcx as 0. I choose 64-bit because of the addl line in loop.
jmp LOOP

LOOP:
	cmpl %edi, %ecx # compare i and n to determine whether the loop will continue
	jge LOOP_END # if i is greater than or equal to n break the loop
	addl (%rdx, %rcx, 4), %esi # add the element in arr[i]: the value in (arr + i * 4) onto sum

	addl $0x2, %rcx # i increase with 2
	jmp LOOP # go the beginning of the loop

LOOP_END:
	ret # if loop is broken return and finished.
