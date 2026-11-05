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

//0x0000
LOADI R0, 0x1
//0x0004
LOADI R1, 0x0
//0x0008
LOADI R2, 0x1000


//0x000C



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




// There is currently no instruction to check whether one value is larger than another I will need to implement it in code

// For any two binary numbers if you cycle through each bit from most to least significant:
// then the number that first has a bit of 1 where the other has a 0 is the larger number

// Pseudocode:
// We want to check if num1 > num2

// num1 = value
// num2 = value + 1
// mask = 0b00000001
// for each bit:
//   num1_bit = num1 & mask
//   num2_bit = num2 & mask
//   if num1_bit - num2_bit == 0:
//     if num1_bit - 1 == 0:
//       is_greater = 1
//     else:
//       is_greater = 0
// mask = mask + mask

//if is_greater = 1 then value > value + 1

// mask = R5
// num1_bit = R6
// num2_bit = R7
// subtraction_results = R8
// is_greater = R9
// loop_tracker = R10

label Greater_Than
    LOADI R5, 0x01
    LOADI R10, 0x08
    LOADI R9, 0x0

    label For_Each_Bit
        AND R6, R3, R5
        AND R7, R4, R5
        SUB R8, R6, R7
        JUMPR R8, If_Not_Num1_Sub_Num2
        SUB R8, R6, R5
        JUMPR R8, Num1_Bit_is_0
        JUMP Num1_Bit_is_not_0

        label Num1_Bit_is_0
        LOADI R9, 0x1
        JUMP If_Not_Num1_Sub_Num2

        label Num1_Bit_is_not_0
        LOADI R9, 0x0

        label If_Not_Num1_Sub_Num2
        ADD R5, R5, R5
        SUB R10, R10, R0
        JUMPR R10, Exit_Greater_Than
        JUMP For_Each_Bit

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