.globl _start
_start:
	movq $10, %rax
	movq $3, %rbx
	imulq %rbx, %rax
	addq $5, %rax
	movq %rax, %rdi
	movq $60, %rax
	syscall
