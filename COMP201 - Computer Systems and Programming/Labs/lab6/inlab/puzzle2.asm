puzzle2:
  pushq %rbp
  movq %rsp, %rbp
  movl %edi, -20(%rbp)
  movl $0, -4(%rbp)
  movl $1, -8(%rbp)
.L4:
  movl -8(%rbp), %eax
  addl %eax, %eax
  addl %eax, -4(%rbp)
  movl -8(%rbp), %eax
  cmpl -20(%rbp), %eax
  jge .L7
  addl $1, -8(%rbp)
  jmp .L4
.L7:
  nop
  movl -4(%rbp), %eax
  popq %rbp
  ret