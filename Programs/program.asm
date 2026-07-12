// A program that tests every instruction in the ISA
// The registers should end up as:
// 0, 15, 10, 25, 5, 10, 15, 5, 4294967285, 25, 0, 0, 0, 5, 1, 27

LOADI R0, #0
// R0 = 0

LOADI R1, #15
// R1 = 15

LOADI R2, #10
// R2 = 10

ADD R3, R1, R2
// R3 = 25

SUB R4, R1, R2
// R4 = 5

AND R5, R1, R2
// R5 = 10

OR R6, R1, R2
// R6 = 15

XOR R7, R1, R2
// R7 = 5

NOT R8, R2
// R8 = 4294967285

STORE R3, 10000
// mem[10000] = 25

LOADI R9, #0
// R9 = 0

LOAD R9, 10000
// R9 = 25

LOADI R10, #1
// R10 = 1

SUB R10, R10, R10
// R10 = 0

JUMPR R10, 68
// Jump to next NOP

LOADI R11, #999
HALT
// Skipped

NOP
// Nothing happens

LOADI R12, #0
// R12 = 0
JUMP 88
//Jump to LOADI R13, #0

LOADI R12, #999
HALT
//Skipped

LOADI R13, #0
// R13 = 0

STORE R4, 10001
// mem[10001] = 5

LOAD R13, 10001
// R13 = 5

LOADI R14, #1
// R14 = 1

JUMPR R14, 116
// Does not jump as R14 != 0

LOADI R15, #27
// R15 = 27

JUMP 120
// Jumps to HALT

LOADI R15, #999
// Skipped

HALT
// End of program