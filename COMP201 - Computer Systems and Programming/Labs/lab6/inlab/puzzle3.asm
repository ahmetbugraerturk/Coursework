puzzle3:
  pushq %rbp
  movq %rsp, %rbp
  movq %rdi, -24(%rbp)
  movl %esi, -28(%rbp)
  movl $0, -4(%rbp)
  movl $0, -8(%rbp)
.L3:
  movl -4(%rbp), %eax
  cltq
  leaq 0(,%rax,4), %rdx
  movq -24(%rbp), %rax
  addq %rdx, %rax
  movl (%rax), %eax
  movl %eax, -12(%rbp)
  cmpl $10, -12(%rbp)
  jle .L2
  addl $1, -8(%rbp)
.L2:
  addl $1, -4(%rbp)
  movl -4(%rbp), %eax
  cmpl -28(%rbp), %eax
  jl .L3
  movl -8(%rbp), %eax
  popq %rbp
  ret