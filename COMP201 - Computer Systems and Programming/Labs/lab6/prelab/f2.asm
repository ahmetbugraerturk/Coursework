
f2.o:     elf64-x86-64 dosya biçemi


Disassembly of section .text:

00000000004000d4 <f2>:
  4000d4:	55                   	pushq  %rbp
  4000d5:	48 89 e5             	movq   %rsp,%rbp
  4000d8:	48 89 7d e8          	movq   %rdi,-0x18(%rbp)
  4000dc:	89 75 e4             	movl   %esi,-0x1c(%rbp)
  4000df:	48 c7 45 f8 00 00 00 	movq   $0x0,-0x8(%rbp)
  4000e6:	00 
  4000e7:	eb 36                	jmp    40011f <f2+0x4b>
  4000e9:	48 8b 45 f8          	movq   -0x8(%rbp),%rax
  4000ed:	48 8d 14 85 00 00 00 	leaq   0x0(,%rax,4),%rdx
  4000f4:	00 
  4000f5:	48 8b 45 e8          	movq   -0x18(%rbp),%rax
  4000f9:	48 01 d0             	addq   %rdx,%rax
  4000fc:	8b 00                	movl   (%rax),%eax
  4000fe:	83 f8 fb             	cmpl   $0xfffffffb,%eax
  400101:	7d 17                	jge    40011a <f2+0x46>
  400103:	48 8b 45 f8          	movq   -0x8(%rbp),%rax
  400107:	48 8d 14 85 00 00 00 	leaq   0x0(,%rax,4),%rdx
  40010e:	00 
  40010f:	48 8b 45 e8          	movq   -0x18(%rbp),%rax
  400113:	48 01 d0             	addq   %rdx,%rax
  400116:	8b 00                	movl   (%rax),%eax
  400118:	eb 16                	jmp    400130 <f2+0x5c>
  40011a:	48 83 45 f8 01       	addq   $0x1,-0x8(%rbp)
  40011f:	8b 45 e4             	movl   -0x1c(%rbp),%eax
  400122:	48 98                	cltq   
  400124:	48 3b 45 f8          	cmpq   -0x8(%rbp),%rax
  400128:	7f bf                	jg     4000e9 <f2+0x15>
  40012a:	48 8b 45 e8          	movq   -0x18(%rbp),%rax
  40012e:	8b 00                	movl   (%rax),%eax
  400130:	5d                   	popq   %rbp
  400131:	c3                   	retq   
