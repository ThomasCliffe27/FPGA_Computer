// A bubble sort that reads sorts all of the non-zero values stored after mem addr 0x1000
// Each number is just one byte
// Pseudocode:

// sorted = False
// while !sorted:
//   foreach value - 1:
//      sorted = true
//      if value > value + 1
//          sorted = false
//          value + 1 = value
//          value = value + 1

// where value and value + 1 are pointers to the memory addresses

// R0 = 1
// sorted = R1
// value_ptr = R2
// value = R3
// value + 1 = R4

LOADI R0, 0x1
LOADI R1, 0x0
LOADI R2, 0x1000

// while !sorted

label While_Not_Sorted
    JUMPR R1, Start_Pass
    JUMP Program_End

label Start_Pass
    LOADI R2, 0x1000
    LOADI R1, 0x1

label For_Each_Value
    LOADR R3, R2
    ADD R2, R2, R0
    LOADR R4, R2
    JUMPR R4, While_Not_Sorted


// Pseudocode:
// We want to check if num1 > num2
// So CMP num1, num2
// If c == 0 JUMP ...

CMP R4, R3
JUMPC R4_Bigger
LOADI R9, 0x0
JUMP Exit_Greater_Than

label R4_Bigger
    LOADI R9, 0x1
    JUMP Exit_Greater_Than

label Exit_Greater_Than

// Now R9 will tell us if value > value + 1
// sorted = false
// swap value and value + 1



JUMPR R9, For_Each_Value
LOADI R1, 0x0
SUB R2, R2, R0
STORER R4, R2
ADD R2, R2, R0
STORER R3, R2
JUMP For_Each_Value

label Program_End
    HALT