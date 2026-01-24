puzzle1:
  pushq %rbp
  movq %rsp, %rbp
  movl %edi, -20(%rbp)
  movl $0, -4(%rbp)
  movl $0, -8(%rbp)
  jmp .L2
.L5:
  movl -8(%rbp), %eax
  andl $1, %eax
  testl %eax, %eax
  jne .L3
  movl -8(%rbp), %eax
  addl %eax, -4(%rbp)
  jmp .L4
.L3:
  movl -8(%rbp), %eax
  subl %eax, -4(%rbp)
.L4:
  addl $3, -8(%rbp)
.L2:
  movl -8(%rbp), %eax
  cmpl -20(%rbp), %eax
  jl .L5
  movl -4(%rbp), %eax
  popq %rbp
  ret