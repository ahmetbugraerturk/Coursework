
f1.o:     elf64-x86-64 dosya biçemi


Disassembly of section .text:

00000000004000d4 <_start>:
  4000d4:	55                   	pushq  %rbp
  4000d5:	48 89 e5             	movq   %rsp,%rbp
  4000d8:	89 7d ec             	movl   %edi,-0x14(%rbp)
  4000db:	89 75 e8             	movl   %esi,-0x18(%rbp)
  4000de:	8b 55 ec             	movl   -0x14(%rbp),%edx
  4000e1:	8b 45 e8             	movl   -0x18(%rbp),%eax
  4000e4:	01 d0                	addl   %edx,%eax
  4000e6:	89 45 fc             	movl   %eax,-0x4(%rbp)
  4000e9:	8b 45 ec             	movl   -0x14(%rbp),%eax
  4000ec:	0f af 45 e8          	imull  -0x18(%rbp),%eax
  4000f0:	89 45 f8             	movl   %eax,-0x8(%rbp)
  4000f3:	8b 45 fc             	movl   -0x4(%rbp),%eax
  4000f6:	3b 45 f8             	cmpl   -0x8(%rbp),%eax
  4000f9:	7e 05                	jle    400100 <_start+0x2c>
  4000fb:	8b 45 fc             	movl   -0x4(%rbp),%eax
  4000fe:	eb 03                	jmp    400103 <_start+0x2f>
  400100:	8b 45 f8             	movl   -0x8(%rbp),%eax
  400103:	5d                   	popq   %rbp
  400104:	c3                   	retq   
