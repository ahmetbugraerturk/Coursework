//I am Ahmet Buğra Ertürk. I hereby declare that I have completed this assignment with honesty and integrity.
//Answer: GOOD!
#if 0
/*
 * Instructions to Students:
 *
 * STEP 1: Read the following instructions carefully.
 */



INTEGER CODING RULES:
 
  Replace the "return" statement in each function with one
  or more lines of C code that implements the function. Your code 
  must conform to the following style:
 
  int Funct(arg1, arg2, ...) {
      /* brief description of how your implementation works */
      int var1 = Expr1;
      ...
      int varM = ExprM;

      varJ = ExprJ;
      ...
      varN = ExprN;
      return ExprR;
  }

  Each "Expr" is an expression using ONLY the following:
  1. Integer constants 0 through 255 (0xFF), inclusive. You are
      not allowed to use big constants such as 0xffffffff.
  2. Function arguments and local variables (no global variables).
  3. Unary integer operations ! ~
  4. Binary integer operations & ^ | + << >>
    
  Some of the problems restrict the set of allowed operators even further.
  Each "Expr" may consist of multiple operators. You are not restricted to
  one operator per line.

  You are expressly forbidden to:
  1. Use any control constructs such as if, do, while, for, switch, etc.
  2. Define or use any macros.
  3. Define any additional functions in this file.
  4. Call any functions.
  5. Use any other operations, such as &&, ||, -, or ?:
  6. Use any form of casting.
  7. Use any data type other than int.  This implies that you
     cannot use arrays, structs, or unions.

 
  You may assume that your machine:
  1. Uses 2s complement, 32-bit representations of integers.
  2. Performs right shifts arithmetically.
  3. Has unpredictable behavior when shifting an integer by more
     than the word size.


FLOATING POINT CODING RULES

For the problems that require you to implent floating-point operations,
the coding rules are less strict.  You are allowed to use looping and
conditional control.  You are allowed to use both ints and unsigneds.
You can use arbitrary integer and unsigned constants.

You are expressly forbidden to:
  1. Define or use any macros.
  2. Define any additional functions in this file.
  3. Call any functions.
  4. Use any form of casting.
  5. Use any data type other than int or unsigned.  This means that you
     cannot use arrays, structs, or unions.
  6. Use any floating point data types, operations, or constants.


NOTES:
  1. Use the dlc (data lab checker) compiler (described in the handout) to 
     check the legality of your solutions.
  2. Each function has a maximum number of operators (! ~ & ^ | + << >>)
     that you are allowed to use for your implementation of the function. 
     The max operator count is checked by dlc. Note that '=' is not 
     counted; you may use as many of these as you want without penalty.
  3. Use the btest test harness to check your functions for correctness.
  4. Use the BDD checker to formally verify your functions
  5. The maximum number of ops for each function is given in the
     header comment for each function. If there are any inconsistencies 
     between the maximum ops in the writeup and in this file, consider
     this file the authoritative source.

/*
 * STEP 2: Modify the following functions according the coding rules.
 * 
 *   IMPORTANT. TO AVOID GRADING SURPRISES:
 *   1. Use the dlc compiler to check that your solutions conform
 *      to the coding rules.
 *   2. Use the BDD checker to formally verify that your solutions produce 
 *      the correct answers.
 */


#endif

//1
/* 
 * bitXor - x^y using only ~ and & 
 *   Example: bitXor(4, 5) = 1
 *   Legal ops: ~ &
 *   Max ops: 14
 *   Rating: 1
 */

int bitXor(int x, int y) {
   /*
    * I just wrote the xor operation using only and and not operations.
    */
   return ~(~(x&(~y))&(~((~x)&y)));

}


/* 
 * allOddBits - return 1 if all odd-numbered bits in word set to 1
 *   Examples allOddBits(0xFFFFFFFD) = 0, allOddBits(0xAAAAAAAA) = 1
 *   Legal ops: ! ~ & ^ | + << >>
 *   Max ops: 12
 *   Rating: 2
 */
int allOddBits(int x) {
   /*
    * using 8-bit 10101010 masks because of the limitation
    * apply & operator to our input to check whether all odd-numbered bits of the first 8-bit of the input are 1
    * then shifting input 8, 16, and 24-bits right to check the other 8-bit
    * finally i have totally 4 8-bit int which are 10101010 or versions where some of the 1s are 0s
    * all of them must be 10101010 if all odd-numbered bits are 1
    * so i checked them with using & operator and if all of them are 10101010, the output is also 10101010.
    * to reach the single binary to return i checked these and operations with 10101010 XOR my_output
    * if my output is 10101010, the result is 00000000 then if add ! at the begining it will be 1.
    * utherwise the result contains at least one 1(s) then after ! operation it will be 0
    */
   int msk = 0xAA; //10101010
   int bit8 = (x&msk);
   int bit16 = ((x>>8)&msk);
   int bit24 = ((x>>16)&msk);
   int bit32 = ((x>>24)&msk);

   return !(msk^(bit8&bit16&bit24&bit32));

}


//4
/* 
 * logicalNeg - implement the ! operator, using all of 
 *              the legal operators except !
 *   Examples: logicalNeg(3) = 0, logicalNeg(0) = 1
 *   Legal ops: ~ & ^ | + << >>
 *   Max ops: 12
 *   Rating: 4 
 */
int logicalNeg(int x) {
   /*
    * first i take the 2s complemet of the x since if x is 0, ~x+1 will be 0 because of overflow
    * then when i shifted them 31-bit they are going to be 0 (000..000)
    * for other numbers (except 0x80000000) when i apply same process if x is positive, x>>31=0 (000..000) and (~x+1)>>31=-1 (111..111); if x is negative, vice versa.
    * and as an edge case if x = 0x80000000, x is equal to ~x+1, which is 1000...00, so both sign bit is 1. Therefore when i apply shifting, both is going to be -1 (111..111)
    * then when i apply OR (|) operator between x and ~x+1, if x=0, the result is 0 (000..000); if x=0x80000000 and another integer, the result is -1 (111..111)
    * finally i add them +1 then if x=0, the result will be 1; if x is not 0, the result will be 0
    */
   return (((~x+1)>>31)|(x>>31))+1;
}
